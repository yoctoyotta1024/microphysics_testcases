"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: kid_dynamics.py
Project: test_case_1dkid
Created Date: Monday 2nd September 2024
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
class for driving KiD rainshaft test case
"""

from PyMPDATA import Options
from PyMPDATA_examples import Shipway_and_Hill_2012 as kid


class KiDDynamics:
    """A class for driving the KiD rainshaft test case, based on Shipway and Hill 2012.

    Class is wrapper around MPDATA driver of Shipway and Hill 2012 example in pyMPDATA.
    """

    def __init__(self, nr, dz, dt, R_MIN, R_MAX, N_CCN_HALO):
        """Initialize the KiDDynamics object."""
        RHOD_VERTVELO = 3 * kid.si.m / kid.si.s * kid.si.kg / kid.si.m**3
        T_MAX = 15 * kid.si.minutes
        P0 = 1007 * kid.si.hPa
        Z_MAX = 3200 * kid.si.m

        self.options = Options(n_iters=3, nonoscillatory=True)
        self.key = f"nr={nr}_dz={dz}_dt={dt}_opt={self.options}"
        self.settings = kid.Settings(
            rhod_w_const=RHOD_VERTVELO,
            nr=nr,
            dt=dt,
            dz=dz,
            t_max=T_MAX,
            r_min=R_MIN,
            r_max=R_MAX,
            p0=P0,
            z_max=Z_MAX,
        )

        self.mpdata = kid.MPDATA(
            nr=nr,
            nz=self.settings.nz,
            dt=self.settings.dt,
            qv_of_zZ_at_t0=lambda zZ: self.settings.qv(zZ * self.settings.dz),
            g_factor_of_zZ=lambda zZ: self.settings.rhod(zZ * self.settings.dz),
            options=self.options,
            activation_bc=kid.DropletActivation(
                N_CCN_HALO, self.settings.dr, self.settings.dz
            ),
        )

        print(f"Simulating {self.settings.nt} timesteps using {self.key}")

    def run(self, time, timestep, thermo):
        """
        Run the 1-D KiD motion computations.

        This method integrates the equations from time to time+timestep for a 1-D KiD rainshaft.

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
        return thermo
