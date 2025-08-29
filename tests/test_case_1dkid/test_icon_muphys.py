"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_bulkkid.py
Project: test_case_1dkid
Created Date: Monday 2nd September 2024
Author: Clara Bayley (CB)
Additional Contributors: Joerg Behrens, Georgiana Mania
-----
Last Modified: Wednesday 4th June 2025
Modified By: Joerg Behrens, Georgiana Mania
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

import pytest
import numpy as np
import os
import warnings

from pathlib import Path
from PyMPDATA_examples.Shipway_and_Hill_2012 import si


@pytest.fixture(scope="module")
def aes_muphys_py_dir(pytestconfig):
    return pytestconfig.getoption("aes_muphys_py_dir")


@pytest.hookimpl(tryfirst=True)
def test_aes_muphys_py_dir(aes_muphys_py_dir):
    if not Path(aes_muphys_py_dir).is_dir():
        warnings.warn(
            f"No ICON AES microphysics library found. Not running {Path(__file__).name}"
        )


def test_icon_muphys_1dkid(aes_muphys_py_dir):
    """runs test of 1-D KiD rainshaft model using ICON AES one-moment bulk scheme for
    the microphysics.

    This function sets up initial conditions and parameters for running a 1-D KiD rainshaft
    test case using ICON AES one-moment bulk microphysics scheme (with python bindings and
    via a wrapper). It then runs the test case as specified.
    """
    if Path(aes_muphys_py_dir).is_dir():
        os.environ["AES_MUPHYS_PY_DIR"] = str(aes_muphys_py_dir)
        from libs.test_case_1dkid.perform_1dkid_test_case import perform_1dkid_test_case
        from libs.thermo.thermodynamics import Thermodynamics
        from libs.icon_muphys.microphysics_scheme_wrapper import (
            MicrophysicsSchemeWrapper,
        )

        ### label for test case to name data/plots with
        run_name = "icon_muphys_1dkid"

        ### path to directory to save data/plots in after model run
        binpath = (
            Path(__file__).parent.resolve() / "bin"
        )  # i.e. [current directory]/bin/
        binpath.mkdir(parents=False, exist_ok=True)

        ### time and grid parameters
        z_delta = 25 * si.m
        z_max = 3200 * si.m
        timestep = 1.25 * si.s
        time_end = 15 * si.minutes

        ### initial thermodynamic conditions
        assert z_max % z_delta == 0, "z limit is not a multiple of the grid spacing."
        zeros = np.zeros(int(z_max / z_delta))
        null = np.array([])  # this microphysics test doesn't need winds
        thermo_init = Thermodynamics(
            zeros,
            zeros,
            zeros,
            zeros,
            zeros,
            zeros,
            zeros,
            zeros,
            zeros,
            null,
            null,
            null,
        )

        ### microphysics scheme to use (within a wrapper)
        nvec = 1
        ke = 128
        ivstart = 0
        dz = np.empty(ke, dtype=np.float64)
        dz.fill(25)
        qnc = 500
        lrain = True
        microphys_scheme = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc, lrain)

        ### Perform test of 1-D KiD rainshaft model using chosen setup
        advect_hydrometeors = True
        perform_1dkid_test_case(
            z_delta,
            z_max,
            time_end,
            timestep,
            thermo_init,
            microphys_scheme,
            advect_hydrometeors,
            binpath,
            run_name,
        )
