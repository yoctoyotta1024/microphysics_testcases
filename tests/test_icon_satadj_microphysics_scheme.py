"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_icon_satadj_microphysics_scheme.py
Project: tests
Created Date: Thursday 21st November 2024
Author: Clara Bayley (CB)
Additional Contributors: Joerg Behrens, Georgiana Mania
-----
Last Modified: Friday 22nd November 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
unit tests for Python bindings to the saturation adjustment from ICON AES
one-moment bulk microphysics scheme
"""

import pytest
import numpy as np
import os
import warnings

from pathlib import Path


@pytest.fixture(scope="module")
def aes_muphys_py_dir(pytestconfig):
    return pytestconfig.getoption("aes_muphys_py_dir")


@pytest.hookimpl(tryfirst=True)
def test_aes_muphys_py_dir(aes_muphys_py_dir):
    if not Path(aes_muphys_py_dir).is_dir():
        warnings.warn(
            f"No ICON AES microphysics library found. Not running {Path(__file__).name}"
        )


def test_initialize_wrapper(aes_muphys_py_dir):
    if Path(aes_muphys_py_dir).is_dir():
        os.environ["AES_MUPHYS_PY_DIR"] = str(aes_muphys_py_dir)
        from libs.icon_satadj.microphysics_scheme_wrapper import (
            MicrophysicsSchemeWrapper,
        )

        nvec = 1
        ke = 1
        ivstart = 0
        dz = np.array([10], dtype=np.float64)
        qnc = 500
        microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

        assert microphys_wrapped.initialize() == 0


def test_finalize_wrapper(aes_muphys_py_dir):
    if Path(aes_muphys_py_dir).is_dir():
        os.environ["AES_MUPHYS_PY_DIR"] = str(aes_muphys_py_dir)
        from libs.icon_satadj.microphysics_scheme_wrapper import (
            MicrophysicsSchemeWrapper,
        )

        nvec = 1
        ke = 1
        ivstart = 0
        dz = np.array([10], dtype=np.float64)
        qnc = 500
        microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

        assert microphys_wrapped.finalize() == 0


def test_microphys_with_wrapper(aes_muphys_py_dir):
    if Path(aes_muphys_py_dir).is_dir():
        os.environ["AES_MUPHYS_PY_DIR"] = str(aes_muphys_py_dir)

        from libs.icon_satadj.microphysics_scheme_wrapper import (
            MicrophysicsSchemeWrapper,
            aes_muphys_py,
        )
        from libs.thermo.thermodynamics import Thermodynamics

        nvec = 1
        ke = 1
        ivstart = 0
        dz = np.array([10], dtype=np.float64)
        qnc = 500
        microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

        timestep = 1.0
        temp = np.array([288.15], dtype=np.float64)
        rho = np.array([1.225], dtype=np.float64)
        press = np.array([101325], dtype=np.float64)
        qvap = np.array([0.015], dtype=np.float64)
        qcond = np.array([0.0001], dtype=np.float64)
        qice = np.array([0.0002], dtype=np.float64)
        qrain = np.array([0.0003], dtype=np.float64)
        qsnow = np.array([0.0004], dtype=np.float64)
        qgrau = np.array([0.0005], dtype=np.float64)
        wvel = uvel = vvel = np.array([])  # this microphysics test doesn't need winds

        thermo = Thermodynamics(
            temp,
            rho,
            press,
            qvap,
            qcond,
            qice,
            qrain,
            qsnow,
            qgrau,
            wvel,
            uvel,
            vvel,
        )

        # call saturation adjustment
        total_ice = qgrau + qsnow + qice  # temporary variable
        aes_muphys_py.saturation_adjustment(
            ncells=nvec,
            nlev=ke,
            ta=temp,
            qv=qvap,
            qc=qcond,
            qr=qrain,
            total_ice=total_ice,
            rho=rho,
        )

        result = microphys_wrapped.run(timestep, thermo)

        assert result.temp == temp
        assert result.unpack_massmix_ratios() == [
            qvap,
            qcond,
            qice,
            qrain,
            qsnow,
            qgrau,
        ]
