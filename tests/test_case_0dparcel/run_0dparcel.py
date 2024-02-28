'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: run_0dparcel.py
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
'''

from .adiabatic_expansion import AdiabaticExpansion

def timestep_0dparcel(time, time_end, timestep, thermo, microphys_scheme, parcel_dynamics):

  while time <= time_end:

    thermo = parcel_dynamics.run(time, thermo)
    thermo = microphys_scheme.run(time, thermo)

  time += timestep

def run_0dparcel(time, time_end, timestep, thermo, microphys_scheme):

  ### type of dynamics parcel will undergo
  parcel_dynamics = AdiabaticExpansion()

  ### run dynamics + microphysics
  microphys_scheme.initialize()

  timestep_0dparcel(time, time_end, timestep, thermo, microphys_scheme, parcel_dynamics)

  microphys_scheme.finalize()
