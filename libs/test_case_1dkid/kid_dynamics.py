"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: kid_dynamics.py
Project: test_case_1dkid
Created Date: Monday 2nd September 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Wednesday 4th June 2025
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
from PyMPDATA_examples.Shipway_and_Hill_2012 import si
from PyMPDATA_examples.Shipway_and_Hill_2012 import formulae as SH2012formulae

from .mpdata import MPDATA
from .settings import Settings


class KiDDynamics:
    """A class for driving the KiD rainshaft test case, based on Shipway and Hill 2012.

    This class is a wrapper around the MPDATA driver of the Shipway and Hill 2012 example
    in the PyMPDATA-examples library.

    See https://github.com/open-atmos/PyMPDATA/tree/main/examples/PyMPDATA_examples/Shipway_and_Hill_2012
    for the original source code.
    """

    def __init__(self, z_delta, z_max, timestep, t_end):
        """Initialize the KiDDynamics object.

        Args:
            z_delta (float): Vertical grid spacing [m].
            z_max (float): Maximum height of the domain (top of half-cell) [m].
            timestep (float): Size of time steps of simulation [s].
            t_end (float): End time of the simulation [s].
        """
        options = Options(n_iters=3, nonoscillatory=True)

        RHOD_VERTVELO = 3 * si.m / si.s * si.kg / si.m**3
        P0 = 1007 * si.hPa
        self.settings = Settings(
            dt=timestep,
            dz=z_delta,
            rhod_w_const=RHOD_VERTVELO,
            t_max=t_end,
            p0=P0,
            z_max=z_max,
        )

        self.mpdata = MPDATA(
            nz=self.settings.nz,
            dt=self.settings.dt,
            qv_of_zZ_at_t0=lambda zZ: self.settings.qv(zZ * self.settings.dz),
            g_factor_of_zZ=lambda zZ: self.settings.rhod(zZ * self.settings.dz),
            options=options,
        )

        assert self.settings.nz == int(z_max / z_delta)
        assert self.settings.dz == z_delta
        nz = self.settings.nz
        zfull = np.linspace(z_delta / 2, (nz - 1 / 2) * z_delta, nz, endpoint=True)
        self.zhalf = np.linspace(0, nz * z_delta, nz + 1, endpoint=True)

        self.rhod_prof = self.settings.rhod(zfull)
        self.temp_prof = SH2012formulae.temperature(
            self.rhod_prof, self.settings.thd(zfull)
        )
        qvap0 = self.mpdata["qv"].advectee.get()
        self.press_prof = SH2012formulae.pressure(self.rhod_prof, self.temp_prof, qvap0)

        key = f"nr={self.mpdata.nr}, dz={self.settings.dz}, dt={self.settings.dt}, options={options}"
        print(f"Simulating {self.settings.nt} timesteps using {key}")

    def set_thermo(self, thermo):
        """Set thermodynamics from the dynamics solver.

        Args:
            thermo (Thermodynamics): Object representing the thermodynamic state.

        Returns:
            Thermodynamics: Updated thermodynamic state.
        """
        thermo.temp = self.temp_prof
        thermo.rho = self.rhod_prof
        thermo.press = self.press_prof
        thermo.massmix_ratios[0] = self.mpdata["qv"].advectee.get()  # qvap
        thermo.massmix_ratios[1] = self.mpdata["ql"].advectee.get()  # qcond

        return thermo

    def run(self, time, timestep, thermo):
        """
        Run the 1-D KiD motion computations.

        This method integrates the equations from time to time+timestep
        for the dynamics of a 1-D KiD rainshaft.

        Args:
            time (float): Current time [s].
            timestep (float): Size of timestep for the simulation [s].
            thermo (Thermodynamics): Object representing the thermodynamic state.

        Returns:
            Thermodynamics: Updated thermodynamic state.
        """
        assert timestep == self.settings.dt, "Timestep must match initialised value."

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
