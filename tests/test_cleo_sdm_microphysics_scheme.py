"""
Copyright (c) 2025 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_cleo_sdm_microphysics_scheme.py
Project: tests
Created Date: Monday 23rd June 2025
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 23rd June 2025
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
unit tests for cleo_sdm microphysics module
"""

import pytest
import numpy as np

# from libs.cleo_sdm.cleo_sdm import CleoSDM as MicrophysicsScheme
from libs.cleo_sdm.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper

# from libs.thermo.thermodynamics import Thermodynamics


@pytest.fixture(scope="module")
def cleo_path2pycleo(pytestconfig):
    return pytestconfig.getoption("cleo_path2pycleo")


@pytest.fixture(scope="module")
def cleo_config_filename(pytestconfig):
    return pytestconfig.getoption("cleo_test_generic_config_filename")


# def test_initialize(): WIP
#     microphys = MicrophysicsScheme()

#     assert microphys.initialize() is None


# def test_finalize(): WIP
#     microphys = MicrophysicsScheme()

#     assert microphys.finalize() is None


def test_cleo_initialize_wrapper(cleo_path2pycleo, cleo_config_filename):
    t_start = 0
    timestep = 3
    press = np.array([], dtype=np.float64)
    temp = np.array([], dtype=np.float64)
    qvap = np.array([], dtype=np.float64)
    qcond = np.array([], dtype=np.float64)
    microphys_wrapped = MicrophysicsSchemeWrapper(
        cleo_path2pycleo,
        cleo_config_filename,
        t_start,
        timestep,
        press,
        temp,
        qvap,
        qcond,
    )

    assert microphys_wrapped.initialize() == 0


# def test_finalize_wrapper():
#     microphys_wrapped = MicrophysicsSchemeWrapper()

#     assert microphys_wrapped.finalize() == 0


# def test_microphys_with_wrapper():
#     microphys = MicrophysicsScheme()

#     microphys_wrapped = MicrophysicsSchemeWrapper()

#     timestep = 1.0
#     temp = np.array([288.15], dtype=np.float64)
#     rho = np.array([1.225], dtype=np.float64)
#     press = np.array([101325], dtype=np.float64)
#     qvap = np.array([0.015], dtype=np.float64)
#     qcond = np.array([0.0001], dtype=np.float64)
#     qice = np.array([0.0002], dtype=np.float64)
#     qrain = np.array([0.0003], dtype=np.float64)
#     qsnow = np.array([0.0004], dtype=np.float64)
#     qgrau = np.array([0.0005], dtype=np.float64)

#     thermo = Thermodynamics(temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau)

#     p, t, qv, qc = microphys.run(
#         timestep,
#         temp,
#         press,
#         qvap,
#         qcond,
#     )

#     result = microphys_wrapped.run(timestep, thermo)

#     assert result.press == p
#     assert result.temp == t
#     assert result.massmix_ratios == [qv, qc, qice, qrain, qsnow, qgrau]
