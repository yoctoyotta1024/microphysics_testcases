"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: perform_1dkid_test_case.py
Project: test_case_1dkid
Created Date: Monday 2nd September 2024
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
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from .run_1dkid import run_1dkid
from libs.utility_functions import plot_utilities
from libs.thermo import formulae


def perform_1dkid_test_case(
    z_delta, z_max, time_end, timestep, thermo_init, microphys_scheme, binpath, run_name
):
    """Run test case for a 1-D KiD rainshaft model.

    This function runs a 1-D KiD rainshaft model with a specified microphysics scheme and
    KiD dynamics given the initial thermodynamics. The data is then saved/plotted in the
    binpath directory using the run_name as a label.'''

    Args:
        z_delta (float):
          Grid spacing od 1-D column (m).
        z_max (float):
          Upper limit of 1-D column (m).
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

    print("\n--- Running 1-D KiD Rainshaft Model ---")
    out = run_1dkid(z_delta, z_max, time_end, timestep, thermo_init, microphys_scheme)
    print("--------------------------------")

    print("--- Plotting Results ---")
    assert Path(binpath).exists(), "The specified binpath does not exist."
    assert run_name, "The run_name cannot be empty."
    plot_1dkid_moisture(out, z_delta, z_max, binpath, run_name)
    print("------------------------")


def plot_1dkid_moisture(out, z_delta, z_max, binpath, run_name):
    assert Path(binpath).exists()
    assert run_name
    print("plotting " + run_name + " and saving plots in: " + str(binpath))

    fig, axs = plt.subplots(
        nrows=3, ncols=2, sharey=True, figsize=(9, 16), width_ratios=[3, 1]
    )
    figname = run_name + "_moisture.png"

    # %% plot results
    label = f"{out.qvap.name} [g/kg]"
    plot_kid_result(
        fig,
        axs[0, 0],
        axs[0, 1],
        out.qvap.values,
        out.time.values,
        z_delta,
        z_max,
        label,
        mult=1e-3,
        threshold=1e-3,
        cmap="grey",
    )

    label = f"{out.qcond.name} [g/kg]"
    plot_kid_result(
        fig,
        axs[1, 0],
        axs[1, 1],
        out.qcond.values,
        out.time.values,
        z_delta,
        z_max,
        label,
        mult=1e-3,
        threshold=1e-3,
        cmap="grey",
    )

    supersat = formulae.supersaturation(
        out.temp.values, out.press.values, out.qvap.values
    )
    label = "supersaturation"
    plot_kid_result(
        fig,
        axs[2, 0],
        axs[2, 1],
        supersat,
        out.time.values,
        z_delta,
        z_max,
        label,
        threshold=1e-3,
        cmap="grey",
    )

    fig.tight_layout()
    plot_utilities.save_figure(fig, binpath, figname)


def plot_kid_result(
    fig,
    ax0,
    ax1,
    var,
    time,
    z_delta,
    z_max,
    label,
    mult=1.0,
    threshold=None,
    rng=None,
    cmap="copper",
    rasterized=False,
):
    """function extracted from pyMPDATA plot.py script in
    Shipway and Hill 2012 example for 1-D KiD rainshaft.
    (see https://github.com/open-atmos/PyMPDATA/blob/main/examples/PyMPDATA_examples/Shipway_and_Hill_2012/plot.py)
    """
    lines = {3: ":", 6: "--", 9: "-", 12: "-."}
    colors = {3: "crimson", 6: "orange", 9: "navy", 12: "green"}
    fctr = 50

    coarse_dt = (time[1] - time[0]) * fctr
    tgrid = np.concatenate(((time[0] - coarse_dt / 2,), time[0::fctr] + coarse_dt / 2))
    tgrid = tgrid / 60  # [minutes]

    assert z_max % z_delta == 0, "z limit is not a multiple of the grid spacing."
    nz = int(z_max / z_delta)
    zgrid = np.linspace(0, z_max, nz + 1, endpoint=True)
    zgrid = zgrid / 1000  # [km]

    var = var * mult
    time_steps = var.shape[0] - 1
    assert (
        time_steps % fctr == 0
    ), "number of timesteps must be divisible by coarsening factor"

    # coarsen temporal part by 'fctr' transpose var for plotting
    tmp = var[1:, :]
    tmp = tmp.reshape(-1, fctr, tmp.shape[1])
    tmp = tmp.mean(axis=1)
    tmp = np.concatenate(((var[0, :],), tmp)).T

    if threshold is not None:
        var[var < threshold] = np.nan
    mesh = ax0.pcolormesh(
        tgrid,
        zgrid,
        tmp,
        cmap=cmap,
        rasterized=rasterized,
        vmin=None if rng is None else rng[0],
        vmax=None if rng is None else rng[1],
    )

    ax0.set_xlabel("time / min")
    ax0.set_xticks(list(lines.keys()))
    ax0.set_ylabel("z / km")
    ax0.grid()

    cbar = fig.colorbar(mesh, ax=ax0, shrink=0.8, location="top")
    cbar.set_label(label)

    ax1.set_xlabel(label)
    ax1.grid()
    if rng is not None:
        ax1.set_xlim(rng)

    last_t = -1
    for i, t in enumerate(time):
        t = t / 60  # [minutes]
        d = var[i, :] * mult
        z = (zgrid[1:] + zgrid[:-1]) / 2
        params = {"color": "black"}
        for line_t, line_s in lines.items():
            if last_t < line_t <= t:
                params["ls"] = line_s
                params["color"] = colors[line_t]
                ax1.step(d, z, where="mid", **params)
                ax0.axvline(t, **params)
        last_t = t
