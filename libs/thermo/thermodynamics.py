"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: thermodynamics.py
Project: thermo
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
"""

import numpy as np
from copy import deepcopy


class Thermodynamics:
    """
    Class stores the thermodynamic variables required to run microphysics schemes in this project.

    Thermodynamic variables include pressure, temperature, moist air density and the specific
    content (mass mixing ratio) of vapour and condensates.

    Parameters:
      temp (np.ndarray):
        Temperature (K).
      rho (np.ndarray):
        Density of moist air (kg/m3).
      press (np.ndarray):
        Pressure (Pa).
      qvap (np.ndarray):
        Specific water vapor content (kg/kg).
      qcond (np.ndarray):
        Specific cloud water content (kg/kg).
      qice (np.ndarray):
        Specific cloud ice content (kg/kg).
      qrain (np.ndarray):
        Specific rain content (kg/kg).
      qsnow (np.ndarray):
        Specific snow content kg/kg).
      qgrau (np.ndarray):
        Specific graupel content (kg/kg).

    Attributes:
      temp (np.ndarray):
        Temperature (K).
      rho (np.ndarray):
        Density of moist air (kg/m3).
      press (np.ndarray):
        Pressure (Pa).
      massmix_ratios (tuple):
        Specific content of vapour and condensates (see below).

      massmax_ratios consists of the following:
              massmix_ratios[0] = qvap (np.ndarray): Specific water vapor content (kg/kg)\n
              massmix_ratios[1] = qcond (np.ndarray): Specific cloud water content (kg/kg)\n
              massmix_ratios[2] = qice (np.ndarray): Specific cloud ice content (kg/kg)\n
              massmix_ratios[3] = qrain (np.ndarray): Specific rain content (kg/kg)\n
              massmix_ratios[4] = qsnow (np.ndarray): Specific snow content kg/kg)\n
              massmix_ratios[5] = qgrau (np.ndarray): Specific graupel content (kg/kg).

    """

    def __init__(
        self,
        temp: np.ndarray,
        rho: np.ndarray,
        press: np.ndarray,
        qvap: np.ndarray,
        qcond: np.ndarray,
        qice: np.ndarray,
        qrain: np.ndarray,
        qsnow: np.ndarray,
        qgrau: np.ndarray,
    ):
        """Initialize a thermodynamics object with the given variables

        Parameters:
            press (np.ndarray): Pressure (Pa).
            temp (np.ndarray): Temperature (K).
            rho (np.ndarray): Density of moist air (kg/m3)
            qvap (np.ndarray): Specific water vapor content (kg/kg)
            qcond (np.ndarray): Specific cloud water content (kg/kg)
            qice (np.ndarray): Specific cloud ice content (kg/kg)
            qrain (np.ndarray): Specific rain content (kg/kg)
            qsnow (np.ndarray): Specific snow content kg/kg)
            qgrau (np.ndarray): Specific graupel content (kg/kg)

        """
        self.temp = deepcopy(temp)
        self.rho = deepcopy(rho)
        self.press = deepcopy(press)
        self.massmix_ratios = deepcopy([qvap, qcond, qice, qrain, qsnow, qgrau])
