"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_bulkkid.py
Project: test_case_1dkid
Created Date: Monday 2nd September 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 2nd September 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: wip_1dkid_test_case.py
Project: test_case_1dkid
Created Date: Sunday 1st September 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 2nd September 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

# %% Function definitions
import numpy as np
from pathlib import Path
from PyMPDATA_examples import Shipway_and_Hill_2012 as kid
from PyMPDATA_examples.Shipway_and_Hill_2012 import si

from .perform_1dkid_test_case import perform_1dkid_test_case
from libs.src_mock_py.thermodynamics import Thermodynamics


class WrappedKiDBulkMicrophysics:
    def __init__(self):
        """Initialize the WrappedKiDBulkMicrophysics object."""
        self.microphys = "KiDBulkMicrophysics"
        self.name = "Wrapper around " + self.microphys.name

    def initialize(self) -> int:
        """Initialise the microphysics scheme.

        This method calls the microphysics initialisation

        Returns:
            int: 0 upon successful initialisation
        """
        return 0

    def finalize(self) -> int:
        """Finalise the microphysics scheme.

        This method calls the microphysics finalisation.

        Returns:
            int: 0 upon successful finalisation.
        """
        return 0

    def run(self, timestep: float, thermo: Thermodynamics) -> Thermodynamics:
        """Run the microphysics computations.

        This method is a wrapper of the MicrophysicsScheme object's run function to call the
        microphysics computations in a way that's compatible with the test and scripts in this project.

        Args:
            timestep (float):
              Time-step for integration of microphysics (s)
            thermo (Thermodynamics):
              Thermodynamic properties.

        Returns:
            Thermodynamics: Updated thermodynamic properties after microphysics computations.

        """
        qvap = thermo.massmix_ratios[0]
        pvs = kid.formulae.pvs_Celsius(thermo.temp - kid.const.T0)
        relh = kid.formulae.pv(thermo.press, qvap) / pvs

        dql_cond = np.maximum(0, qvap * (1 - 1 / relh))

        thermo.massmix_ratios[0] -= dql_cond
        thermo.massmix_ratios[1] += dql_cond

        return thermo


def test_mock_py_0dparcel():
    """runs test of 1-D KiD rainshaft model using bulk scheme extracted from pyMPDATA for
    microphysics scheme.

    This function sets up initial conditions and parameters for running a 1-D KiD rainshaft
    test case using the bulk microphysics scheme for condensation from the Shipway and Hill 2012
    pyMPDATA-examples example (via a wrapper). It then runs the test case as specified.
    """
    ### label for test case to name data/plots with
    run_name = "bulkkid_microphys_1dkid"

    ### path to directory to save data/plots in after model run
    binpath = Path(__file__).parent.resolve() / "bin"  # i.e. [current directory]/bin/
    binpath.mkdir(parents=False, exist_ok=True)

    ### time and grid parameters
    z_delta = 25 * si.m
    z_max = 3200 * si.m
    timestep = 0.25 / 2 * si.s
    time_end = 15 * si.minutes

    ### initial thermodynamic conditions
    assert z_max % z_delta == 0, "z limit is not a multiple of the grid spacing."
    zeros = np.zeros(int(z_max / z_delta))
    thermo_init = Thermodynamics(
        zeros, zeros, zeros, zeros, zeros, zeros, zeros, zeros, zeros
    )

    ### microphysics scheme to use (within a wrapper)
    microphys_scheme = WrappedKiDBulkMicrophysics()

    ### Perform test of 1-D KiD rainshaft model using chosen setup
    perform_1dkid_test_case(
        z_delta,
        z_max,
        time_end,
        timestep,
        thermo_init,
        microphys_scheme,
        binpath,
        run_name,
    )


# # %% Run 1-D KiD Model
# outputs = {}
# output = {
#     k: np.zeros((kiddyn.settings.nz, kiddyn.settings.nt + 1))
#     for k in ("qv", "S", "ql", "act_frac", "reldisp")
# }
# outputs[kiddyn.key] = output
# assert "t" not in output and "z" not in output
# output["t"] = np.linspace(
#     0, kiddyn.settings.nt * kiddyn.settings.dt, kiddyn.settings.nt + 1, endpoint=True
# )
# output["z"] = np.linspace(
#     kiddyn.settings.dz / 2,
#     (kiddyn.settings.nz - 1 / 2) * kiddyn.settings.dz,
#     kiddyn.settings.nz,
#     endpoint=True,
# )
# output["qv"][:, 0] = kiddyn.mpdata["qv"].advectee.get()

# [HERE runs model]

# output["ql"][:, t + 1] = ql
# output["qv"][:, t + 1] = qv
# output["S"][:, t + 1] = RH - 1


# # %% plot results
# cmap = "gray"
# rasterized = False
# figsize = (3.5, 3.5)
# print(kiddyn.key)

# kid.plot(
#     var="qv",
#     mult=1e3,
#     label="$q_v$ [g/kg]",
#     output=outputs[f"{kiddyn.key}"],
#     cmap=cmap,
#     threshold=1e-3,
# )
# savename = binpath / "kid1d_qvap.png"
# plt.savefig(savename, bbox_inches="tight")

# kid.plot(
#     var="ql",
#     mult=1e3,
#     label="$q_l$ [g/kg]",
#     output=outputs[f"{kiddyn.key}"],
#     cmap=cmap,
#     threshold=1e-3,
#     figsize=figsize,
# )
# savename = binpath / "kid1d_qcond.png"
# plt.savefig(savename, bbox_inches="tight")

# kid.plot(
#     var="S",
#     mult=1e2,
#     label="$S$ [%]",
#     rng=(-0.25, 0.75),
#     output=outputs[f"{kiddyn.key}"],
#     cmap=cmap + "_r",
#     figsize=figsize,
# )
# savename = binpath / "kid1d_supersat.png"
# plt.savefig(savename, bbox_inches="tight")
