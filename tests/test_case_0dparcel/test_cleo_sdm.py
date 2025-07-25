"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_cleo_sdm.py
Project: test_case_0dparcel
Created Date: Tuesday 24th June 2025
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
perform test case for 0-D parcel model with CLEO Superdroplet Model (SDM) microphysics scheme
"""

import pytest
import numpy as np
from pathlib import Path


@pytest.fixture(scope="module")
def path2pycleo(pytestconfig):
    return pytestconfig.getoption("cleo_path2pycleo")


@pytest.fixture(scope="module")
def config_filename(pytestconfig):
    return pytestconfig.getoption("cleo_test_0dparcel_config_filename")


def test_cleo_sdm_0dparcel(path2pycleo, config_filename):
    """runs 0-D parcel model test using CLEO SDM microphysics scheme

    NOTE: test assumes CLEO's initial condition binary files already exist
    (i.e. 'dimlessGBxboundaries.dat' and 'dimlessSDsinit.dat' files, whose
    locations are given in CLEO's config file ('config_filename')

    This function sets up initial conditions and parameters for running a 0-D parcel model
    test case using the CLEO SDM microphysics scheme (via a wrapper and assuming CLEO's
    initial condition files have already been made). It then runs the
    0-D parcel test case as specified.

    Test Parameters:
        Timestepping:
          time_init (float): Initial time for the simulation (s).
          time_end (float): End time for the simulation (s).
          timestep (float): Timestep for the simulation (s).
        Initial thermodynamics:
          temp (np.ndarray): Initial temperature (K).
          rho (np.ndarray): Initial density of moist air (kg/m3).
          press (np.ndarray): Initial pressure (Pa).
          qvap (np.ndarray): Initial specific water vapor content (kg/kg).
          qcond (np.ndarray): Initial specific cloud water content (kg/kg).
          qice (np.ndarray): Initial specific cloud ice content (kg/kg).
          qrain (np.ndarray): Initial specific rain content (kg/kg).
          qsnow (np.ndarray): Initial specific snow content (kg/kg).
          qgrau (np.ndarray): Initial specific graupel content (kg/kg).

    """
    import os

    os.environ["PYCLEO_DIR"] = str(path2pycleo)

    from libs.test_case_0dparcel.perform_0dparcel_test_case import (
        perform_0dparcel_test_case,
    )
    from libs.thermo.thermodynamics import Thermodynamics
    from libs.cleo_sdm.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper

    ### label for test case to name data/plots with
    run_name = "cleo_sdm_0dparcel"

    ### path to directory to save data/plots in after model run
    binpath = Path(__file__).parent.resolve() / "bin"  # i.e. [current directory]/bin/
    binpath.mkdir(parents=False, exist_ok=True)

    ### time parameters
    time_init = 0.0  # [s]
    time_end = 240.0  # [s]
    timestep = 1.0  # [s]

    ### initial thermodynamic conditions
    temp = np.array([288.15], dtype=np.float64)
    rho = np.array([1.225], dtype=np.float64)
    press = np.array([101325], dtype=np.float64)
    qvap = np.array([0.01], dtype=np.float64)
    qcond = np.array([0.02], dtype=np.float64)
    qice = np.array([0.03], dtype=np.float64)
    qrain = np.array([0.04], dtype=np.float64)
    qsnow = np.array([0.05], dtype=np.float64)
    qgrau = np.array([0.06], dtype=np.float64)
    wvel = np.array([0.0, 0.0], dtype=np.float64)
    uvel = np.array([0.0, 0.0], dtype=np.float64)
    vvel = np.array([0.0, 0.0], dtype=np.float64)
    thermo_init = Thermodynamics(
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

    ### microphysics scheme to use (within a wrapper)
    is_motion = False
    microphys_scheme = MicrophysicsSchemeWrapper(
        config_filename,
        is_motion,
        time_init,
        timestep,
        thermo_init.press,
        thermo_init.temp,
        thermo_init.massmix_ratios["qvap"],
        thermo_init.massmix_ratios["qcond"],
        thermo_init.wvel,
        thermo_init.uvel,
        thermo_init.vvel,
    )

    ### Perform 0-D parcel model test case using chosen setup
    perform_0dparcel_test_case(
        time_init, time_end, timestep, thermo_init, microphys_scheme, binpath, run_name
    )
