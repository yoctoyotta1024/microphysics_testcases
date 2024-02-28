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

from src_py import microphysics_scheme

microphys = microphys.MicrophysicsScheme()