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
from libs.src_py.microphysics_scheme_wrapper import MicrophysicsSchemeWrapper
from libs.src_py.thermodynamics import Thermodynamics

def test_initialize():

	microphys = MicrophysicsScheme()

	assert microphys.initialize() == None

def test_finalize():

	microphys = MicrophysicsScheme()

	assert microphys.finalize() == None

def test_initialize_wrapper():

	nvec = 1
	ke = 1
	ivstart = 0
	dz = 10
	qnc = 500
	microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

	assert microphys_wrapped.initialize() == 0

def test_finalize_wrapper():

	nvec = 1
	ke = 1
	ivstart = 0
	dz = 10
	qnc = 500
	microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

	assert microphys_wrapped.finalize() == 0

def test_microphys_with_wrapper():

	microphys = MicrophysicsScheme()

	nvec = 1
	ke = 1
	ivstart = 0
	dz = 10
	qnc = 500
	microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

	timestep = 1.0
	temp = 288.15
	rho = 1.225
	press = 101325
	qvap = 0.015
	qcond = 0.0001
	qice = 0.0002
	qrain = 0.0003
	qsnow = 0.0004
	qgrau = 0.0005

	thermo = Thermodynamics(temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau)

	t, qv, qc, qi, qr, qs, qg, prr_gsp, pflx = microphys.run(nvec, ke, ivstart, timestep, dz, temp,
																													rho, press, qvap, qcond, qice,
																													qrain, qsnow, qgrau, qnc)

	thermo = microphys_wrapped.run(timestep, thermo)

	assert thermo.temp == t
	assert thermo.massmix_ratios == [qv, qc, qi, qr, qs, qg]
