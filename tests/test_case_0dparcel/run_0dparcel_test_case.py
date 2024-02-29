'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: run_0dparcel_test_case.py
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

from pathlib import Path
import matplotlib.pyplot as plt

from .adiabatic_motion import AdiabaticMotion
from libs.src_py.output_thermodynamics import OutputThermodynamics

def run_0dparcel_test_case(time_init, time_end, timestep, thermo_init, microphys_scheme,
                           binpath, run_name):
  '''Run a 0-D parcel model with a specified microphysics scheme and parcel dynamics.
  Then save/plot data from model provided path to bin exists.'''

  print("\n--- Running 0-D Parcel Model ---")
  output = run_0dparcel_model(time_init, time_end, timestep, thermo_init, microphys_scheme)
  print("--------------------------------")

  print("--- Plotting Results ---")
  assert(Path(binpath).exists())
  assert(run_name)
  plot_0dparcel_thermodynamics(output, binpath, run_name)
  print("------------------------")

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
  tau = 60 # time period of pressure sinusiod [s]
  parcel_dynamics = AdiabaticMotion(amp, tau)

  ### run dynamics + microphysics from time to time_end
  microphys_scheme.initialize()

  out.output_thermodynamics(time, thermo)
  while time <= time_end:

    thermo = parcel_dynamics.run(time, timestep, thermo)
    thermo = microphys_scheme.run(timestep, thermo)

    out.output_thermodynamics(time, thermo)

    time += timestep

  microphys_scheme.finalize()

  return out.finalize()

def plot_0dparcel_thermodynamics(out, binpath, run_name):

  assert(Path(binpath).exists())
  assert(run_name)
  print("plotting "+run_name+" and saving plots in: "+binpath)

  fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
  figname = run_name+"_thermodynamics.png"
  axs = axs.flatten()

  time = out.time.values
  plot_variable_on_axis(axs[0], time, out.press)
  plot_variable_on_axis(axs[1], time, out.rho)
  plot_variable_on_axis(axs[2], time, out.temp)
  plot_thetas_on_axis(axs[3], time, out.temp, out.press)

  for ax in axs:
    ax.set_xlabel(out.time.name+" /"+out.time.units)

  fig.tight_layout()
  save_figure(fig, binpath, figname)

def plot_variable_on_axis(ax, time, var):

  ax.plot(time, var.values)
  ax.set_ylabel(var.name+" /"+var.units)

def plot_thetas_on_axis(ax, time, temp, press):

  theta_dry = dry_potential_temperature(temp.values, press.values)
  ax.plot(time, theta_dry, label="dry")
  ax.legend()
  ax.set_ylabel("potential temperature /"+temp.units)

def dry_potential_temperature(temp, press):

  rgas_univ = 8.314462618   # universal molar gas constant [J/Kg/K]
  mr_dry = 0.028966216      # molecular mass of dry air [Kg/mol]
  cp_dry = 1004.64     # specific heat capacity of water vapour [J/Kg/K] (IAPWS97 at 273.15K)
  rgas_dry = rgas_univ / mr_dry   # specific gas constant for dry air [J/Kg/K] (approx. 287 J/Kg/K)

  theta_dry = temp * (press[0] / press) ** (rgas_dry / cp_dry)

  return theta_dry

def save_figure(fig, binpath, figname):

  fig.savefig(binpath+"/"+figname,dpi=400, bbox_inches="tight", facecolor='w', format="png")
  print("Figure .png saved as: "+binpath+"/"+figname)
