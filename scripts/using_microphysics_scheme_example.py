"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: using_microphysics_scheme_example.py
Project: scripts
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 11th November 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
Example of how a microphysics scheme can be used.
"""

import sys
import pathlib
import numpy as np

path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(path + "/../libs/")  # add path to python modules to PATH

from thermo.thermodynamics import Thermodynamics
from src_mock_py.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper


def print_message(time, thermo):
    """Print statement about the time and some thermodynamic variables."""

    msg = "time = {:.1f}s:\n".format(time)
    msg += "   T = " + str(["{:.2f}K".format(x) for x in thermo.temp]) + ",\n"
    msg += " rho = " + str(["{:.3f}Kgm^-3".format(x) for x in thermo.rho]) + ",\n"
    msg += "   P = " + str(["{:.0f}Pa".format(x) for x in thermo.press]) + ",\n"

    print(msg)


def timestep_model(time_init, time_end, timestep, thermo, microphys):
    """run timestepping of microphysics and print a statement about the returned
    thermodynamics at each timestep.

    """
    time = time_init
    while time <= time_end:
        print_message(time, thermo)

        thermo = microphys.run(timestep, thermo)

        time += timestep


def main():
    """Run an example of using the MicrophysicsScheme class through the
    MicrophysicsSchemeWrapper class.

    This function demonstrates an example usage of the microphysics scheme wrapped by the
    MicrophysicsSchemeWrapper class. It creates an instance of the MicrophysicsSchemeWrapper class,
    initializes it, loops over series of computations using the `run` method, and finalizes it.
    """

    time_init = 0.0
    time_end = 10.0
    timestep = 1.0

    temp = np.array([288.15])
    rho = np.array([1.225])
    press = np.array([101325])
    qvap = np.array([0.015])
    qcond = np.array([0.0])
    qice = np.array([0.0])
    qrain = np.array([0.0])
    qsnow = np.array([0.0])
    qgrau = np.array([0.0])
    thermo = Thermodynamics(temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau)

    nvec = 1
    ke = 1
    ivstart = 0
    dz = np.array([10])
    qnc = 500
    microphys = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

    print("\n--- Example of using: " + microphys.name + " ---\n")

    microphys.initialize()

    timestep_model(time_init, time_end, timestep, thermo, microphys)

    microphys.finalize()

    print("\n--- Example Complete ---\n")


if __name__ == "__main__":
    main()
