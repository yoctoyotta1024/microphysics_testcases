"""
Copyright (c) 2025 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_cleo_sdm_microphysics_scheme.py
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
unit tests for cleo_sdm microphysics module
"""

import pytest


@pytest.fixture(scope="module")
def path2pycleo(pytestconfig):
    return pytestconfig.getoption("cleo_path2pycleo")


@pytest.fixture(scope="module")
def config_filename(pytestconfig):
    return pytestconfig.getoption("cleo_test_generic_config_filename")


def test_generic_cleo(path2pycleo, config_filename):
    """NOTE: tests assume CLEO's initial condition binary files already exist
    (i.e. 'dimlessGBxboundaries.dat' and 'dimlessSDsinit.dat' files, whose
    locations are given in CLEO's config file ('config_filename')
    """
    import subprocess
    from ruamel.yaml import YAML

    yaml = YAML()
    with open(config_filename, "r") as file:
        python_config = yaml.load(file)

    print("PYCLEO STATUS: creating GridboxMaps")
    print("gridfile:", python_config["inputfiles"]["grid_filename"])
    result = subprocess.run(["pwd"], capture_output=True, text=True, check=True)
    print("pwd:", result.stdout.strip())
    result = subprocess.run(
        ["ls", "./src/cleo_initial_conditions/generic/"], capture_output=True, text=True
    )
    print("ls:", result.stdout)
    result = subprocess.run(
        ["curl", "./src/cleo_initial_conditions/generic/dimlessGBxboundaries.dat"],
        capture_output=True,
        text=True,
    )
    print("ls:", result.stdout)
