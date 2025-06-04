"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_bulkkid.py
Project: test_case_1dkid
Created Date: Monday 2nd September 2024
Author: Clara Bayley (CB)
Additional Contributors: Joerg Behrens, Georgiana Mania
-----
Last Modified: Thursday 21st November 2024
Modified By: Joerg Behrens, Georgiana Mania
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

# %% Function definitions
import numpy as np
import os

path = os.environ.get("AES_MUPHYS_PY_DIR")
if path and path is not None:
    from pathlib import Path
    from PyMPDATA_examples.Shipway_and_Hill_2012 import si

    from .perform_1dkid_test_case import perform_1dkid_test_case
    from libs.thermo.thermodynamics import Thermodynamics
    from libs.icon_graupel.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper

    def test_icon_graupel_1dkid():
        """runs test of 1-D KiD rainshaft model using ICON's one-moment "graupel"
        bulk scheme for the microphysics.

        This function sets up initial conditions and parameters for running a 1-D KiD rainshaft
        test case using ICON's one-moment bulk microphysics scheme (with python bindings and
        via a wrapper). It then runs the test case as specified.
        """
        ### label for test case to name data/plots with
        run_name = "icon_graupel_1dkid"

        ### path to directory to save data/plots in after model run
        binpath = (
            Path(__file__).parent.resolve() / "bin"
        )  # i.e. [current directory]/bin/
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
        nvec = 1
        ke = 128
        ivstart = 0
        dz = np.array([25], dtype=np.float64)
        qnc = 500

        ### Call graupel
        microphys_scheme = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

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
