'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_case_0dparcel.py
Project: tests
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


from libs.src_py.microphysics_scheme import MicrophysicsScheme

def run_0dparcel_adiabatic_expansion(time_init, time_end, time_microphys, temp0, press0, microphys):

  assert 1+1 == 2

def test_case_0dparcel():

  time_init = 0.0 # [s]
  time_end = 10.0 # [s]
  time_microphys = 1.0 # [s]

  temp0 = 298.15 # [K]
  press0 = 101325 # [Pa]

  microphys = MicrophysicsScheme()

  run_0dparcel_adiabatic_expansion(time_init, time_end, time_microphys, temp0, press0, microphys)
