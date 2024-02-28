'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_case_0dparcel.py
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

import matplotlib.pyplot as plt
from libs.src_py.microphysics_scheme import MicrophysicsScheme
from .adiabatic_expansion import AdiabaticExpansion

def run_0dparcel_adiabatic_expansion(time_init, time_end, timestep, thermo_init, expansion, microphys):

  time = time_init
  thermo = thermo_init
  while time <= time_end:

    thermo = microphys.run(time, thermo)
    thermo = expansion.run(time, thermo)

    time += timestep


def test_case_0dparcel():

  time_init = 0.0 # [s]
  time_end = 10.0 # [s]
  timestep = 1.0 # [s]

  temp_init = 298.15 # [K]
  press_init = 101325 # [Pa]

  thermo_init = {
    "temp": temp_init,
    "press": press_init
  }
  microphys = MicrophysicsScheme()
  expansion = AdiabaticExpansion()

  run_0dparcel_adiabatic_expansion(time_init, time_end, timestep, thermo_init, expansion, microphys)
