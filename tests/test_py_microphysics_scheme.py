"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_mock_py_microphysics_scheme.py
Project: tests
Created Date: Tuesday 27th February 2024
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
mock unit tests for Python microphysics module
"""

import numpy as np
import os
import sys

sys.path.append(os.environ["PY_GRAUPEL_DIR"])
from libs.graupel.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper, py_graupel

from libs.thermo.thermodynamics import Thermodynamics

def test_initialize():

    microphys = py_graupel.Graupel() 

    assert microphys.initialize() is None


def test_finalize():
    microphys = py_graupel.Graupel() 

    assert microphys.finalize() is None


def test_initialize_wrapper():
    nvec = 1
    ke = 1
    ivstart = 0
    dz = 10
    qnc = 500
    microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

    assert microphys_wrapped.initialize() == 0


def test_finalize_wrapper():
    nvec = 1
    ke = 1
    ivstart = 0
    dz = 10
    qnc = 500
    microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

    assert microphys_wrapped.finalize() == 0


def test_microphys_with_wrapper():
    microphys = py_graupel.Graupel() 
    nvec = 1
    ke = 1
    ivstart = 0
    dz = np.array([10.], np.float64)
    qnc = 500
    microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

    timestep = 1.0
    temp = np.array([288.15])
    rho = np.array([1.225])
    press = np.array([101325])
    qvap = np.array([0.015])
    qcond = np.array([0.0001])
    qice = np.array([0.0002])
    qrain = np.array([0.0003])
    qsnow = np.array([0.0004])
    qgrau = np.array([0.0005])

    thermo = Thermodynamics(temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau)

    prr_gsp = np.zeros(nvec, np.float64)
    pri_gsp = np.zeros(nvec, np.float64)
    prs_gsp = np.zeros(nvec, np.float64)
    prg_gsp = np.zeros(nvec, np.float64)
    pflx = np.zeros((ke, nvec), np.float64)

    microphys.run(
        ncells=nvec,
        nlev=ke,
        dt=timestep,
        dz=dz,
        t=temp,
        rho=rho,
        p=press,
        qv=qvap,
        qc=qcond,
        qi=qice,
        qr=qrain,
        qs=qsnow,
        qg=qgrau,
        qnc=qnc,
        prr_gsp=prr_gsp,
        pri_gsp=pri_gsp,
        prs_gsp=prs_gsp,
        prg_gsp=prg_gsp,
        pflx=pflx
    )

    thermo = microphys_wrapped.run(timestep, thermo)

    assert thermo.temp == temp
    assert thermo.massmix_ratios == [qvap, qcond, qice, qrain, qsnow, qgrau]
