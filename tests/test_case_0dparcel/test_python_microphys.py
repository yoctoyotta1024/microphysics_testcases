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

from .case_0dparcel import run_case_0dparcel
from libs.src_py.thermodynamics import Thermodynamics
from libs.src_py.microphysics_scheme import MicrophysicsSchemeWrapper

def test_python_microphys():

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

  run_case_0dparcel(time_init, time_end, timestep, thermo_init, microphys_scheme)
