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

import numpy as np
from PyMPDATA import Options
from PyMPDATA_examples import Shipway_and_Hill_2012 as kid


class KiDDynamics:
    """A class for driving the KiD rainshaft test case, based on Shipway and Hill 2012.

    Class is wrapper around MPDATA driver of Shipway and Hill 2012 example in pyMPDATA.
    """

    def __init__(self, z_delta, z_max, timestep, t_end):
        """Initialize the KiDDynamics object."""
        N_CCN_HALO = 500 / kid.si.mg
        R_MIN = 1 * kid.si.um
        R_MAX = 20.2 * kid.si.um

        RHOD_VERTVELO = 3 * kid.si.m / kid.si.s * kid.si.kg / kid.si.m**3
        P0 = 1007 * kid.si.hPa
        NR = 1  # fixed value for bulk scheme microphysics

        self.options = Options(n_iters=3, nonoscillatory=True)
        self.key = f"nr={NR}_dz={z_delta}_dt={timestep}_opt={self.options}"
        self.settings = kid.Settings(
            rhod_w_const=RHOD_VERTVELO,
            nr=NR,
            dt=timestep,
            dz=z_delta,
            t_max=t_end,
            r_min=R_MIN,
            r_max=R_MAX,
            p0=P0,
            z_max=z_max,
        )

        self.mpdata = kid.MPDATA(
            nr=NR,
            nz=self.settings.nz,
            dt=self.settings.dt,
            qv_of_zZ_at_t0=lambda zZ: self.settings.qv(zZ * self.settings.dz),
            g_factor_of_zZ=lambda zZ: self.settings.rhod(zZ * self.settings.dz),
            options=self.options,
            activation_bc=kid.DropletActivation(
                N_CCN_HALO, self.settings.dr, self.settings.dz
            ),
        )

        z1 = self.settings.dz / 2
        z2 = (self.settings.nz - 1 / 2) * self.settings.dz
        z = np.linspace(
            z1,
            z2,
            self.settings.nz,
            endpoint=True,
        )

        self.rhod_prof = self.settings.rhod(z)
        self.temp_prof = kid.formulae.temperature(self.rhod_prof, self.settings.thd(z))
        qvap0 = self.mpdata["qv"].advectee.get()
        self.press_prof = kid.formulae.pressure(self.rhod_prof, self.temp_prof, qvap0)

        print(f"Simulating {self.settings.nt} timesteps using {self.key}")

    def set_thermo(self, thermo):
        thermo.temp = self.temp_prof
        thermo.rho = self.rhod_prof
        thermo.press = self.press_prof
        thermo.massmix_ratios[0] = self.mpdata["qv"].advectee.get()  # qvap
        thermo.massmix_ratios[1] = self.mpdata["ql"].advectee.get()  # qcond

        return thermo

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
        t = int(time / timestep)
        assert time % timestep == 0, "Time not a multiple of the timestep."

        GC = (
            self.settings.rhod_w((t + 0.5) * self.settings.dt)
            * self.settings.dt
            / self.settings.dz
        )
        advector_0 = np.ones_like(self.settings.z_vec) * GC

        self.mpdata["qv"].advector.get_component(0)[:] = advector_0
        self.mpdata["qv"].advance(1)

        self.mpdata["ql"].advector.get_component(0)[:] = advector_0
        self.mpdata["ql"].advance(1)

        thermo = self.set_thermo(thermo)
        return thermo
