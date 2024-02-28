'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_python_microphys.py
Project: test_case_0dparcel
Created Date: Wednesday 28th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Wednesday 28th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
mock test case for adiabatic expansion of a parcel of air (0-D model)
'''

from .run_0dparcel import run_0dparcel
from libs.src_py.thermodynamics import Thermodynamics
from libs.src_py.microphysics_scheme import MicrophysicsSchemeWrapper

def test_python_microphys():
  """runs 0-D parcel model test using Python microphysics scheme (which is a mock-up of the
  muphys-cpp graupel class for ICON).

  This function sets up initial conditions and parameters for running a 0-D parcel model
  test case using the Python microphysics scheme (via a wrapper). It then runs the 0-D parcel
  model with the chosen setup.

  Test Parameters:
      Timestepping:
        time_init (float): Initial time for the simulation (s).
        time_end (float): End time for the simulation (s).
        timestep (float): Timestep for the simulation (s).
      Initial thermodynamics:
        temp (float): Initial temperature (K).
        rho (float): Initial density of moist air (kg/m3).
        press (float): Initial pressure (Pa).
        qvap (float): Initial specific water vapor content (kg/kg).
        qcond (float): Initial specific cloud water content (kg/kg).
        qice (float): Initial specific cloud ice content (kg/kg).
        qrain (float): Initial specific rain content (kg/kg).
        qsnow (float): Initial specific snow content (kg/kg).
        qgrau (float): Initial specific graupel content (kg/kg).
      Microphysics Scheme:
        nvec (int): Number of horizontal points for the microphysics scheme.
        ke (float): Number of grid points in vertical direction for the microphysics scheme.
        ivstart (int): Start index for horizontal direction for the microphysics scheme.
        dz (float): Layer thickness of full levels (m) for the microphysics scheme.
        qnc (float): Cloud number concentration.

  """

  ### timestepping
  time_init = 0.0 # [s]
  time_end = 10.0 # [s]
  timestep = 1.0 # [s]

  ### initial thermodynamic conditions
  temp = 288.15
  rho = 1.225
  press = 101325
  qvap = 0.015
  qcond = 0.0
  qice = 0.0
  qrain = 0.0
  qsnow = 0.0
  qgrau = 0.0
  thermo_init = Thermodynamics(temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau)

  ### microphysics scheme to use (within a wrapper)
  nvec = 1
  ke = 1
  ivstart = 0
  dz = 10
  qnc = 500
  microphys_scheme = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

  run_0dparcel(time_init, time_end, timestep, thermo_init, microphys_scheme)