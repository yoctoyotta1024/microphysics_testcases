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

path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(path+'/../libs/') # add path to src_py to PATH

from src_py.microphysics_scheme import MicrophysicsScheme

def main():

  microphys = MicrophysicsScheme()

  print("--- Example of using: "+microphys.name+" ---")

  microphys.initialize()

  some_value = 0
  for step in range(0, 10):
    # for 10 steps print value returned by microphysics

    some_value = microphys.run(some_value)

    print("i = "+str(some_value))

  microphys.finalize()

if __name__ == "__main__":
    main()
