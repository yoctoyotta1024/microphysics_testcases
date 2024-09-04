"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_pympdata_bulk_microphysics_scheme.py
Project: tests
Created Date: Wednesday 4th September 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Wednesday 4th September 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
unit tests for bulk microphysics scheme from pyMPDATA
"""

import numpy as np

from libs.pympdata_microphysics.bulk_scheme_condensation import (
    bulk_scheme_condensation,
    MicrophysicsSchemeWrapper,
)
from libs.thermo.thermodynamics import Thermodynamics


def test_bulk_scheme_condensation():
    temp = np.array([290])
    press = np.array([10100])
    qvap = np.array([0.999])
    qcond = np.array([0.0002])
    qvap, qcond = bulk_scheme_condensation(temp, press, qvap, qcond)

    qvap_correct = 0.30739488331808
    qcond_correct = 0.69180511668192
    thres = 2e-16

    assert qvap - qvap_correct < thres
    assert qcond_correct - qcond < thres


def test_initialize_wrapper():
    microphys_wrapped = MicrophysicsSchemeWrapper()

    assert microphys_wrapped.initialize() == 0


def test_finalize_wrapper():
    microphys_wrapped = MicrophysicsSchemeWrapper()

    assert microphys_wrapped.finalize() == 0


def test_microphys_with_wrapper():
    microphys_wrapped = MicrophysicsSchemeWrapper()

    timestep = 1.0
    temp = np.array([288.15])
    rho = np.array([1.225])
    press = np.array([101325])
    qvap = np.array([0.015])
    qcond = np.array([0.0001])
    qice = np.array([0.0002])
    qrain = np.array([0.0003])
    qsnow = np.array([0.0004])
    qgrau = np.array([0.0005])

    thermo = Thermodynamics(temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau)

    qv, qc = bulk_scheme_condensation(temp, press, qvap, qcond)

    thermo = microphys_wrapped.run(timestep, thermo)

    assert thermo.massmix_ratios == [qv, qc, qice, qrain, qsnow, qgrau]
