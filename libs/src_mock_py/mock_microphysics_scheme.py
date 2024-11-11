"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: mock_microphysics_scheme.py
Project: src_mock_py
Created Date: Tuesday 27th February 2024
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
class for mock microphysics scheme in Python
"""


class MicrophysicsScheme:
    """A class representing a Python microphysics scheme which is a mock-up of the muphys-cpp graupel
    class for ICON."""

    def __init__(self):
        """Init the MicrophysicsScheme object (Python only)"""

        self.name = "Python mock-up of an instance of muphys-cpp's graupel for ICON"
        self.n = 0

    def initialize(self):
        """Initialize the microphysics scheme.

        This method performs the initialization steps necessary for the microphysics scheme.

        """

        print("microphysics initialisation")

    def finalize(self):
        """Finalize the microphysics scheme.

        This method performs the finalization steps for the microphysics scheme.

        """

        print("microphysics finalisation")

    def run(self, nvec, ke, ivstart, dt, dz, t, rho, p, qv, qc, qi, qr, qs, qg, qnc):
        """Run the microphysics computations.

        This method executes the microphysics computations.

        Parameters:
            nvec (int):
              Number of horizontal points.
            ke (int):
              Number of grid points in vertical direction.
            ivstart (int):
              Start index for horizontal direction.
            dt (np.ndarray):
              Times-tep for integration of microphysics (s)
            dz (np.ndarray):
              Layer thickness of full levels (m).
            t (np.ndarray):
              Temperature (K).
            rho (np.ndarray):
              Density of moist air (kg/m3)
            p (np.ndarray):
              Pressure (Pa).
            qv (np.ndarray):
              Specific water vapor content (kg/kg)
            qc (np.ndarray):
              Specific cloud water content (kg/kg)
            qi (np.ndarray):
              Specific cloud ice content (kg/kg)
            qr (np.ndarray):
              Specific rain content (kg/kg)
            qs (np.ndarray):
              Specific snow content kg/kg)
            qg (np.ndarray):
              Specific graupel content (kg/kg)
            qnc (np.ndarray):
              Cloud number concentration.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray,
            np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
                - Updated temperature (K).
                - Updated specific water vapor content (kg/kg)
                - Updated specific cloud water content (kg/kg)
                - Updated specific cloud ice content (kg/kg)
                - Updated specific rain content (kg/kg)
                - Updated specific snow content kg/kg)
                - Updated specific graupel content kg/kg)
                - Updated precipitation rate of rain, grid-scale (kg/(m2*s))
                - Updated total precipitation flux

        """

        ### some mock exchange of mass between vapour and condensate categories
        if self.n % 50 == 0:
            qv += (-1) ** self.n * 0.001
            qc += (-1) ** (self.n + 1) * 0.001
            qi += (-1) ** self.n * 0.002
            qr += (-1) ** (self.n + 1) * 0.002
            qs += (-1) ** self.n * 0.0003
            qg += (-1) ** (self.n + 1) * 0.0003
        self.n += 1

        prr_gsp = 0.001
        pflx = 0.01

        return t, qv, qc, qi, qr, qs, qg, prr_gsp, pflx
