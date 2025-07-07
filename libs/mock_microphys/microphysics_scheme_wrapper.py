"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: microphysics_scheme_wrapper.py
Project: mock_microphys
Created Date: Wednesday 28th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 11th November 2024
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
from .mock_microphysics_scheme import MicrophysicsScheme

from copy import deepcopy


class MicrophysicsSchemeWrapper:
    """A class wrapping around Python MicrophysicsScheme for compatibility purposes.

    This class wraps around the MicrophysicsScheme class to provide compatibility with the Python
    run scripts and tests in this project. It initializes a MicrophysicsScheme object and provides
    wrappers around methods to initialize, finalize, and run the microphysics.

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
        self.microphys = MicrophysicsScheme()
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

        cp_thermo = deepcopy(thermo)
        dt = timestep
        t = cp_thermo.temp
        rho = cp_thermo.rho
        p = cp_thermo.press
        qv, qc, qi, qr, qs, qg = cp_thermo.unpack_massmix_ratios()

        t, qv, qc, qi, qr, qs, qg, prr_gsp, pflx = self.microphys.run(
            self.nvec,
            self.ke,
            self.ivstart,
            dt,
            self.dz,
            t,
            rho,
            p,
            qv,
            qc,
            qi,
            qr,
            qs,
            qg,
            self.qnc,
        )

        cp_thermo.temp[:] = t
        cp_thermo.copy_massmix_ratios(qv, qc, qi, qr, qs, qg)

        return cp_thermo
