'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_microphysics_scheme.py
Project: tests
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
mock unit tests for Python microphysics module
'''


from libs.src_py.microphysics_scheme import MicrophysicsScheme

def test_microphys():

	microphys = MicrophysicsScheme()

	assert microphys.initialize() == 0

	assert microphys.run(0,1) == 1
	assert microphys.run(0,2) == 2

	assert microphys.finalize() == 0
