"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: run_1dkid_test_case.py.py
Project: test_case_1dkid
Created Date: Sunday 1st September 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Sunday 1st September 2024
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
import numba
from pathlib import Path
from PyMPDATA import Options
from PyMPDATA.impl.enumerations import ARG_DATA_INNER, ARG_DATA, ONE_FOR_STAGGERED_GRID
from PyMPDATA_examples import Shipway_and_Hill_2012 as kid


def label(options, nr, dz, dt):
    return f"nr={nr}_dz={dz}_dt={dt}_opt={options}"


def adapt_dt(nr, dz, NRS0, DZS0, BASE_DT):
    r_ratio = NRS0 / nr
    z_ratio = dz / DZS0
    if r_ratio == 1 or z_ratio == 1:
        return BASE_DT * r_ratio * z_ratio
    return BASE_DT * min(r_ratio, z_ratio)


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
dt = AUTO_DT
dz = 25 * kid.si.m
nr = 1  # note: nr=1 -> bulk scheme microphysics
RHOD_VERTVELO = 3 * kid.si.m / kid.si.s * kid.si.kg / kid.si.m**3
T_MAX = 15 * kid.si.minutes
P0 = 1007 * kid.si.hPa
Z_MAX = 3200 * kid.si.m
N_CCN_HALO = 500 / kid.si.mg
R_MIN = 1 * kid.si.um
R_MAX = 20.2 * kid.si.um

# %% Run 1-D KiD Model
options = Options(n_iters=3, nonoscillatory=True)
outputs = {}
if dt == AUTO_DT:
    dt = adapt_dt(nr, dz, NRS0, DZS0, BASE_DT)
key = label(options, nr, dz, dt)

settings = kid.Settings(
    rhod_w_const=RHOD_VERTVELO,
    nr=nr,
    dt=dt,
    dz=dz,
    t_max=T_MAX,
    r_min=R_MIN,
    r_max=R_MAX,
    p0=P0,
    z_max=Z_MAX,
)
print(f"Simulating {settings.nt} timesteps using {key}")

mpdata = kid.MPDATA(
    nr=nr,
    nz=settings.nz,
    dt=settings.dt,
    qv_of_zZ_at_t0=lambda zZ: settings.qv(zZ * settings.dz),
    g_factor_of_zZ=lambda zZ: settings.rhod(zZ * settings.dz),
    options=options,
    activation_bc=kid.DropletActivation(N_CCN_HALO, settings.dr, settings.dz),
)

output = {
    k: np.zeros((settings.nz, settings.nt + 1))
    for k in ("qv", "S", "ql", "act_frac", "reldisp")
}
outputs[key] = output

halo = mpdata.options.n_halo
dpsi_shape = mpdata["ql"].advectee.get().shape


@numba.experimental.jitclass([("dpsi_cond", numba.float64[:, :])])
class PostIter:  # pylint: disable=too-few-public-methods
    def __init__(self):
        self.dpsi_cond = np.zeros(dpsi_shape)

    def call(self, flux, g_factor, t, it):  # pylint: disable=unused-argument
        if it == 0:
            self.dpsi_cond[:] = 0
        flux_wo_halo = flux[ARG_DATA_INNER][
            halo:-halo, halo - 1 : halo - 1 + nr + ONE_FOR_STAGGERED_GRID
        ]
        self.dpsi_cond[:] -= (flux_wo_halo[:, 1:] - flux_wo_halo[:, :-1]) / g_factor[
            ARG_DATA
        ][halo:-halo, halo:-halo]


post_iter = PostIter() if nr > 1 else None

assert "t" not in output and "z" not in output
output["t"] = np.linspace(0, settings.nt * settings.dt, settings.nt + 1, endpoint=True)
output["z"] = np.linspace(
    settings.dz / 2, (settings.nz - 1 / 2) * settings.dz, settings.nz, endpoint=True
)
output["qv"][:, 0] = mpdata["qv"].advectee.get()

prof = {}
prof["rhod"] = settings.rhod(output["z"])
prof["T"] = kid.formulae.temperature(prof["rhod"], settings.thd(output["z"]))
prof["p"] = kid.formulae.pressure(prof["rhod"], prof["T"], output["qv"][:, 0])
prof["pvs"] = kid.formulae.pvs_Celsius(prof["T"] - kid.const.T0)

Gscl = prof["rhod"]

for t in range(settings.nt):
    GC = settings.rhod_w((t + 0.5) * settings.dt) * settings.dt / settings.dz
    advector_0 = np.ones_like(settings.z_vec) * GC
    mpdata["qv"].advector.get_component(0)[:] = advector_0
    mpdata["qv"].advance(1)

    qv = mpdata["qv"].advectee.get()
    RH = kid.formulae.pv(prof["p"], qv) / prof["pvs"]

    mpdata["ql"].advector.get_component(0)[:] = advector_0
    ql = mpdata["ql"].advectee.get()
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
print(key)

kid.plot(
    var="qv",
    mult=1e3,
    label="$q_v$ [g/kg]",
    output=outputs[f"{key}"],
    cmap=cmap,
    threshold=1e-3,
)
savename = binpath / "kid1d_qvap.png"
plt.savefig(savename, bbox_inches="tight")

kid.plot(
    var="ql",
    mult=1e3,
    label="$q_l$ [g/kg]",
    output=outputs[f"{key}"],
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
    output=outputs[f"{key}"],
    cmap=cmap + "_r",
    figsize=figsize,
)
savename = binpath / "kid1d_supersat.png"
plt.savefig(savename, bbox_inches="tight")
