'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: thermodynamics.py
Project: src_py
Created Date: Wednesday 28th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 17th June 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
'''

import numpy as np

class Thermodynamics:
  '''
  Class stores the thermodynamic variables required to run microphysics schemes in this project.

  Thermodynamic variables include pressure, temperature, moist air density and the specific
  content (mass mixing ratio) of vapour and condensates.

  Parameters:
    temp (float):
      Temperature (K).
    rho (float):
      Density of moist air (kg/m3).
    press (float):
      Pressure (Pa).
    qvap (float):
      Specific water vapor content (kg/kg).
    qcond (float):
      Specific cloud water content (kg/kg).
    qice (float):
      Specific cloud ice content (kg/kg).
    qrain (float):
      Specific rain content (kg/kg).
    qsnow (float):
      Specific snow content kg/kg).
    qgrau (float):
      Specific graupel content (kg/kg).

  Attributes:
    temp (float):
      Temperature (K).
    rho (float):
      Density of moist air (kg/m3).
    press (float):
      Pressure (Pa).
    massmix_ratios (tuple):
      Specific content of vapour and condensates (see below).

    massmax_ratios consists of the following:
            massmix_ratios[0] = qvap (float): Specific water vapor content (kg/kg)\n
            massmix_ratios[1] = qcond (float): Specific cloud water content (kg/kg)\n
            massmix_ratios[2] = qice (float): Specific cloud ice content (kg/kg)\n
            massmix_ratios[3] = qrain (float): Specific rain content (kg/kg)\n
            massmix_ratios[4] = qsnow (float): Specific snow content kg/kg)\n
            massmix_ratios[5] = qgrau (float): Specific graupel content (kg/kg).

  '''

  def __init__(self, temp: np.ndarray, rho: np.ndarray, press: np.ndarray, qvap: np.ndarray,
               qcond: np.ndarray, qice: np.ndarray, qrain: np.ndarray,
               qsnow: np.ndarray, qgrau: np.ndarray):
    '''Initialize a thermodynamics object with the given variables

    Parameters:
        press (np.array): Pressure (Pa).
        temp (np.array): Temperature (K).
        rho (np.array): Density of moist air (kg/m3)
        qvap (np.array): Specific water vapor content (kg/kg)
        qcond (np.array): Specific cloud water content (kg/kg)
        qice (np.array): Specific cloud ice content (kg/kg)
        qrain (np.array): Specific rain content (kg/kg)
        qsnow (np.array): Specific snow content kg/kg)
        qgrau (np.array): Specific graupel content (kg/kg)

    '''
    self.temp = temp
    self.rho = rho
    self.press = press
    self.massmix_ratios = [qvap, qcond, qice, qrain, qsnow, qgrau]
