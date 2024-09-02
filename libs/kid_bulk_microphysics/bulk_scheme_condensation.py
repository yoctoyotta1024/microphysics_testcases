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
Simple bulk microphysics scheme extracted from pyMPDATA
Shipway and Hill 2012 example for 1-D KiD rainshaft model
"""

import numpy as np
from ..thermo.thermodynamics import Thermodynamics
from PyMPDATA_examples import Shipway_and_Hill_2012 as kid


def bulk_scheme_condensation(temp, press, qvap, qcond):
    """enacts saturation adjustment on qvap and qcond for a very simple bulk
    scheme to ensure relative humidity <= 100%. Extracted from pyMPDATA
    KiD Bulk Microphysics Scheme (nr=1) for Condensation
    from Shipway and Hill 2012 example for a 1-D KiD rainshaft model.
    """
    pvs = kid.formulae.pvs_Celsius(temp - kid.const.T0)
    relh = kid.formulae.pv(press, qvap) / pvs

    dql_cond = np.maximum(0, qvap * (1 - 1 / relh))

    qvap -= dql_cond
    qcond += dql_cond

    return qvap, qcond


# TODO(CB): add documentation
class MicrophysicsSchemeWrapper:
    def __init__(self):
        """Initialize the WrappedKiDBulkMicrophysics object."""
        self.microphys = "pyMPDATA KiD Bulk Microphysics Scheme for Condensation"
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

        temp = thermo.temp
        press = thermo.press
        qvap = thermo.massmix_ratios[0]
        qcond = thermo.massmix_ratios[1]

        qvap, qcond = bulk_scheme_condensation(temp, press, qvap, qcond)

        thermo.massmix_ratios[0] = qvap
        thermo.massmix_ratios[1] = qcond

        return thermo
