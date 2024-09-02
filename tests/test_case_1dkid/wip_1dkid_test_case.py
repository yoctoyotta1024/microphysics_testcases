"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: wip_1dkid_test_case.py
Project: test_case_1dkid
Created Date: Sunday 1st September 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 2nd September 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

# %% Function definitions
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from PyMPDATA_examples import Shipway_and_Hill_2012 as kid

from kid_dynamics import KiDDynamics

# %% Easy Callable Settings

### path to directory to save data/plots in after model run
binpath = Path(__file__).parent.resolve() / "bin"  # i.e. [current directory]/bin/
binpath.mkdir(parents=False, exist_ok=True)

### Setup constants
BASE_DT = 0.25 * kid.si.s
NRS0 = 32
DZS0 = 100 * kid.si.m
AUTO_DT = 0  # note: dt = AUTO_DT -> adaptive timestepping

### settings for grid, timesteps and KiD
dt = BASE_DT / 2
dz = 25 * kid.si.m
nr = 1  # note: nr=1 -> bulk scheme microphysics

N_CCN_HALO = 500 / kid.si.mg
R_MIN = 1 * kid.si.um
R_MAX = 20.2 * kid.si.um

# %% Run 1-D KiD Model
kiddyn = KiDDynamics(nr, dz, dt, R_MIN, R_MAX, N_CCN_HALO)

outputs = {}
output = {
    k: np.zeros((kiddyn.settings.nz, kiddyn.settings.nt + 1))
    for k in ("qv", "S", "ql", "act_frac", "reldisp")
}
outputs[kiddyn.key] = output
assert "t" not in output and "z" not in output
output["t"] = np.linspace(
    0, kiddyn.settings.nt * kiddyn.settings.dt, kiddyn.settings.nt + 1, endpoint=True
)
output["z"] = np.linspace(
    kiddyn.settings.dz / 2,
    (kiddyn.settings.nz - 1 / 2) * kiddyn.settings.dz,
    kiddyn.settings.nz,
    endpoint=True,
)
output["qv"][:, 0] = kiddyn.mpdata["qv"].advectee.get()


for t in range(kiddyn.settings.nt):
    GC = (
        kiddyn.settings.rhod_w((t + 0.5) * kiddyn.settings.dt)
        * kiddyn.settings.dt
        / kiddyn.settings.dz
    )
    advector_0 = np.ones_like(kiddyn.settings.z_vec) * GC
    kiddyn.mpdata["qv"].advector.get_component(0)[:] = advector_0
    kiddyn.mpdata["qv"].advance(1)

    qv = kiddyn.mpdata["qv"].advectee.get()
    RH = kid.formulae.pv(kiddyn.prof["p"], qv) / kiddyn.prof["pvs"]

    kiddyn.mpdata["ql"].advector.get_component(0)[:] = advector_0
    ql = kiddyn.mpdata["ql"].advectee.get()
    dql_cond = np.maximum(0, qv * (1 - 1 / RH))
    ql += dql_cond
    qv -= dql_cond

    output["ql"][:, t + 1] = ql
    output["qv"][:, t + 1] = qv
    output["S"][:, t + 1] = RH - 1

# %% plot results
cmap = "gray"
rasterized = False
figsize = (3.5, 3.5)
print(kiddyn.key)

kid.plot(
    var="qv",
    mult=1e3,
    label="$q_v$ [g/kg]",
    output=outputs[f"{kiddyn.key}"],
    cmap=cmap,
    threshold=1e-3,
)
savename = binpath / "kid1d_qvap.png"
plt.savefig(savename, bbox_inches="tight")

kid.plot(
    var="ql",
    mult=1e3,
    label="$q_l$ [g/kg]",
    output=outputs[f"{kiddyn.key}"],
    cmap=cmap,
    threshold=1e-3,
    figsize=figsize,
)
savename = binpath / "kid1d_qcond.png"
plt.savefig(savename, bbox_inches="tight")

kid.plot(
    var="S",
    mult=1e2,
    label="$S$ [%]",
    rng=(-0.25, 0.75),
    output=outputs[f"{kiddyn.key}"],
    cmap=cmap + "_r",
    figsize=figsize,
)
savename = binpath / "kid1d_supersat.png"
plt.savefig(savename, bbox_inches="tight")
