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


import numpy as np

class AdiabaticMotion():
  """A class for driving the adiabatic expansion/contraction of a volume of air"""

  def __init__(self, rho_amp, tau, temp_ref, press_ref):
    """Init the AdiabaticMoetion object """

    rgas_univ = 8.314462618   # universal molar gas constant [J/Kg/K]
    mr_dry = 0.028966216      # molecular mass of dry air [Kg/mol]
    mr_water = 0.01801528     # molecular mass of water [Kg/mol]

    self.rgas_dry = rgas_univ / mr_dry   # specific gas constant for dry air [J/Kg/K] (approx. 287 J/Kg/K)
    self.gamma_dry = 1.400               # ratio of dry air specific heat capacities (cp_dry / cv_dry)
    self.epsilon = mr_water / mr_dry     # ratio of gas constants, dry air / water vapour (approx. 0.622)

    self.rho_amp = rho_amp
    self.freq = 2.0 * np.pi / tau

    self.temp_ref = temp_ref
    self.press_ref = press_ref

  def kappa_const(self, qvap):

    kappa = self.rgas_dry * self.temp_ref / self.press_ref * (1 + qvap / self.epsilon)

    return kappa

  def drho_dt(self, time):

    drho_dt = -self.freq * self.rho_amp * np.cos(self.freq * time)

    return drho_dt

  def dtemp_drho(self, temp, rho):

    dtemp_drho = (self.gamma_dry - 1) * temp / rho

    return dtemp_drho

  def dpress_drho(self, press, rho):

    dpress_drho = self.gamma_dry * press / rho

    return dpress_drho

  def run(self, time, timestep, thermo):
    """Run the adiabatic motion computations.

    This method executes the adiabatic expansion/contraction computations.

    """

    delta_rho = self.drho_dt(time) * timestep
    delta_temp = self.dtemp_drho(thermo.temp, thermo.rho) * delta_rho
    delta_press = self.dpress_drho(thermo.press, thermo.rho) * delta_rho

    thermo.temp += delta_temp
    thermo.rho += delta_rho
    thermo.press += delta_press

    return thermo
