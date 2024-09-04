"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_bulkkid.py
Project: test_case_1dkid
Created Date: Monday 2nd September 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Wednesday 4th September 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

# %% Function definitions
import numpy as np
from pathlib import Path
from PyMPDATA_examples.Shipway_and_Hill_2012 import si

from .perform_1dkid_test_case import perform_1dkid_test_case
from libs.thermo.thermodynamics import Thermodynamics
from libs.pympdata_microphysics.bulk_scheme_condensation import (
    MicrophysicsSchemeWrapper,
)


def test_pympdata_bulk_scheme_1dkid():
    """runs test of 1-D KiD rainshaft model using bulk scheme for condensation
    extracted from pyMPDATA for the microphysics scheme.

    This function sets up initial conditions and parameters for running a 1-D KiD rainshaft
    test case using the bulk microphysics scheme for condensation from the Shipway and Hill 2012
    pyMPDATA-examples example (via a wrapper). It then runs the test case as specified.
    """
    ### label for test case to name data/plots with
    run_name = "pympdata_bulkmicrophys_1dkid"

    ### path to directory to save data/plots in after model run
    binpath = Path(__file__).parent.resolve() / "bin"  # i.e. [current directory]/bin/
    binpath.mkdir(parents=False, exist_ok=True)

    ### time and grid parameters
    z_delta = 25 * si.m
    z_max = 3200 * si.m
    timestep = 0.25 / 2 * si.s
    time_end = 15 * si.minutes

    ### initial thermodynamic conditions
    assert z_max % z_delta == 0, "z limit is not a multiple of the grid spacing."
    zeros = np.zeros(int(z_max / z_delta))
    thermo_init = Thermodynamics(
        zeros, zeros, zeros, zeros, zeros, zeros, zeros, zeros, zeros
    )

    ### microphysics scheme to use (within a wrapper)
    microphys_scheme = MicrophysicsSchemeWrapper()

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