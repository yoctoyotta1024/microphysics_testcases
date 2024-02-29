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

  def __init__(self, amp, tau):
    """Init the AdiabaticMotion object """

    rgas_univ = 8.314462618   # universal molar gas constant [J/Kg/K]
    mr_dry = 0.028966216      # molecular mass of dry air [Kg/mol]
    mr_water = 0.01801528     # molecular mass of water [Kg/mol]

    self.cp_dry = 1004.64     # specific heat capacity of water vapour [J/Kg/K] (IAPWS97 at 273.15K)
    self.rgas_dry = rgas_univ / mr_dry   # specific gas constant for dry air [J/Kg/K] (approx. 287 J/Kg/K)
    self.epsilon = mr_water / mr_dry     # ratio of gas constants, dry air / water vapour (approx. 0.622)

    self.amp = amp # amplitude of pressure sinusoid [Pa]
    self.omega = 2.0 * np.pi / tau # angular frequency of pressure sinusio (tau is time period) [radians s^-1]

  def dpress_dtime(self, time):

    dpress_dt = - self.omega * self.amp * np.cos(self.omega * time)

    return dpress_dt

  def dtemp_dtime(self, rho, dpress_dt):

    dtemp_dt = dpress_dt / rho / self.cp_dry

    return dtemp_dt

  def drho_dtime(self, temp, rho, qvap, dpress_dt, dtemp_dt):

    rgas_eff = self.rgas_dry * (1 + qvap / self.epsilon)

    drho_dt_temp = - dtemp_dt * rho / temp
    drho_dt_press = dpress_dt / rgas_eff / temp

    drho_dt = drho_dt_press + drho_dt_temp

    return drho_dt

  def run(self, time, timestep, thermo):
    """Run the adiabatic motion computations.

    This method executes the adiabatic expansion/contraction computations.

    """

    qvap = thermo.massmix_ratios[0]

    dpress_dt = self.dpress_dtime(time)
    dtemp_dt = self.dtemp_dtime(thermo.rho, dpress_dt)

    delta_press = dpress_dt * timestep
    delta_temp = dtemp_dt * timestep
    delta_rho = self.drho_dtime(thermo.temp, thermo.rho, qvap, dpress_dt, dtemp_dt) * timestep

    thermo.press += delta_press
    thermo.temp += delta_temp
    thermo.rho += delta_rho

    return thermo
