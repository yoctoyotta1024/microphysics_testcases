"""
Copyright (c) 2025 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: conftest.py
Project: tests
Created Date: Monday 23rd June 2025
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 23rd June 2025
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
configuration file for pytests to allow tests to receive arguments
"""


def pytest_addoption(parser):
    from pathlib import Path

    default_aes_muphys_py_dir = (
        Path("/work")
        / "k20200"
        / "k202174"
        / "icon-mpim"
        / "ragnarok"
        / "build_py"
        / "src"
        / "aes_microphysics"
    )
    default_cleo_path2pycleo = Path.cwd() / "build" / "_deps" / "cleo-build" / "pycleo"
    parser.addoption(
        "--aes_muphys_py_dir", action="store", default=str(default_aes_muphys_py_dir)
    )
    parser.addoption(
        "--cleo_path2pycleo", action="store", default=str(default_cleo_path2pycleo)
    )

    default_cleo_test_generic_config_filename = (
        Path.cwd() / "src" / "cleo_initial_conditions" / "generic" / "config.yaml"
    )
    parser.addoption(
        "--cleo_test_generic_config_filename",
        action="store",
        default=str(default_cleo_test_generic_config_filename),
    )

    default_cleo_test_0dparcel_config_filename = (
        Path.cwd() / "src" / "cleo_initial_conditions" / "0dparcel" / "config.yaml"
    )
    parser.addoption(
        "--cleo_test_0dparcel_config_filename",
        action="store",
        default=str(default_cleo_test_0dparcel_config_filename),
    )

    cleo_initconds_1dkid_path = Path.cwd() / "src" / "cleo_initial_conditions" / "1dkid"
    default_cleo_test_1dkid_condevap_only_config_filename = (
        cleo_initconds_1dkid_path / "condevap_only" / "config.yaml"
    )
    default_cleo_test_1dkid_fullscheme_config_filename = (
        cleo_initconds_1dkid_path / "fullscheme" / "config.yaml"
    )
    parser.addoption(
        "--cleo_test_1dkid_condevap_only_config_filename",
        action="store",
        default=str(default_cleo_test_1dkid_condevap_only_config_filename),
    )
    parser.addoption(
        "--cleo_test_1dkid_fullscheme_config_filename",
        action="store",
        default=str(default_cleo_test_1dkid_fullscheme_config_filename),
    )
