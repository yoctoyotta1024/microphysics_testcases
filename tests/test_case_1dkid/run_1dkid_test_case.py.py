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

import numpy as np
from PyMPDATA import Options

# from PyMPDATA.impl.enumerations import ARG_DATA_INNER, ARG_DATA, ONE_FOR_STAGGERED_GRID
from PyMPDATA_examples import Shipway_and_Hill_2012 as kid


def label(options, nr, dz, dt):
    return f"nr={nr}_dz={dz}_dt={dt}_opt={options}"


def adapt_dt(nr, dz, NRS0, DZS0, BASE_DT):
    r_ratio = NRS0 / nr
    z_ratio = dz / DZS0
    if r_ratio == 1 or z_ratio == 1:
        return BASE_DT * r_ratio * z_ratio
    return BASE_DT * min(r_ratio, z_ratio)


### Setup constants
BASE_DT = 0.25 * kid.si.s
NRS0 = 32
DZS0 = 100 * kid.si.m
AUTO_DT = 0  # note: dt = AUTO_DT -> adaptive timestepping

### settings for grid, timesteps and KiD
dt = AUTO_DT
dz = 25 * kid.si.m
# idz = 0
# idt = 0
NRS = (32, 16, 64, 128)  # note: NR=1 -> bulk scheme microphysics
RHOD_VERTVELO = 3 * kid.si.m / kid.si.s * kid.si.kg / kid.si.m**3
T_MAX = 15 * kid.si.minutes
P0 = 1007 * kid.si.hPa
Z_MAX = 3200 * kid.si.m
N_CCN_HALO = 500 / kid.si.mg
R_MIN = 1 * kid.si.um
R_MAX = 20.2 * kid.si.um

# ANIM = False
options = Options(n_iters=3, nonoscillatory=True)
outputs = {}
for inr, nr in enumerate(sorted(NRS)):
    if dt == AUTO_DT:
        dt = adapt_dt(nr, dz, NRS0, DZS0, BASE_DT)

    key = label(options, nr, dz, dt)
    if key in outputs:
        continue
    if nr < NRS0 and dz != DZS0:
        continue
    if dz > DZS0 and nr != NRS0:
        continue

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
