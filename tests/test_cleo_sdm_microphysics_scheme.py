"""
Copyright (c) 2025 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_cleo_sdm_microphysics_scheme.py
Project: tests
Created Date: Monday 23rd June 2025
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Tuesday 1st July 2025
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
unit tests for cleo_sdm microphysics module.
NOTE: tests assume CLEO's initial condition binary files already exist
    (i.e. 'dimlessGBxboundaries.dat' and 'dimlessSDsinit.dat' files, whose
    locations are given in CLEO's config file ('config_filename')
"""

import pytest
from mpi4py import MPI
import os
import sys
import numpy as np
from ruamel.yaml import YAML


@pytest.fixture(scope="module")
def path2pycleo(pytestconfig):
    return pytestconfig.getoption("cleo_path2pycleo")


@pytest.fixture(scope="module")
def config_filename(pytestconfig):
    return pytestconfig.getoption("cleo_test_generic_config_filename")


def test_mpi_is_initialised():
    print(f"MPI version: {MPI.Get_version()}")


def test_initialize(path2pycleo, config_filename):
    os.environ["PYCLEO_DIR"] = str(path2pycleo)

    from libs.cleo_sdm.cleo_sdm import CleoSDM as MicrophysicsScheme

    sys.path.append(os.environ["PYCLEO_DIR"])
    import pycleo

    yaml = YAML()
    with open(config_filename, "r") as file:
        python_config = yaml.load(file)

    t_start = 0
    timestep = python_config["timesteps"]["COUPLTSTEP"]  # [s]
    is_motion = python_config["pycleo_settings"]["is_motion"]
    press = np.array([], dtype=np.float64)
    temp = np.array([], dtype=np.float64)
    qvap = np.array([], dtype=np.float64)
    qcond = np.array([], dtype=np.float64)
    config = pycleo.Config(str(config_filename))
    pycleo.pycleo_initialize(config)
    microphys = MicrophysicsScheme(
        config, is_motion, t_start, timestep, press, temp, qvap, qcond
    )

    assert microphys.name == "CLEO SDM microphysics"


def test_initialize_wrapper(path2pycleo, config_filename):
    os.environ["PYCLEO_DIR"] = str(path2pycleo)

    from libs.cleo_sdm.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper

    sys.path.append(os.environ["PYCLEO_DIR"])

    yaml = YAML()
    with open(config_filename, "r") as file:
        python_config = yaml.load(file)

    t_start = 0
    timestep = python_config["timesteps"]["COUPLTSTEP"]  # [s]
    is_motion = python_config["pycleo_settings"]["is_motion"]
    press = np.array([], dtype=np.float64)
    temp = np.array([], dtype=np.float64)
    qvap = np.array([], dtype=np.float64)
    qcond = np.array([], dtype=np.float64)
    microphys_wrapped = MicrophysicsSchemeWrapper(
        config_filename,
        is_motion,
        t_start,
        timestep,
        press,
        temp,
        qvap,
        qcond,
    )

    assert microphys_wrapped.initialize() == 0


def test_finalize_wrapper(path2pycleo, config_filename):
    os.environ["PYCLEO_DIR"] = str(path2pycleo)

    from libs.cleo_sdm.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper

    sys.path.append(os.environ["PYCLEO_DIR"])

    yaml = YAML()
    with open(config_filename, "r") as file:
        python_config = yaml.load(file)

    t_start = 0
    timestep = python_config["timesteps"]["COUPLTSTEP"]  # [s]
    is_motion = python_config["pycleo_settings"]["is_motion"]
    press = np.array([], dtype=np.float64)
    temp = np.array([], dtype=np.float64)
    qvap = np.array([], dtype=np.float64)
    qcond = np.array([], dtype=np.float64)
    microphys_wrapped = MicrophysicsSchemeWrapper(
        config_filename,
        is_motion,
        t_start,
        timestep,
        press,
        temp,
        qvap,
        qcond,
    )

    assert microphys_wrapped.finalize() == 0


def test_microphys_with_wrapper(path2pycleo, config_filename):
    os.environ["PYCLEO_DIR"] = str(path2pycleo)

    from libs.cleo_sdm.cleo_sdm import CleoSDM as MicrophysicsScheme
    from libs.cleo_sdm.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper
    from libs.thermo.thermodynamics import Thermodynamics

    sys.path.append(os.environ["PYCLEO_DIR"])
    import pycleo

    yaml = YAML()
    with open(config_filename, "r") as file:
        python_config = yaml.load(file)

    t_start = 0
    timestep = python_config["timesteps"]["COUPLTSTEP"]  # [s]
    is_motion = python_config["pycleo_settings"]["is_motion"]
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

    config = pycleo.Config(str(config_filename))
    microphys = MicrophysicsScheme(
        config, is_motion, t_start, timestep, press1, temp1, qvap1, qcond1
    )

    microphys_wrapped = MicrophysicsSchemeWrapper(
        config_filename,
        is_motion,
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
