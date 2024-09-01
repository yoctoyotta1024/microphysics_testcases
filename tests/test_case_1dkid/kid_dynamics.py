"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: kid_dynamics.py
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
class for driving KiD rainshaft test case
"""


class KiDDynamics:
    """A class for driving the KiD rainshaft test case, based on Shipway and Hill 2012.

    Class is wrapper around MPDATA driver of Shipway and Hill 2012 example in pyMPDATA.
    """

    def __init__(self):
        """Initialize the KiDDynamics object."""

    def run(self, time, timestep, thermo):
        """
        Run the 1-D KiD motion computations.

        This method integrates the equations from time to time+timestep for a 1-D KiD rainshaft.

        Args:
            time (float):
              Current time [s].
            timestep (float):
              Time step size for the simulation [s].
            thermo (Thermodynamics):
              Object representing the thermodynamic state of the air.

        Returns:
            Thermodynamics: Updated thermodynamic state of the air.
        """
        return thermo
