'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: use_microphysics_scheme.py
Project: scripts
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Wednesday 28th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
'''


import sys
import pathlib
import numpy as np

path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(path+'/../libs/') # add path to src_py to PATH

from src_py.thermodynamics import Thermodynamics
from src_py.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper

def print_message(time, thermo):
  """Print statement about the time and some thermodynamic variables."""

  msg = "time = {:.1f}s: ".format(time)
  msg += "[T, rho, P] = [{:.2f}K, {:.3f}Kgm^-3, {:.0f}Pa]".format(thermo.temp, thermo.rho, thermo.press)

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

  temp = 288.15
  rho = 1.225
  press = 101325
  qvap = 0.015
  qcond = 0.0
  qice = 0.0
  qrain = 0.0
  qsnow = 0.0
  qgrau = 0.0
  thermo = Thermodynamics(temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau)

  nvec = 1
  ke = 1
  ivstart = 0
  dz = 10
  qnc = 500
  microphys = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

  print("\n--- Example of using: "+microphys.name+" ---\n")

  microphys.initialize()

  timestep_model(time_init, time_end, timestep, thermo, microphys)

  microphys.finalize()

  print("\n--- Example Complete ---\n")

if __name__ == "__main__":
    main()
