"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_mock_microphys_microphysics_scheme.py
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

from libs.mock_microphys.mock_microphysics_scheme import MicrophysicsScheme
from libs.mock_microphys.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper
from libs.thermo.thermodynamics import Thermodynamics


def test_initialize():
    microphys = MicrophysicsScheme()

    assert microphys.initialize() is None


def test_finalize():
    microphys = MicrophysicsScheme()

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
    microphys = MicrophysicsScheme()

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
    wvel = uvel = vvel = np.array([])  # this microphysics test doesn't need winds

    thermo = Thermodynamics(
        temp,
        rho,
        press,
        qvap,
        qcond,
        qice,
        qrain,
        qsnow,
        qgrau,
        wvel,
        uvel,
        vvel,
    )

    t, qv, qc, qi, qr, qs, qg, prr_gsp, pflx = microphys.run(
        nvec,
        ke,
        ivstart,
        timestep,
        dz,
        temp,
        rho,
        press,
        qvap,
        qcond,
        qice,
        qrain,
        qsnow,
        qgrau,
        qnc,
    )

    result = microphys_wrapped.run(timestep, thermo)

    assert result.temp == t
    assert result.unpack_massmix_ratios() == [qv, qc, qi, qr, qs, qg]
