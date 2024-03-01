'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: adiabatic_motion.py
Project: test_case_0dparcel
Created Date: Wednesday 28th February 2024
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
class for driving adiabatic expansion/contraction test case
'''


import numpy as np
import scipy.integrate as integrate

class AdiabaticMotion:
  """A class for driving the adiabatic expansion/contraction of a volume of air.

  Enacts adiabatic sinusoidal pressure change of parcel of air.

  Args:
      amp (float):
        Amplitude of pressure sinusoid [Pa].
      tau (float):
        Time period of the pressure sinusoid [s].

  Attributes:
      amp (float):
        Amplitude of pressure sinusoid [Pa].
      omega (float):
        Angular frequency of pressure sinusoid (tau is time period) [radians s^-1].
      cp_dry (float):
        Specific heat capacity of water vapour [J/Kg/K] (IAPWS97 at 273.15K).
      rgas_dry (float):
        Specific gas constant for dry air [J/Kg/K] (approx. 287 J/Kg/K).
      epsilon (float):
        Ratio of gas constants, dry air / water vapour (approx. 0.622).
  """

  def __init__(self, amp, tau):
    """Initialize the AdiabaticMotion object.

    Args:
        amp (float):
          Amplitude of pressure sinusoid [Pa].
        tau (float):
          Time period of the pressure sinusoid [s].
    """

    rgas_univ = 8.314462618   # universal molar gas constant [J/Kg/K]
    mr_dry = 0.028966216      # molecular mass of dry air [Kg/mol]
    mr_water = 0.01801528     # molecular mass of water [Kg/mol]

    self.cp_dry = 1004.64     # specific heat capacity of water vapour [J/Kg/K] (IAPWS97 at 273.15K)
    self.rgas_dry = rgas_univ / mr_dry   # specific gas constant for dry air [J/Kg/K] (approx. 287 J/Kg/K)
    self.epsilon = mr_water / mr_dry     # ratio of gas constants, dry air / water vapour (approx. 0.622)

    self.amp = amp # amplitude of pressure sinusoid [Pa]
    self.omega = 2.0 * np.pi / tau # angular frequency of pressure sinusio (tau is time period) [radians s^-1]

  def dpress_dtime(self, time):
    """Calculate the rate of change of pressure with respect to time.

    The rate of change of pressure with respect to time is calculated from the equation:

    .. math:: \\frac{dP}{dt} = - \omega \cdot A \cos(\omega t)

    so that pressure evolution follows:

    .. math:: P(t) = P_{\\rm init} - A \sin(\omega t)

    where :math:`P_{\\rm init} = P(t=t_{\\rm{init}})`

    Args:
        time (float): Current time [s].

    Returns:
        float: Rate of change of pressure with respect to time [Pa/s].
    """

    dpress_dt = - self.omega * self.amp * np.cos(self.omega * time)

    return dpress_dt

  def dtemp_dtime(self, rho, dpress_dt):
    """Calculate the rate of change of temperature with respect to time.

    The rate of change of temperature with respect to time is calculated from the equation:

    .. math:: \\frac{dT}{dt} = \\frac{1}{\\rho c_{\\rm p, dry}} \\frac{dP}{dt}

    assuming :math:`c_{\\rm p} \\approx c_{\\rm p, dry}`,
    i.e. :math:`q_{\\rm dry}c_{\\rm p, dry} \gg  q_{\\rm v}c_{\\rm p, v}`,
    and :math:`q_{\\rm dry}c_{\\rm p, dry} \gg  q_{\\rm v}c_{\\rm k}` for all condensates :math:`k`.

    Args:
        rho (float):
          Density of air [Kg/m^3].
        dpress_dt (float):
          Rate of change of pressure with respect to time [Pa/s].

    Returns:
        float: Rate of change of temperature with respect to time [K/s].
    """
    dtemp_dt = dpress_dt / rho / self.cp_dry

    return dtemp_dt

  def drho_dtime(self, temp, rho, qvap, dpress_dt, dtemp_dt):
    """
    Calculate the rate of change of density with respect to time.

    The rate of change of temperature with respect to time is calculated from the equation:

    .. math::
      \\frac{d\\rho}{dt} = \\frac{\\rho}{P} \\frac{dP}{dt} - \\frac{\\rho}{T} \\frac{dT}{dt}

    where

    .. math::
      P = \\rho R_{\\rm dry} \\left(1 + \\frac{q_{\\rm v}}{\\epsilon}\\right) T

    assuming :math:`q_{\\rm v} \\approx r_{\\rm v}`, i.e. :math:`q_{\\rm dry} \gg  q_{\\rm v}`.

    Args:
        temp (float):
          Temperature of air [K].
        rho (float):
          Density of air [Kg/m^3].
        qvap (float):
          Mass mixing ratio of water vapor [Kg/Kg].
        dpress_dt (float):
          Rate of change of pressure with respect to time [Pa/s].
        dtemp_dt (float):
          Rate of change of temperature with respect to time [K/s].

    Returns:
        float: Rate of change of density with respect to time [Kg/m^3/s].
    """

    rgas_eff = self.rgas_dry * (1 + qvap / self.epsilon)

    drho_dt_temp = - dtemp_dt * rho / temp
    drho_dt_press = dpress_dt / rgas_eff / temp

    drho_dt = drho_dt_press + drho_dt_temp

    return drho_dt

  def run(self, time, timestep, thermo):
    """
    Run the adiabatic motion computations.

    This method integrates the equations from time to time+timestep for adiabatic
    expansion/contraction of a parcel of air.

    Args:
        time (float):
          Current time [s].
        timestep (float):
          Time step size for the simulation [s].
        thermo (Thermodynamics):
          Object representing the thermodynamic state of the air.

    Returns:
        Thermodynamics: Updated thermodynamic state of the air.
    """

    t0, t1 = time, time+timestep
    qvap = thermo.massmix_ratios[0]

    dpress_dt = self.dpress_dtime(time)
    dtemp_dt = self.dtemp_dtime(thermo.rho, dpress_dt)

    delta_press = integrate.quad(self.dpress_dtime, t0, t1, args=())[0]
    delta_temp = dtemp_dt * timestep
    delta_rho = self.drho_dtime(thermo.temp, thermo.rho, qvap, dpress_dt, dtemp_dt) * timestep

    thermo.press += delta_press
    thermo.temp += delta_temp
    thermo.rho += delta_rho

    return thermo
