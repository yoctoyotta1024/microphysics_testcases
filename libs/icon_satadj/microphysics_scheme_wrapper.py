"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: microphysics_scheme_wrapper.py
Project: icon_satadj
Created Date: Thursday 21st November 2024
Author: Clara Bayley (CB)
Additional Contributors: Joerg Behrens, Georgiana Mania
-----
Last Modified: Friday 22nd November 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
wrapper function for an instance of MicrophysicsScheme so it can be used by generic test cases
and run scripts
NOTE: To use the wrapper, you must first export "AES_MUPHYS_PY_DIR". Currently on Levante, do:
export AES_MUPHYS_PY_DIR=/work/k20200/k202174/icon-mpim/ragnarok/build_py/src/aes_microphysics/
"""

import os
import sys
from copy import deepcopy

from ..thermo.thermodynamics import Thermodynamics

sys.path.append(
    os.environ["AES_MUPHYS_PY_DIR"]
)  # TODO(ALL): receive as argument to class
import aes_muphys_py


class MicrophysicsSchemeWrapper:
    """A class wrapping around ICON AES saturation adjustment as a MicrophysicsScheme
    (without AES microphysics)

    This class wraps around python bindings to the ICON one-moment saturation adjustment
    to provide compatibility with the Python run scripts and tests in this project. It
    initializes the ICON MicrophysicsScheme object and provides wrappers around methods to
    initialize, finalize, and run the microphysics.

    Args:
        nvec (int):
          Number of horizontal points.
        ke (int):
          Number of grid points in vertical direction.
        ivstart (int):
          Start index for horizontal direction.
        dz (np.ndarray):
          Layer thickness of full levels (m).
        qnc (float):
          Cloud number concentration.

    Attributes:
        nvec (int):
          Number of horizontal points.
        ke (int):
          Number of grid points in vertical direction.
        ivstart (int):
          Start index for horizontal direction.
        dz (np.ndarray):
          Layer thickness of full levels (m).
        qnc (float):
          Cloud number concentration.
        microphys (MicrophysicsScheme):
          instance of Python MicrophysicsScheme.

    """

    def __init__(self, nvec, ke, ivstart, dz, qnc):
        """Initialize the MicrophysicsSchemeWrapper object.

        Args:
          nvec (int):
            Number of horizontal points.
          ke (int):
            Number of grid points in vertical direction.
          ivstart (int):
            Start index for horizontal direction.
          dz (np.ndarray):
            Layer thickness of full levels (m).
          qnc (float):
            Cloud number concentration.

        """
        self.nvec = nvec
        self.ke = ke
        self.ivstart = ivstart
        self.dz = dz
        self.qnc = qnc
        self.microphys = aes_muphys_py
        self.name = (
            "Wrapper around " + "ICON Saturation Adjustment"
        )  # self.microphys.name

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

        cp_thermo = deepcopy(thermo)
        t = cp_thermo.temp
        rho = cp_thermo.rho
        qv, qc, qi, qr, qs, qg = cp_thermo.massmix_ratios

        # call saturation adjustment
        total_ice = qg + qs + qi  # temporary variable
        aes_muphys_py.saturation_adjustment(
            ncells=self.nvec,
            nlev=self.ke,
            ta=t,
            qv=qv,
            qc=qc,
            qr=qr,
            total_ice=total_ice,
            rho=rho,
        )

        cp_thermo.temp = t
        cp_thermo.massmix_ratios = [qv, qc, qi, qr, qs, qg]

        return cp_thermo
