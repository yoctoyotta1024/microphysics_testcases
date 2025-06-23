"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: microphysics_scheme_wrapper.py
Project: cleo_sdm
Created Date: Monday 23rd June 2025
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 23rd June 2025
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
wrapper function for an instance of MicrophysicsScheme so it can be used by generic test cases
and run scripts
"""

from ..thermo.thermodynamics import Thermodynamics
from cleo_sdm import CleoSDM


class MicrophysicsSchemeWrapper:
    """A class wrapping around C++ bindings to CLEO's Superdroplet Model (SDM) microphysics scheme
    (wrapper for compatibility purposes).

    This class wraps around the CLEO SDM microphysics to provide compatibility
    with the Python run scripts and tests in this project. It initializes CLEO SDM microphysics
    object and provides wrappers around methods to initialize, finalize, and run the microphysics.
    """

    def __init__(self):
        """Initialize the MicrophysicsSchemeWrapper object."""
        self.microphys = CleoSDM()  # WIP
        self.name = "Wrapper around " + self.microphys.name

    def initialize(self) -> int:
        """Initialise the microphysics scheme.

        This method calls the microphysics initialisation

        Returns:
            int: 0 upon successful initialisation
        """

        self.microphys.initialize()

        return 0

    def finalize(self) -> int:
        """Finalise the microphysics scheme.

        This method calls the microphysics finalisation.

        Returns:
            int: 0 upon successful finalisation.
        """

        self.microphys.finalize()

        return 0

    def run(self, timestep: float, thermo: Thermodynamics) -> Thermodynamics:
        """Run the microphysics computations.

        This method is a wrapper of the MicrophysicsScheme object's run function to call the
        microphysics computations in a way that's compatible with the test and scripts in this project.

        Args:
            timestep (float):
              Time-step for integration of microphysics (s)
            thermo (Thermodynamics):
              Thermodynamic properties.

        Returns:
            Thermodynamics: Updated thermodynamic properties after microphysics computations.

        """

        self.microphys.run(timestep, thermo)

        return thermo
