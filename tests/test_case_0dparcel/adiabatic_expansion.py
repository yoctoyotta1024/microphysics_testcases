'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: adiabatic_expansion.py
Project: test_case_0dparcel
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
class for driving adiabatic expansion test case
'''


class AdiabaticExpansion():
  """A class for driving the adiabatic expansion of a volume of air"""

  def __init__(self):
    """Init the AdiabaticExpansion object """

    self.name = "Adiabatic Expansion Instance"

  def run(self, timestep, thermo):
    """Run the adiabatic expansion computations.

    This method executes the adiabatic expansion computations.

    """

    delta_temp =
    delta_rho =
    delta_press =

    thermo.temp += delta_temp
    thermo.rho += delta_rho
    thermo.press += delta_press

    return thermo
