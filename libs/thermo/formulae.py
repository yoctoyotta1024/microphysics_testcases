"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: calcs.py
Project: thermo
Created Date: Friday 1st March 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 2nd September 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
functions for calculations of some quantities e.g. potential temperature(s)
"""


def dry_potential_temperature(temp, press, press0):
    r"""Calculate the potential temperature for dry air.

    This function calculates the potential temperature for dry air given the temperature and pressure.

    .. math::
          \theta_{\rm{dry}} = T \left( \frac{P_{\rm ref}}{P} \right)
              ^{ \frac{R_{\rm{dry}}}{c_{\rm{p, dry}}} }

    where :math:`P_{\rm ref}` is the first pressure in press array.

    Args:
      temp (array-like):
          Temperature values (K).
      press (array-like):
          Pressure values (Pa).

    Returns:
        array-like: The potential temperature (K).
    """

    rgas_univ = 8.314462618  # universal molar gas constant [J/Kg/K]
    mr_dry = 0.028966216  # molecular mass of dry air [Kg/mol]
    cp_dry = (
        1004.64  # specific heat capacity of water vapour [J/Kg/K] (IAPWS97 at 273.15K)
    )
    rgas_dry = (
        rgas_univ / mr_dry
    )  # specific gas constant for dry air [J/Kg/K] (approx. 287 J/Kg/K)

    theta_dry = temp * (press0 / press) ** (rgas_dry / cp_dry)

    return theta_dry


def supersaturation(temp, press, qvap):
    """
    Calculate supersaturation based on the method described in PyMPDATA-examples

    This function uses the calculations in the Shipway and Hill (2012) example from
    PyMPDATA-examples library to compute the supersaturation.

    Parameters:
    temp (float): Temperature in Kelvin.
    press (float): Pressure in Pascals.
    qvap (float): Specific humidity (kg/kg).

    Returns:
    float: Supersaturation value.
    """
    from PyMPDATA_examples import Shipway_and_Hill_2012 as kid

    pvs = kid.formulae.pvs_Celsius(temp - kid.const.T0)
    relh = kid.formulae.pv(press, qvap) / pvs

    return relh - 1
