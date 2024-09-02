"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: plot_utilities.py
Project: utility_functions
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
Helpful functions for plotting
"""


def save_figure(fig, binpath, figname):
    """Save a Matplotlib figure as a PNG file with high resolution and tight bounding box.

    Args:
        fig (matplotlib.figure.Figure): The Matplotlib figure to be saved.
        binpath (Path): The directory where the figure will be saved.
        figname (str): The name of the PNG file to save in binpath directory.

    Returns:
        None
    """
    filename = binpath / figname
    fig.savefig(
        filename,
        dpi=400,
        bbox_inches="tight",
        facecolor="w",
        format="png",
    )
    print("Figure .png saved as: " + str(binpath) + "/" + figname)
