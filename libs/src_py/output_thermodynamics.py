'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: output_thermodynamics.py
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
  '''Class is method to output a variable with some of its metadata.

  Attributes:
      name (string): name of variable.
      units (string): units of variable.
      value (any): value of variable; must be able to be appended to
  '''

  def __init__(self, name, units, value):
    '''Initialise OutputVariable instance

    Parameters:
        name (string): name of variable.
        units (string): units of variable.
        value (any): value of variable; must be able to be appended to
    '''

    self.name = name
    self.units = units
    self.value = value

  def write(self, val):
    self.value.append(val)

class OutputThermodynamics:
  '''Class is method and store for thermodynamic variables output during model timestep.

  Thermodynamic variables include pressure, temperature, moist air density and the specific
  content (mass mixing ratio) of vapour and condensates.

  Attributes:
      time (OutputVariable): time (s).
      temp (OutputVariable): Temperature (K).
      rho (OutputVariable): Density of moist air (kg/m3)
      press (OutputVariable): Pressure (Pa).
      qvap (OutputVariable): Specific water vapor content (kg/kg)
      qcond (OutputVariable): Specific cloud water content (kg/kg)
      qice (OutputVariable): Specific cloud ice content (kg/kg)
      qrain (OutputVariable): Specific rain content (kg/kg)
      qsnow (OutputVariable): Specific snow content kg/kg)
      qgrau (OutputVariable): Specific graupel content (kg/kg)

  '''

  def __init__(self):
    '''Initialize a thermodynamics output object.'''

    self.time = OutputVariable('time', 's', [])

    self.temp = OutputVariable('temp', 'K', [])
    self.rho = OutputVariable('rho', 'Kg m-3', [])
    self.press = OutputVariable('press', 'Pa', [])

    self.qvap = OutputVariable('qvap', 'Kg/Kg', [])
    self.qcond = OutputVariable('qcond', 'Kg/Kg', [])
    self.qice = OutputVariable('qice', 'Kg/Kg', [])
    self.qrain = OutputVariable('qrain', 'Kg/Kg', [])
    self.qsnow = OutputVariable('qsnow', 'Kg/Kg', [])
    self.qgrau = OutputVariable('qgrau', 'Kg/Kg', [])

  def output_thermodynamics(self, time: float, thermo: Thermodynamics):
    '''operator to output thermodynamics from thermo to each variable in thermodynamics output.'''

    self.time.write(time)

    self.temp.write(thermo.temp)
    self.rho.write(thermo.rho)
    self.press.write(thermo.press)

    self.qvap.write(thermo.massmix_ratios[0])
    self.qcond.write(thermo.massmix_ratios[1])
    self.qice.write(thermo.massmix_ratios[2])
    self.qrain.write(thermo.massmix_ratios[3])
    self.qsnow.write(thermo.massmix_ratios[4])
    self.qgrau.write(thermo.massmix_ratios[5])

  def __call__(self, time: float, thermo: Thermodynamics):
    ''' callable for using class as operator() '''
    self.output_thermodynamics(time, thermo)
