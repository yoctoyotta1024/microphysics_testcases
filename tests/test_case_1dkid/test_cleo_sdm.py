"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_cleo_sdm.py
Project: test_case_1dkid
Created Date: Friday 27th June 2025
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
"""

import pytest
import numpy as np
from pathlib import Path
from PyMPDATA_examples.Shipway_and_Hill_2012 import si


@pytest.fixture(scope="module")
def path2pycleo(pytestconfig):
    return pytestconfig.getoption("cleo_path2pycleo")


@pytest.fixture(scope="module")
def config_filename(pytestconfig):
    return pytestconfig.getoption("cleo_test_1dkid_config_filename")


def test_cleo_sdm_1dkid(path2pycleo, config_filename):
    """runs test of 1-D KiD rainshaft model using CLEO SDM for the
    microphysics scheme.

     NOTE: test assumes CLEO's initial condition binary files already exist
    (i.e. 'dimlessGBxboundaries.dat' and 'dimlessSDsinit.dat' files, whose
    locations are given in CLEO's config file ('config_filename')

    This function sets up initial conditions and parameters for running a 1-D KiD rainshaft
    test case using the CLEO SDM microphysics scheme (via a wrapper).
    It then runs the test case as specified.
    """
    import os

    os.environ["PYCLEO_DIR"] = str(path2pycleo)

    from libs.test_case_1dkid.perform_1dkid_test_case import perform_1dkid_test_case
    from libs.thermo.thermodynamics import Thermodynamics
    from libs.cleo_sdm.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper

    ### label for test case to name data/plots with
    run_name = "cleo_sdm_1dkid"

    ### path to directory to save data/plots in after model run
    binpath = Path(__file__).parent.resolve() / "bin"  # i.e. [current directory]/bin/
    binpath.mkdir(parents=False, exist_ok=True)

    ### time and grid parameters
    # NOTE: these must be consistent with CLEO initial condition binary files(!)
    z_delta = 25 * si.m  # (!) must be consistent with CLEO
    z_max = 3200 * si.m  # (!) must be consistent with CLEO
    timestep = 1.25 * si.s
    time_end = 15 * si.minutes

    ### initial thermodynamic conditions
    assert z_max % z_delta == 0, "z limit is not a multiple of the grid spacing."
    zeros = np.zeros(int(z_max / z_delta))
    thermo_init = Thermodynamics(
        zeros, zeros, zeros, zeros, zeros, zeros, zeros, zeros, zeros
    )

    ### microphysics scheme to use (within a wrapper)
    is_motion = True
    microphys_scheme = MicrophysicsSchemeWrapper(
        config_filename,
        is_motion,
        0.0,
        timestep,
        thermo_init.press,
        thermo_init.temp,
        thermo_init.massmix_ratios["qvap"],
        thermo_init.massmix_ratios["qcond"],
    )

    ### Perform test of 1-D KiD rainshaft model using chosen setup
    perform_1dkid_test_case(
        z_delta,
        z_max,
        time_end,
        timestep,
        thermo_init,
        microphys_scheme,
        binpath,
        run_name,
    )
