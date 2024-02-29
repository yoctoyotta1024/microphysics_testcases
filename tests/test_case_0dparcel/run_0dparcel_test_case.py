'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: run_0dparcel_test_case.py
Project: test_case_0dparcel
Created Date: Wednesday 28th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Friday 1st March 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
'''

from pathlib import Path
import matplotlib.pyplot as plt

from .run_0dparcel_model import run_0dparcel_model
from libs.src_py import thermo_equations as eqns

def run_0dparcel_test_case(time_init, time_end, timestep, thermo_init, microphys_scheme,
                           binpath, run_name):
  """Run test case for a 0-D parcel model.

  This function runs a 0-D parcel model with a specified microphysics scheme and parcel dynamics
  given the initial thermodynamics. The data is then saved/plotted in the binpath directory
  using the run_name as a label.'''

  Args:
      time_init (float):
        Initial time for the simulation (s).
      time_end (float):
        End time for the simulation (s).
      timestep (float):
        Timestep for the simulation (s).
      thermo_init (Thermodynamics):
        Initial thermodynamic conditions.
      microphys_scheme:
        Microphysics scheme to use in test run.
      binpath (str):
        Path to the directory where data/plots will be saved.
      run_name (str):
        Name of the test run (used for labeling output).

  Raises:
      AssertionError: If the specified binpath does not exist or if run_name is empty.

  Returns:
      None
  """

  print("\n--- Running 0-D Parcel Model ---")
  out = run_0dparcel_model(time_init, time_end, timestep, thermo_init, microphys_scheme)
  print("--------------------------------")

  print("--- Plotting Results ---")
  assert(Path(binpath).exists()), "The specified binpath does not exist."
  assert(run_name), "The run_name cannot be empty."
  plot_0dparcel_thermodynamics(out, binpath, run_name)
  plot_0dparcel_massmix_ratios(out, binpath, run_name)
  print("------------------------")

def plot_0dparcel_thermodynamics(out, binpath, run_name):
  """Plot thermodynamic variables for a 0-D parcel model and save the plots.

  This function plots the pressure, density, temperature, and potential temperature(s)
  of a run of the 0-D parcel model as a function of time and then saves the plots as a PNG image.

  Args:
      out (OutputThermodynamics):
        OutputThermodynamics object containing the thermodynamic data.
      binpath (str):
        Path to the directory where the plots will be saved.
      run_name (str):
        Name of the test run to use in naming saved image.

  Raises:
      AssertionError: If the specified binpath does not exist or if run_name is empty.

  Returns:
      None
  """

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

def plot_0dparcel_massmix_ratios(out, binpath, run_name):
  """Plot mass mixing ratios for a 0-D parcel model and save the plots.

  This function plots the mass mixing ratios of water vapor, cloud liquid, cloud ice,
  rain, snow, and graupel for a run of the 0-D parcel model as a function of time and then
  saves the plots as a PNG image.

  Args:
      out (OutputThermodynamics):
        OutputThermodynamics object containing the mass mixing ratio data.
      binpath (str):
        Path to the directory where the plots will be saved.
      run_name (str):
        Name of the test run to use in naming saved image.

  Raises:
      AssertionError: If the specified binpath does not exist or if run_name is empty.

  Returns:
      None
  """

  assert(Path(binpath).exists()), "The specified binpath does not exist."
  assert(run_name), "The run_name cannot be empty."
  print("plotting "+run_name+" and saving plots in: "+binpath)

  fig, axs = plt.subplots(nrows=2, ncols=3, sharex=True)
  figname = run_name+"_massmix_ratios.png"
  axs = axs.flatten()

  time = out.time.values
  plot_variable_on_axis(axs[0], time, out.qvap)
  plot_variable_on_axis(axs[1], time, out.qcond)
  plot_variable_on_axis(axs[2], time, out.qice)
  plot_variable_on_axis(axs[3], time, out.qrain)
  plot_variable_on_axis(axs[4], time, out.qsnow)
  plot_variable_on_axis(axs[5], time, out.qgrau)

  for ax in axs:
    ax.set_xlabel(out.time.name+" /"+out.time.units)

  fig.tight_layout()
  save_figure(fig, binpath, figname)


def plot_variable_on_axis(ax, time, var):
  """Plot a variable against time on an axis.

  Args:
      ax (matplotlib.axes.Axes): The (x-y) axis on which to plot the variable.
      time (array-like): Time values (x axis).
      var (OutputVariable): The variable to be plotted (y axis).

  Returns:
      None
  """
  ax.plot(time, var.values)
  ax.set_ylabel(var.name+" /"+var.units)

def plot_thetas_on_axis(ax, time, temp, press):
  """Plot potential temperature(s) on a specified axis.

  This function calculates and plots potential temperature(s) against time on a specified axis.

  Args:
      ax (matplotlib.axes.Axes): The (x-y) axis on which to plot the potential temperature(s).
      time (array-like): Time values (x axis).
      temp (OutputVariable): Temperature variable.
      press (OutputVariable): Pressure variable.

  Returns:
      None
  """
  theta_dry = eqns.dry_potential_temperature(temp.values, press.values)
  ax.plot(time, theta_dry, label="dry")
  ax.legend()
  ax.set_ylabel("potential temperature /"+temp.units)

def save_figure(fig, binpath, figname):
  """Save a Matplotlib figure as a PNG file with high resolution and tight bounding box.

  Args:
      fig (matplotlib.figure.Figure): The Matplotlib figure to be saved.
      binpath (str): The directory where the figure will be saved.
      figname (str): The name of the PNG file to save in binpath directory.

  Returns:
      None
  """
  fig.savefig(binpath+"/"+figname,dpi=400, bbox_inches="tight", facecolor='w', format="png")
  print("Figure .png saved as: "+binpath+"/"+figname)
