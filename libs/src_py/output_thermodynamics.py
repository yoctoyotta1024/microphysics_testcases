'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: output_thermodynamics.py
Project: src_py
Created Date: Thursday 29th February 2024
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
class for storing thermodynamics output during model run
'''


import numpy as np

from .thermodynamics import Thermodynamics

class OutputVariable:
  """Class to output a variable with some of its metadata.

  Attributes:
      name (string):
        Name of variable.
      units (string):
        Units of variable.
      values (any):
        Values of variable; must be able to be appended to.
  """

  def __init__(self, name, units, values):
    """Initialise OutputVariable instance

    Parameters:
      name (string):
        Name of variable.
      units (string):
        Units of variable.
      values (any):
        Values of variable; must be able to be appended to.
    """

    self.name = name
    self.units = units
    self.values = values

  def write(self, val):
    '''Append a value to the list of variable values.

    Parameters:
      val (any): Value to append.
    '''
    self.values.append(val)

  def finalize(self):
    '''Convert values to a NumPy array.'''
    self.values = np.asarray(self.values)

class OutputThermodynamics:
  '''Class is method and store for thermodynamic variables output during model timestep.

  Thermodynamic variables include pressure, temperature, moist air density and the specific
  content (mass mixing ratio) of vapour and condensates.

  Attributes:
      time (OutputVariable):
        time (s).
      temp (OutputVariable):
        Temperature (K).
      rho (OutputVariable):
        Density of moist air (kg/m3).
      press (OutputVariable):
        Pressure (Pa).
      qvap (OutputVariable):
        Specific water vapor content (kg/kg).
      qcond (OutputVariable):
        Specific cloud water content (kg/kg).
      qice (OutputVariable):
        Specific cloud ice content (kg/kg).
      qrain (OutputVariable):
        Specific rain content (kg/kg).
      qsnow (OutputVariable):
        Specific snow content kg/kg).
      qgrau (OutputVariable):
        Specific graupel content (kg/kg).
  '''

  def __init__(self):
    '''Initialize a ThermodynamicsOutput object.'''

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
    """output thermodynamics from thermo to each variable in thermodynamics output.

    This method writes time and thermodynamic variables from thermo such as temperature, density,
    pressure, and specific mass mixing ratios to the respective output variables.

    Parameters:
        time (float):
          The time at which the thermodynamic variables are output (s).
        thermo (Thermodynamics):
          An instance of the Thermodynamics class containing the thermodynamic variables to output.

    Returns:
        None
    """
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
    """Invoke the object as a function to call the `output_thermodynamics` method.

    Parameters:
        time (float):
          The time at which the thermodynamic variables are output (s).
        thermo (Thermodynamics):
          An instance of the Thermodynamics class containing the thermodynamic variables to output.

    Returns:
        None
    """
    self.output_thermodynamics(time, thermo)

  def finalize(self):
    """Finalize the thermodynamics output.

    This method finalizes the output of thermodynamic variables by calling the `finalize` method
    of each output variable, e.g. to ensure that all variables are properly formatted
    for further use or analysis.

    Returns:
        None
    """
    self.time.finalize()
    self.temp.finalize()
    self.rho.finalize()
    self.press.finalize()
    self.qvap.finalize()
    self.qcond.finalize()
    self.qice.finalize()
    self.qrain.finalize()
    self.qsnow.finalize()
    self.qgrau.finalize()
