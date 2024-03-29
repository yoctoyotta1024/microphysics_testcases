'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: mock_microphysics_scheme.py
Project: src_py
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Friday 1st March 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
class for mock microphysics scheme in Python
'''


import numpy as np

class MicrophysicsScheme:
  """A class representing a Python microphysics scheme which is a mock-up of the muphys-cpp graupel
  class for ICON."""

  def __init__(self):
    """Init the MicrophysicsScheme object (Python only) """

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
        dt (float):
          Times-tep for integration of microphysics (s)
        dz (float):
          Layer thickness of full levels (m).
        t (float):
          Temperature (K).
        rho (float):
          Density of moist air (kg/m3)
        p (float):
          Pressure (Pa).
        qv (float):
          Specific water vapor content (kg/kg)
        qc (float):
          Specific cloud water content (kg/kg)
        qi (float):
          Specific cloud ice content (kg/kg)
        qr (float):
          Specific rain content (kg/kg)
        qs (float):
          Specific snow content kg/kg)
        qg (float):
          Specific graupel content (kg/kg)
        qnc (float):
          Cloud number concentration.

    Returns:
        Tuple[float, float, float, float, float, float, float, float, float]:
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
      qv += (-1)**self.n * 0.001
      qc += (-1)**(self.n+1) * 0.001
      qi += (-1)**self.n * 0.002
      qr += (-1)**(self.n+1) * 0.002
      qs += (-1)**self.n * 0.0003
      qg += (-1)**(self.n+1) * 0.0003
    self.n += 1

    prr_gsp = 0.001
    pflx = 0.01

    return t, qv, qc, qi, qr, qs, qg, prr_gsp, pflx
