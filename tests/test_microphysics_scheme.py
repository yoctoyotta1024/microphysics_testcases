"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_mock_py_microphysics_scheme.py
Project: tests
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 11th November 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
mock unit tests for Python microphysics module
"""

import numpy as np
from copy import deepcopy

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
    dz = np.array([10], dtype=np.float64)
    qnc = 500
    microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

    assert microphys_wrapped.initialize() == 0


def test_finalize_wrapper():
    nvec = 1
    ke = 1
    ivstart = 0
    dz = np.array([10], dtype=np.float64)
    qnc = 500
    microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

    assert microphys_wrapped.finalize() == 0


def test_microphys_with_wrapper():
    microphys = py_graupel.Graupel() 
    nvec = 1
    ke = 1
    ivstart = 0
    dz = np.array([10], dtype=np.float64)
    qnc = 500
    microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

    timestep = 1.0
    temp = np.array([288.15], dtype=np.float64)
    rho = np.array([1.225], dtype=np.float64)
    press = np.array([101325], dtype=np.float64)
    qvap = np.array([0.015], dtype=np.float64)
    qcond = np.array([0.0001], dtype=np.float64)
    qice = np.array([0.0002], dtype=np.float64)
    qrain = np.array([0.0003], dtype=np.float64)
    qsnow = np.array([0.0004], dtype=np.float64)
    qgrau = np.array([0.0005], dtype=np.float64)

    thermo = Thermodynamics(temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau)

    prr_gsp = np.zeros(nvec, np.float64)
    pri_gsp = np.zeros(nvec, np.float64)
    prs_gsp = np.zeros(nvec, np.float64)
    prg_gsp = np.zeros(nvec, np.float64)
    pflx = np.zeros((ke, nvec), np.float64)

    # temporary variable
    total_ice = qgrau + qsnow + qice
      
    # call saturation adjustment
    py_graupel.saturation_adjustment(
        ncells=nvec,
        nlev=ke,
        ta=temp,
        qv=qvap,
        qc=qcond,
        qr=qrain,
        total_ice=total_ice,
        rho=rho,
    )

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
 
    # call saturation adjustment
    py_graupel.saturation_adjustment(
        ncells=nvec,
        nlev=ke,
        ta=temp,
        qv=qvap,
        qc=qcond,
        qr=qrain,
        total_ice=total_ice,
        rho=rho,
    )
       
    result = microphys_wrapped.run(timestep, thermo)

    assert result.temp == temp  
    assert result.massmix_ratios == [qvap, qcond, qice, qrain, qsnow, qgrau]
