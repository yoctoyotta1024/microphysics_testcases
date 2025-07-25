"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_icon_satadj.py
Project: test_case_0dparcel
Created Date: Thursday 21st November
Author: Clara Bayley (CB)
Additional Contributors: Joerg Behrens, Georgiana Mania
-----
Last Modified: Wednesday 4th June 2025
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
perform test case for 0-D parcel model with python bindings to saturation adjustment from
ICON AES one-moment bulk microphysics scheme
"""

import pytest
import os
import warnings
import numpy as np

from pathlib import Path


@pytest.fixture(scope="module")
def aes_muphys_py_dir(pytestconfig):
    return pytestconfig.getoption("aes_muphys_py_dir")


@pytest.hookimpl(tryfirst=True)
def test_aes_muphys_py_dir(aes_muphys_py_dir):
    if not Path(aes_muphys_py_dir).is_dir():
        warnings.warn(
            f"No ICON AES microphysics library found. Not running {Path(__file__).name}"
        )


def test_icon_satadj_0dparcel(aes_muphys_py_dir):
    """runs 0-D parcel model test using ICON saturation adjustment as a MicrophysicsScheme
    (without AES microphysics).

    This function sets up initial conditions and parameters for running a 0-D parcel model
    test case using a wrapper around python bindings to ICON AES saturation adjustment.
    It then runs the 0-D parcel test case as specified.

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
        Microphysics Scheme:
            nvec (int): Number of horizontal points for the microphysics scheme.
            ke (float): Number of grid points in vertical direction for the microphysics scheme.
            ivstart (int): Start index for horizontal direction for the microphysics scheme.
            dz (np.ndarray): Layer thickness of full levels (m) for the microphysics scheme.
            qnc (float): Cloud number concentration.

    """
    if Path(aes_muphys_py_dir).is_dir():
        os.environ["AES_MUPHYS_PY_DIR"] = str(aes_muphys_py_dir)
        from libs.icon_satadj.microphysics_scheme_wrapper import (
            MicrophysicsSchemeWrapper,
        )
        from libs.test_case_0dparcel.perform_0dparcel_test_case import (
            perform_0dparcel_test_case,
        )
        from libs.thermo.thermodynamics import Thermodynamics

        ### label for test case to name data/plots with
        run_name = "icon_satadj_0dparcel"

        ### path to directory to save data/plots in after model run
        binpath = (
            Path(__file__).parent.resolve() / "bin"
        )  # i.e. [current directory]/bin/
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
        qice = np.array([0.0], dtype=np.float64)
        qrain = np.array([0.04], dtype=np.float64)
        qsnow = np.array([0.0], dtype=np.float64)
        qgrau = np.array([0.0], dtype=np.float64)
        wvel = uvel = vvel = np.array([])  # this microphysics test doesn't need winds

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
        nvec = 1
        ke = 1
        ivstart = 0
        dz = np.array([100], dtype=np.float64)
        qnc = 500
        microphys_scheme = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

        ### Perform 0-D parcel model test case using chosen setup
        perform_0dparcel_test_case(
            time_init,
            time_end,
            timestep,
            thermo_init,
            microphys_scheme,
            binpath,
            run_name,
        )
