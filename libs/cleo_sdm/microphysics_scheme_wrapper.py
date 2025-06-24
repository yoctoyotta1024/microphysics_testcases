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
wrapper function for an instance of CleoSDM microphysics ccheme so it can be used by
generic test cases and run scripts
"""

import os
import sys

from .cleo_sdm import CleoSDM
from ..thermo.thermodynamics import Thermodynamics

sys.path.append(os.environ["PYCLEO_DIR"])  # TODO(ALL): receive as argument to class?
# currently on Levante, do:
# export PYCLEO_DIR=/home/m/m300950/microphysics_testcases/build/_deps/cleo-build/pycleo/
import pycleo


class MicrophysicsSchemeWrapper:
    """A class wrapping around C++ bindings to CLEO's Superdroplet Model (SDM) microphysics scheme
    (wrapper for compatibility purposes).

    This class wraps around the CLEO SDM microphysics to provide compatibility
    with the Python run scripts and tests in this project. It initializes CLEO SDM microphysics
    object and provides wrappers around methods to initialize, finalize, and run the microphysics.
    """

    def __init__(
        self,
        config_filename,
        t_start,
        timestep,
        press,
        temp,
        qvap,
        qcond,
        no_init=True,
        no_final=True,
    ):
        """Initialize the MicrophysicsSchemeWrapper object."""
        config = pycleo.Config(str(config_filename))
        if not no_init:
            # TODO(CB): fix multiple kokkos initialise error -> remove option not to initialise?
            pycleo.pycleo_initialize(config)

        self.microphys = CleoSDM(config, t_start, timestep, press, temp, qvap, qcond)
        self.name = "Wrapper around " + self.microphys.name

        self.pycleo_finalize = lambda: None
        if not no_final:
            # TODO(CB): fix multiple kokkos initialise error -> remove option not to finalize?
            self.pycleo_finalize = pycleo.pycleo_finalize

    def initialize(self) -> int:
        """Initialise the microphysics scheme.

        This method calls the microphysics initialisation

        Returns:
            int: 0 upon successful initialisation
        """

        return 0

    def finalize(self) -> int:
        """Finalise the microphysics scheme.

        This method calls the microphysics finalisation.

        Returns:
            int: 0 upon successful finalisation.
        """

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

        self.microphys.run(timestep)

        return thermo

    def __del__(self):
        self.microphys = None  # destroys CleoSDM member
        self.pycleo_finalize()
