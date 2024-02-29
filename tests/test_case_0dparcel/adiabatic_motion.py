'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: adiabatic_motion.py
Project: test_case_0dparcel
Created Date: Wednesday 28th February 2024
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
class for driving adiabatic expansion/contraction test case
'''


class AdiabaticMotion():
  """A class for driving the adiabatic expansion/contraction of a volume of air"""

  def __init__(self):
    """Init the AdiabaticMoetion object """

    self.name = "Adiabatic Motion Instance"

  def run(self, timestep, thermo):
    """Run the adiabatic motion computations.

    This method executes the adiabatic expansion/contraction computations.

    """

    delta_rho = drho_dt() * timestep
    delta_temp =
    delta_press =

    thermo.temp += delta_temp
    thermo.rho += delta_rho
    thermo.press += delta_press

    return thermo
