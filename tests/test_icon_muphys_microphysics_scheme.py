"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_icon_muphys_microphysics_scheme.py
Project: tests
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors: Joerg Behrens, Georgiana Mania
-----
Last Modified: Wednesday 4th June 2025
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
unit tests for Python bindings of ICON AES one-moment bulk microphysics scheme
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


def test_microphys_with_wrapper(aes_muphys_py_dir):
    if Path(aes_muphys_py_dir).is_dir():
        os.environ["AES_MUPHYS_PY_DIR"] = str(aes_muphys_py_dir)
        from libs.icon_muphys.microphysics_scheme_wrapper import (
            MicrophysicsSchemeWrapper,
            aes_muphys_py,
        )
        from libs.thermo.thermodynamics import Thermodynamics

        microphys = aes_muphys_py
        nvec = 1
        ke = 1
        ivstart = 0
        dz = np.array([10], dtype=np.float64)
        qnc = np.float64(500)
        lrain = True
        microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc, lrain)

        microphys_wrapped.initialize()

        timestep = np.float64(1.0)
        temp = np.array([288.15], dtype=np.float64)
        rho = np.array([1.225], dtype=np.float64)
        press = np.array([101325], dtype=np.float64)
        qvap = np.array([0.015], dtype=np.float64)
        qcond = np.array([0.0001], dtype=np.float64)
        qice = np.array([0.0002], dtype=np.float64)
        qrain = np.array([0.0003], dtype=np.float64)
        qsnow = np.array([0.0004], dtype=np.float64)
        qgrau = np.array([0.0005], dtype=np.float64)

        thermo = Thermodynamics(
            temp, rho, press, qvap, qcond, qice, qrain, qsnow, qgrau
        )

        prr_gsp = np.zeros(nvec, np.float64)
        pri_gsp = np.zeros(nvec, np.float64)
        prs_gsp = np.zeros(nvec, np.float64)
        prg_gsp = np.zeros(nvec, np.float64)
        pre_gsp = np.zeros(nvec, np.float64)
        pflx = np.zeros((nvec, ke), np.float64)

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

        microphys.run(
            ncells=nvec,
            nlev=ke,
            dt=timestep,
            dz=dz,
            t=temp,
            rho=rho,
            p=press,
            qv=qvap,
            qc=qcond,
            qi=qice,
            qr=qrain,
            qs=qsnow,
            qg=qgrau,
            qnc=qnc,
            prr_gsp=prr_gsp,
            pri_gsp=pri_gsp,
            prs_gsp=prs_gsp,
            prg_gsp=prg_gsp,
            pflx=pflx,
            pre_gsp=pre_gsp,
            lrain=lrain,
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

        microphys_wrapped.finalize()

        assert result.temp == temp
        assert result.unpack_massmix_ratios() == [
            qvap,
            qcond,
            qice,
            qrain,
            qsnow,
            qgrau,
        ]
