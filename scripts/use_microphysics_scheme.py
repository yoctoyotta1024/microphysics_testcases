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

def main():
  """Run an example of using the MicrophysicsScheme class through the
  MicrophysicsSchemeWrapper class.

  This function demonstrates an example usage of the microphysics scheme wrapped by the
  MicrophysicsSchemeWrapper class. It creates an instance of the MicrophysicsSchemeWrapper class,
  initializes it, loops over series of computations using the `run` method, and finalizes it.
  """

  press = 101325
  temp = 288.15
  rho = 1.225
  qvap = 0.015
  qcond = 0.0
  qice = 0.0
  qrain = 0.0
  qsnow = 0.0
  qgrau = 0.0
  thermo = Thermodynamics(press, temp, rho, qvap, qcond, qice, qrain, qsnow, qgrau)

  nvec = 1
  ke = 1
  ivstart = 0
  dz = 10
  qnc = 500
  microphys = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

  print("\n--- Example of using: "+microphys.name+" ---\n")

  microphys.initialize()

  ### run 11 steps print value returned by microphysics
  time = 0.0
  time_end = 10.0
  timestep = 1.0
  while time <= time_end:

    thermo = microphys.run(timestep, thermo)

    print("temp = "+str(thermo.temp))

    time += timestep

  microphys.finalize()

  print("\n--- Example Complete ---\n")

if __name__ == "__main__":
    main()
