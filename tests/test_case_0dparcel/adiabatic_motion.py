"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: adiabatic_motion.py
Project: test_case_0dparcel
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
class for driving adiabatic expansion/contraction test case
"""

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
          Specific heat capacity of water vapour [J/kg/K] (IAPWS97 at 273.15K).
        rgas_dry (float):
          Specific gas constant for dry air [J/kg/K] (approx. 287 J/kg/K).
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

        rgas_univ = 8.314462618  # universal molar gas constant [J/kg/K]
        mr_dry = 0.028966216  # molecular mass of dry air [kg/mol]
        mr_water = 0.01801528  # molecular mass of water [kg/mol]

        self.cp_dry = 1004.64  # specific heat capacity of water vapour [J/kg/K] (IAPWS97 at 273.15K)
        self.rgas_dry = (
            rgas_univ / mr_dry
        )  # specific gas constant for dry air [J/kg/K] (approx. 287 J/kg/K)
        self.epsilon = (
            mr_water / mr_dry
        )  # ratio of gas constants, dry air / water vapour (approx. 0.622)

        self.amp = amp  # amplitude of pressure sinusoid [Pa]
        self.omega = (
            2.0 * np.pi / tau
        )  # angular frequency of pressure sinusio (tau is time period) [radians s^-1]

    def dpress_dtime(self, time):
        r"""Calculate the rate of change of pressure with respect to time.

        The rate of change of pressure with respect to time is calculated from the equation:

        .. math:: \frac{dP}{dt} = - \omega \cdot A \cos(\omega t)

        so that pressure evolution follows:

        .. math:: P(t) = P_{\rm init} - A \sin(\omega t)

        where :math:`P_{\rm init} = P(t=t_{\rm{init}})`

        Args:
            time (float): Current time [s].

        Returns:
            float: Rate of change of pressure with respect to time [Pa/s].
        """

        dpress_dt = -self.omega * self.amp * np.cos(self.omega * time)

        return dpress_dt

    def dtemp_dtime(self, rho, dpress_dt):
        r"""Calculate the rate of change of temperature with respect to time.

        The rate of change of temperature with respect to time is calculated from the equation:

        .. math:: \frac{dT}{dt} = \frac{1}{\rho c_{\rm p, dry}} \frac{dP}{dt}

        assuming :math:`c_{\rm p} \approx c_{\rm p, dry}`,
        i.e. :math:`q_{\rm dry}c_{\rm p, dry} \gg  q_{\rm v}c_{\rm p, v}`,
        and :math:`q_{\rm dry}c_{\rm p, dry} \gg  q_{\rm v}c_{\rm k}` for all condensates :math:`k`.

        Args:
            rho (np.ndarray):
              Density of air [kg/m^3].
            dpress_dt (np.ndarray):
              Rate of change of pressure with respect to time [Pa/s].

        Returns:
            np.ndarray: Rate of change of temperature with respect to time [K/s].
        """

        dtemp_dt = dpress_dt / rho / self.cp_dry

        return dtemp_dt

    def drho_dtime(self, qvap, temp, rho, dtemp_dt, dpress_dt):
        r"""
        Calculate the rate of change of density with respect to time.

        The rate of change of temperature with respect to time is calculated from the equation:

        .. math::
          \frac{d\rho}{dt} = \frac{\rho}{P} \frac{dP}{dt} - \frac{\rho}{T} \frac{dT}{dt}

        where

        .. math::
          P = \rho R_{\rm dry} \left(1 + \frac{q_{\rm v}}{\epsilon}\right) T

        assuming :math:`q_{\rm v} \approx r_{\rm v}`, i.e. :math:`q_{\rm dry} \gg  q_{\rm v}`.

        Args:
            temp (np.ndarray):
              Temperature of air [K].
            rho (np.ndarray):
              Density of air [kg/m^3].
            qvap (np.ndarray):
              Mass mixing ratio of water vapor [kg/kg].
            dpress_dt (np.ndarray):
              Rate of change of pressure with respect to time [Pa/s].
            dtemp_dt (np.ndarray):
              Rate of change of temperature with respect to time [K/s].

        Returns:
            np.ndarray: Rate of change of density with respect to time [kg/m^3/s].
        """

        rgas_eff = self.rgas_dry * (1 + qvap / self.epsilon)

        drho_dt_temp = -dtemp_dt * rho / temp
        drho_dt_press = dpress_dt / rgas_eff / temp

        drho_dt = drho_dt_press + drho_dt_temp

        return drho_dt

    def adiabatic_odes(self, y, time, qvap):
        temp, rho, press = y
        dpress_dt = self.dpress_dtime(time)
        dtemp_dt = self.dtemp_dtime(rho, dpress_dt)
        drho_dt = self.drho_dtime(qvap, temp, rho, dtemp_dt, dpress_dt)

        return [dtemp_dt, drho_dt, dpress_dt]

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
        assert (
            thermo.temp.size == 1
        ), "AdiabaticMotion only applicable to 0-D parcel (1 element)"
        assert (
            thermo.rho.size == 1
        ), "AdiabaticMotion only applicable to 0-D parcel (1 element)"
        assert (
            thermo.press.size == 1
        ), "AdiabaticMotion only applicable to 0-D parcel (1 element)"
        assert (
            thermo.massmix_ratios[0].size == 1
        ), "AdiabaticMotion only applicable to 0-D parcel (1 element)"

        t0, t1 = time, time + timestep
        qvap = thermo.massmix_ratios[0][0]

        y0 = [thermo.temp[0], thermo.rho[0], thermo.press[0]]
        temp, rho, press = integrate.odeint(
            self.adiabatic_odes, y0, [t0, t1], args=(qvap,)
        )[1]

        thermo.temp = np.array([temp], dtype=np.float64)
        thermo.rho = np.array([rho], dtype=np.float64)
        thermo.press = np.array([press], dtype=np.float64)

        return thermo
