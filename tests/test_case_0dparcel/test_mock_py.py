"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_mock_py.py
Project: test_case_0dparcel
Created Date: Wednesday 28th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 2nd September 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
perform test case for 0-D parcel model with mock python microphysics scheme
"""

from pathlib import Path

from .perform_0dparcel_test_case import perform_0dparcel_test_case
from libs.src_mock_py.thermodynamics import Thermodynamics
from libs.src_mock_py.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper


def test_mock_py_0dparcel():
    """runs 0-D parcel model test using Python mock microphysics scheme (a mock-up of the muphys-cpp
    graupel class for ICON).

    This function sets up initial conditions and parameters for running a 0-D parcel model
    test case using the Python mock microphysics scheme (via a wrapper). It then runs the
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
        Microphysics Scheme:
          nvec (int): Number of horizontal points for the microphysics scheme.
          ke (float): Number of grid points in vertical direction for the microphysics scheme.
          ivstart (int): Start index for horizontal direction for the microphysics scheme.
          dz (float): Layer thickness of full levels (m) for the microphysics scheme.
          qnc (float): Cloud number concentration.

    """

    ### label for test case to name data/plots with
    run_name = "python_microphys_0dparcel"

    ### path to directory to save data/plots in after model run
    binpath = Path(__file__).parent.resolve() / "bin"  # i.e. [current directory]/bin/
    binpath.mkdir(parents=False, exist_ok=True)

    ### time parameters
    time_init = 0.0  # [s]
    time_end = 240.0  # [s]
    timestep = 1.0  # [s]

    ### initial thermodynamic conditions
    temp = 288.15
    rho = 1.225
    press = 101325
    qvap = 0.01
    qcond = 0.02
    qice = 0.03
    qrain = 0.04
    qsnow = 0.05
    qgrau = 0.06
    thermo_init = Thermodynamics(
        temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau
    )

    ### microphysics scheme to use (within a wrapper)
    nvec = 1
    ke = 1
    ivstart = 0
    dz = 10
    qnc = 500
    microphys_scheme = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

    ### Perform 0-D parcel model test case using chosen setup
    perform_0dparcel_test_case(
        time_init, time_end, timestep, thermo_init, microphys_scheme, binpath, run_name
    )
