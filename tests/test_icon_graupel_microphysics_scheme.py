"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_icon_graupel_microphysics_scheme.py
Project: tests
Created Date: Tuesday 27th February 2024
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
unit tests for Python bindings of ICON's graupel one-moment bulk microphysics scheme
"""

import numpy as np
import os

path = os.environ.get("AES_MUPHYS_PY_DIR")
if path and path is not None:
    from libs.icon_graupel.microphysics_scheme_wrapper import (
        MicrophysicsSchemeWrapper,
        aes_muphys_py,
    )
    from libs.thermo.thermodynamics import Thermodynamics

    """  def test_initialize():
        microphys = aes_muphys_py

        assert microphys.initialize() is None

    def test_finalize():
        microphys = aes_muphys_py

        assert microphys.finalize() is None

    def test_initialize_wrapper():
        nvec = 1
        ke = 1
        ivstart = 0
        dz = np.array([10], dtype=np.float64)
        qnc = 500
        microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

        assert microphys_wrapped.initialize() == 0

    def test_finalize_wrapper():
        nvec = 1
        ke = 1
        ivstart = 0
        dz = np.array([10], dtype=np.float64)
        qnc = 500
        microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

        assert microphys_wrapped.finalize() == 0
 """

    def test_microphys_with_wrapper():
        microphys = aes_muphys_py
        nvec = 1
        ke = 1
        ivstart = 0
        dz = np.array([10], dtype=np.float64)
        qnc = np.float64(500)
        microphys_wrapped = MicrophysicsSchemeWrapper(nvec, ke, ivstart, dz, qnc)

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
        aes_muphys_py.saturation_adjustment(
            ncells=nvec,
            nlev=ke,
            ta=temp,
            qv=qvap,
            qc=qcond,
            qr=qrain,
            total_ice=qgrau + qsnow + qice,
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
        )

        # temporary variable
        total_ice = qgrau + qsnow + qice

        # call saturation adjustment
        aes_muphys_py.saturation_adjustment(
            ncells=nvec,
            nlev=ke,
            ta=temp,
            qv=qvap,
            qc=qcond,
            qr=qrain,
            total_ice=qgrau + qsnow + qice,
            rho=rho,
        )

        result = microphys_wrapped.run(timestep, thermo)

        microphys_wrapped.finalize()

        assert result.temp == temp
        assert result.massmix_ratios == [qvap, qcond, qice, qrain, qsnow, qgrau]
