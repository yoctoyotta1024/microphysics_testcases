"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: perform_1dkid_model.py
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
interface called by a test to run the 1-D KiD rainshaft and then plot the results.
"""

from pathlib import Path
from .run_1dkid import run_1dkid


def perform_0dparcel_test_case(
    time_init, time_end, timestep, thermo_init, microphys_scheme, binpath, run_name
):
    """Run test case for a 1-D KiD rainshaft model.

    This function runs a 1-D KiD rainshaft model with a specified microphysics scheme and
    KiD dynamics given the initial thermodynamics. The data is then saved/plotted in the
    binpath directory using the run_name as a label.'''

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
    run_1dkid(time_init, time_end, timestep, thermo_init, microphys_scheme)
    print("--------------------------------")

    print("--- Plotting Results ---")
    assert Path(binpath).exists(), "The specified binpath does not exist."
    assert run_name, "The run_name cannot be empty."
    # TODO(CB): make plots for KiD Test Case
    print("------------------------")
