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


@pytest.fixture(scope="module")
def path2pycleo(pytestconfig):
    return pytestconfig.getoption("cleo_path2pycleo")


@pytest.fixture(scope="module")
def config_filename(pytestconfig):
    return pytestconfig.getoption("cleo_test_generic_config_filename")


def test_generic_cleo(path2pycleo, config_filename):
    # TODO(CB): fix multiple kokkos initialise error -> call each test seperately
    import os
    import sys
    import numpy as np
    from mpi4py import MPI

    os.environ["PYCLEO_DIR"] = str(path2pycleo)

    from libs.cleo_sdm.cleo_sdm import CleoSDM as MicrophysicsScheme
    from libs.cleo_sdm.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper
    from libs.thermo.thermodynamics import Thermodynamics

    sys.path.append(os.environ["PYCLEO_DIR"])
    import pycleo

    def test_initialize(config_filename):
        from ruamel.yaml import YAML

        yaml = YAML()
        with open(config_filename, "r") as file:
            python_config = yaml.load(file)

        t_start = 0
        timestep = python_config["timesteps"]["COUPLTSTEP"]  # [s]
        press = np.array([], dtype=np.float64)
        temp = np.array([], dtype=np.float64)
        qvap = np.array([], dtype=np.float64)
        qcond = np.array([], dtype=np.float64)
        config = pycleo.Config(str(config_filename))
        microphys = MicrophysicsScheme(
            config, t_start, timestep, press, temp, qvap, qcond
        )

        assert microphys.name == "CLEO SDM microphysics"

    def test_initialize_wrapper(config_filename):
        from ruamel.yaml import YAML

        yaml = YAML()
        with open(config_filename, "r") as file:
            python_config = yaml.load(file)

        t_start = 0
        timestep = python_config["timesteps"]["COUPLTSTEP"]  # [s]
        press = np.array([], dtype=np.float64)
        temp = np.array([], dtype=np.float64)
        qvap = np.array([], dtype=np.float64)
        qcond = np.array([], dtype=np.float64)
        microphys_wrapped = MicrophysicsSchemeWrapper(
            config_filename,
            t_start,
            timestep,
            press,
            temp,
            qvap,
            qcond,
        )

        assert microphys_wrapped.initialize() == 0

    def test_finalize_wrapper(config_filename):
        from ruamel.yaml import YAML

        yaml = YAML()
        with open(config_filename, "r") as file:
            python_config = yaml.load(file)

        t_start = 0
        timestep = python_config["timesteps"]["COUPLTSTEP"]  # [s]
        press = np.array([], dtype=np.float64)
        temp = np.array([], dtype=np.float64)
        qvap = np.array([], dtype=np.float64)
        qcond = np.array([], dtype=np.float64)
        microphys_wrapped = MicrophysicsSchemeWrapper(
            config_filename,
            t_start,
            timestep,
            press,
            temp,
            qvap,
            qcond,
        )

        assert microphys_wrapped.finalize() == 0

    def test_microphys_with_wrapper(config_filename):
        from ruamel.yaml import YAML

        yaml = YAML()
        with open(config_filename, "r") as file:
            python_config = yaml.load(file)

        t_start = 0
        timestep = python_config["timesteps"]["COUPLTSTEP"]  # [s]
        temp1 = np.array([288.15], dtype=np.float64)
        temp2 = np.array([288.15], dtype=np.float64)
        rho = np.array([1.225], dtype=np.float64)
        press1 = np.array([101325], dtype=np.float64)
        press2 = np.array([101325], dtype=np.float64)
        qvap1 = np.array([0.015], dtype=np.float64)
        qvap2 = np.array([0.015], dtype=np.float64)
        qcond1 = np.array([0.0001], dtype=np.float64)
        qcond2 = np.array([0.0001], dtype=np.float64)
        qice = np.array([0.0002], dtype=np.float64)
        qrain = np.array([0.0003], dtype=np.float64)
        qsnow = np.array([0.0004], dtype=np.float64)
        qgrau = np.array([0.0005], dtype=np.float64)

        thermo1 = Thermodynamics(
            temp1, rho, press1, qvap1, qcond1, qice, qrain, qsnow, qgrau
        )
        thermo2 = Thermodynamics(
            temp2, rho, press2, qvap2, qcond2, qice, qrain, qsnow, qgrau
        )

        microphys = MicrophysicsScheme(
            config, t_start, timestep, press1, temp1, qvap1, qcond1
        )

        microphys_wrapped = MicrophysicsSchemeWrapper(
            config_filename,
            t_start,
            timestep,
            press2,
            temp2,
            qvap2,
            qcond2,
        )

        microphys.run(timestep)  # implict change of thermo1
        thermo2 = microphys_wrapped.run(timestep, thermo2)

        assert thermo1.press == thermo2.press
        assert thermo1.temp == thermo2.temp
        for q1, q2 in zip(thermo1.massmix_ratios, thermo2.massmix_ratios):
            assert q1 == q2

    print(f"MPI version: {MPI.Get_version()}")
    config = pycleo.Config(str(config_filename))
    pycleo.pycleo_initialize(config)

    print("TEST 1: test_initialize")
    test_initialize(config_filename)
    print("------- TEST 1/4 PASSED -------")

    print("TEST 2: test_initialize_wrapper")
    test_initialize_wrapper(config_filename)
    print("------- TEST 2/4 PASSED -------")

    print("TEST 3: test_finalize_wrapper")
    test_finalize_wrapper(config_filename)
    print("------- TEST 3/4 PASSED -------")

    print("TEST 4: test_microphys_with_wrapper")
    test_microphys_with_wrapper(config_filename)
    print("------- TEST 4/4 PASSED -------")

    pycleo.pycleo_finalize()
