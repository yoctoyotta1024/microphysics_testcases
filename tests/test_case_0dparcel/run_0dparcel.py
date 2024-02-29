'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: run_0dparcel.py
Project: test_case_0dparcel
Created Date: Wednesday 28th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Thursday 29th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
'''

from .adiabatic_motion import AdiabaticMotion

def run_0dparcel(time, time_end, timestep, thermo, microphys_scheme):
  """Run a 0-D parcel model with a specified microphysics scheme and parcel dynamics.

  This function runs a 0-D parcel model with the given initial thermodynamic conditions, and
  microphysics scheme from time to time_end with a constant timestep using some set parcel
  dynamics.

  Parameters:
      time (float): Initial time for the simulation (s).
      time_end (float): End time for the simulation (s).
      timestep (float): Timestep for the simulation (s).
      thermo (Thermodynamics): Initial thermodynamic conditions.
      microphys_scheme: Microphysics scheme to use.

  """

  ### type of dynamics parcel will undergo
  parcel_dynamics = AdiabaticMotion()

  ### run dynamics + microphysics from time to time_end
  microphys_scheme.initialize()

  while time <= time_end:

    thermo = parcel_dynamics.run(timestep, thermo)
    thermo = microphys_scheme.run(timestep, thermo)
    time += timestep

  microphys_scheme.finalize()
