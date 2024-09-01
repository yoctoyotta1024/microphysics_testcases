"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: run_1dkid.py
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
run 1-D KiD rainshaft model by timestepping and outputting data
"""

from .kid_dynamics import KiDDynamics
from libs.src_mock_py.output_thermodynamics import OutputThermodynamics


def run_1dkid(time, time_end, timestep, thermo, microphys_scheme):
    """Run 1-D KiD rainshaft model with a specified microphysics scheme and KiD dynamics.

    This function runs a 1-D KiD rainshaft model with the given initial thermodynamic conditions,
    and microphysics scheme from time to time_end with a constant timestep based on the
    PyMPDATA Shipway and Hill 2012 example for the KiD dynamics.

    Parameters:
        time (float):
          Initial time for the simulation (s).
        time_end (float):
          End time for the simulation (s).
        timestep (float):
          Timestep for the simulation (s).
        thermo (Thermodynamics):
          Initial thermodynamic conditions.
        microphys_scheme:
          Microphysics scheme to use.

    Returns:
          OutputThermodynamics: Output containing thermodynamic data from the model run.
    """

    ### data to output during model run
    out = OutputThermodynamics()

    # ### type of dynamics rainshaft will undergo
    parcel_dynamics = KiDDynamics()

    ### run dynamics + microphysics from time to time_end
    microphys_scheme.initialize()

    out.output_thermodynamics(time, thermo)
    while time <= time_end:
        thermo = parcel_dynamics.run(time, timestep, thermo)
        thermo = microphys_scheme.run(timestep, thermo)

        out.output_thermodynamics(time, thermo)

        time += timestep

    microphys_scheme.finalize()

    out.finalize()
    return out
