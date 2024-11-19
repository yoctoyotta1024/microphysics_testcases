"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: perform_0dparcel_test_case.py
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
interface called by a test to run the 0-D parcel and then plot the results.
"""

from pathlib import Path
import matplotlib.pyplot as plt

from .run_0dparcel import run_0dparcel
from libs.thermo import formulae
from libs.utility_functions import plot_utilities


def perform_0dparcel_test_case(
    time_init, time_end, timestep, thermo_init, microphys_scheme, binpath, run_name
):
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
    out = run_0dparcel(time_init, time_end, timestep, thermo_init, microphys_scheme)
    print("--------------------------------")

    print("--- Plotting Results ---")
    assert Path(binpath).exists(), "The specified binpath does not exist."
    assert run_name, "The run_name cannot be empty."
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

    assert Path(binpath).exists()
    assert run_name
    print("plotting " + run_name + " and saving plots in: " + str(binpath))

    fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
    figname = run_name + "_thermodynamics.png"
    axs = axs.flatten()

    time = out.time.values
    plot_utilities.plot_thermodynamics_output_timeseries(axs[0], out, "press")
    plot_utilities.plot_thermodynamics_output_timeseries(axs[1], out, "rho")
    plot_utilities.plot_thermodynamics_output_timeseries(axs[2], out, "temp")
    plot_thetas_on_axis(axs[3], time, out.temp, out.press, out.press.values[0])

    for ax in axs:
        ax.set_xlabel(out.time.name + " /" + out.time.units)

    fig.tight_layout()
    plot_utilities.save_figure(fig, binpath, figname)


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

    assert Path(binpath).exists(), "The specified binpath does not exist."
    assert run_name, "The run_name cannot be empty."
    print("plotting " + run_name + " and saving plots in: " + str(binpath))

    fig, axs = plt.subplots(nrows=2, ncols=3, sharex=True)
    figname = run_name + "_massmix_ratios.png"
    axs = axs.flatten()

    plot_utilities.plot_thermodynamics_output_timeseries(axs[0], out, "qvap")
    plot_utilities.plot_thermodynamics_output_timeseries(axs[1], out, "qcond")
    plot_utilities.plot_thermodynamics_output_timeseries(axs[2], out, "qice")
    plot_utilities.plot_thermodynamics_output_timeseries(axs[3], out, "qrain")
    plot_utilities.plot_thermodynamics_output_timeseries(axs[4], out, "qsnow")
    plot_utilities.plot_thermodynamics_output_timeseries(axs[5], out, "qgrau")

    for ax in axs:
        ax.set_xlabel(out.time.name + " /" + out.time.units)

    fig.tight_layout()
    plot_utilities.save_figure(fig, binpath, figname)


def plot_thetas_on_axis(ax, time, temp, press, press0):
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
    theta_dry = formulae.dry_potential_temperature(temp.values, press.values, press0)
    ax.plot(time, theta_dry, label="dry")
    ax.set_ylim(theta_dry[0] - 10, theta_dry[0] + 10)
    ax.legend()
    ax.set_ylabel("potential temperature /" + temp.units)
