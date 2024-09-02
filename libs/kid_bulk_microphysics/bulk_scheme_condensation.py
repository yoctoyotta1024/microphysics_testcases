"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: bulk_scheme_condensation.py
Project: kid_bulk_microphysics
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
Simple bulk microphysics scheme to model condensation extracted from pyMPDATA
Shipway and Hill 2012 example for 1-D KiD rainshaft model
"""

import numpy as np
from ..thermo.thermodynamics import Thermodynamics
from PyMPDATA_examples import Shipway_and_Hill_2012 as kid


# TODO(CB): add documentation
class MicrophysicsSchemeWrapper:
    def __init__(self):
        """Initialize the WrappedKiDBulkMicrophysics object."""
        self.microphys = "KiDBulkMicrophysics"
        self.name = "Wrapper around " + self.microphys

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
        qvap = thermo.massmix_ratios[0]
        pvs = kid.formulae.pvs_Celsius(thermo.temp - kid.const.T0)
        relh = kid.formulae.pv(thermo.press, qvap) / pvs

        dql_cond = np.maximum(0, qvap * (1 - 1 / relh))

        thermo.massmix_ratios[0] -= dql_cond
        thermo.massmix_ratios[1] += dql_cond

        return thermo
