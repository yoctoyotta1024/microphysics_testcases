'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: observe_thermodynamics.py
Project: src_py
Created Date: Thursday 29th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Thursday 29th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
class for storing thermodynamics output during model run
'''

from .thermodynamics import Thermodynamics

class OutputVariable():
  '''Class stores a variable with some of its metadata.

  Attributes:
      name (string): name of variable.
      units (string): units of variable.
      value (any): value of variable; must be able to be appended to
  '''
  def __init__(self, name, units, value):

    self.name = name
    self.units = units
    self.value = value

  def write(self, val):

    self.value.append(val)

class ObserveThermodynamics:
  '''Class stores the thermodynamic variables output during model timestep.

  Thermodynamic variables include pressure, temperature, moist air density and the specific
  content (mass mixing ratio) of vapour and condensates.

  Attributes:
      temp (float): Temperature (K).
      rho (float): Density of moist air (kg/m3)
      press (float): Pressure (Pa).
      qvap (float): Specific water vapor content (kg/kg)
      qcond (float): Specific cloud water content (kg/kg)
      qice (float): Specific cloud ice content (kg/kg)
      qrain (float): Specific rain content (kg/kg)
      qsnow (float): Specific snow content kg/kg)
      qgrau (float): Specific graupel content (kg/kg)

  '''

  def __init__(self):
    '''Initialize a thermodynamics observer object.'''

    self.temp = OutputVariable('temp', 'K', [])
    self.rho = OutputVariable('rho', 'Kg m-3', [])
    self.press = OutputVariable('press', 'Pa', [])
    self.qvap = OutputVariable('qvap', 'Kg/Kg', [])
    self.qcond = OutputVariable('qcond', 'Kg/Kg', [])
    self.qice = OutputVariable('qice', 'Kg/Kg', [])
    self.qrain = OutputVariable('qrain', 'Kg/Kg', [])
    self.qsnow = OutputVariable('qsnow', 'Kg/Kg', [])
    self.qgrau = OutputVariable('qgrau', 'Kg/Kg', [])

  def write_thermodynamics(self, thermo: Thermodynamics):

    self.temp.write(thermo.temp)
    self.rho.write(thermo.rho)
    self.press.write(thermo.press)

    self.qvap.write(thermo.massmix_ratios[0])
    self.qcond.write(thermo.massmix_ratios[1])
    self.qice.write(thermo.massmix_ratios[2])
    self.qrain.write(thermo.massmix_ratios[3])
    self.qsnow.write(thermo.massmix_ratios[4])
    self.qgrau.write(thermo.massmix_ratios[5])
