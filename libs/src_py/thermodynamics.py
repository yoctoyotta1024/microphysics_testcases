'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: thermodynamics.py
Project: src_py
Created Date: Wednesday 28th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Wednesday 28th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
'''


class Thermodynamics:
  '''Class stores the thermodynamic variables required to run microphysics schemes in this project.

  Thermodynamic variables include pressure, temperature, moist air density and the specific
  content (mass mixing ratio) of vapour and condensates.

  Parameters:
      press (float): Pressure (Pa).
      temp (float): Temperature (K).
      rho (float): Density of moist air (kg/m3)
      qvap (float): Specific water vapor content (kg/kg)
      qcond (float): Specific cloud water content (kg/kg)
      qice (float): Specific cloud ice content (kg/kg)
      qrain (float): Specific rain content (kg/kg)
      qsnow (float): Specific snow content kg/kg)
      qgrau (float): Specific graupel content (kg/kg)

  Attributes:
      press (float): Pressure (Pa).
      temp (float): Temperature (K).
      rho (float): Density of moist air (kg/m3)
      massmix_ratios (tuple): specific content of vapour and condensates,
                                in order: [
                                qvap (float): Specific water vapor content (kg/kg),
                                qcond (float): Specific cloud water content (kg/kg),
                                qice (float): Specific cloud ice content (kg/kg),
                                qrain (float): Specific rain content (kg/kg),
                                qsnow (float): Specific snow content kg/kg),
                                qgrau (float): Specific graupel content (kg/kg)
                                ]

  '''

  def __init__(self, press, temp, rho, qvap, qcond, qice, qrain, qsnow, qgrau):
    '''Initialize a thermodynamics object with the given variables

    Parameters:
        press (float): Pressure (Pa).
        temp (float): Temperature (K).
        rho (float): Density of moist air (kg/m3)
        qvap (float): Specific water vapor content (kg/kg)
        qcond (float): Specific cloud water content (kg/kg)
        qice (float): Specific cloud ice content (kg/kg)
        qrain (float): Specific rain content (kg/kg)
        qsnow (float): Specific snow content kg/kg)
        qgrau (float): Specific graupel content (kg/kg)

    '''
    self.press = press
    self.temp = temp
    self.rho = rho
    self.massmix_ratios = [qvap, qcond, qice, qrain, qsnow, qgrau]
