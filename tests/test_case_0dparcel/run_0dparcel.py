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


import matplotlib.pyplot as plt
from .adiabatic_motion import AdiabaticMotion
from libs.src_py.output_thermodynamics import OutputThermodynamics

def run_0dparcel_model(time, time_end, timestep, thermo, microphys_scheme):
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

  ### data to output during model run
  out = OutputThermodynamics()

  ### type of dynamics parcel will undergo
  amp = 10000 # amplitude of pressure sinusoid [Pa]
  tau = 10 # time period of pressure sinusiod [s]
  parcel_dynamics = AdiabaticMotion(amp, tau)

  ### run dynamics + microphysics from time to time_end
  microphys_scheme.initialize()

  out.output_thermodynamics(thermo)
  while time <= time_end:

    thermo = parcel_dynamics.run(time, timestep, thermo)
    thermo = microphys_scheme.run(timestep, thermo)

    out.output_thermodynamics(thermo)

    time += timestep

  microphys_scheme.finalize()

  return out

def run_0dparcel_test_case(time_init, time_end, timestep, thermo_init, microphys_scheme, savedir):

  output = run_0dparcel_model(time_init, time_end, timestep, thermo_init, microphys_scheme)

  print(output.temp.value)
  print(output.rho.value)
  print(output.press.value)
  print(output.qvap.value)
  print(output.qcond.value)
  print(output.qice.value)
  print(output.qrain.value)
  print(output.qsnow.value)
  print(output.qgrau.value)
