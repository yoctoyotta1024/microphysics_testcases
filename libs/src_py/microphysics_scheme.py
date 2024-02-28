'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: microphysics_scheme.py
Project: src_py
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
class for mock microphysics scheme in Python
'''


import numpy as np

class MicrophysicsScheme:
  """A class representing a Python mock microphysics scheme."""

  def __init__(self):
    """Init the MicrophysicsScheme object (Python only) """

    self.name = "Python Mock Microphysics Instance"

  def initialize(self):
    """Initialize the microphysics scheme.

    This method performs the initialization steps necessary for the microphysics scheme.

    Returns:
        int: 0 upon successful initialization.
    """

    print("microphysics initialisation")

    return 0

  def finalize(self):
    """Finalize the microphysics scheme.

    This method performs the finalization steps for the microphysics scheme.

    Returns:
        int: 0 upon successful finalization.
    """

    print("microphysics finalisation")

    return 0

  def run(self, nvec, ke, ivstart, dt, dz, t, rho, p, qv, qc, qi, qr, qs, qg, qnc, prr_gsp, pflx):
    """Run the microphysics computations.

    This method executes the microphysics computations.

    Parameters:
        i (int): Some parameter to be used in the computations.

    Returns:
        int: Result of the computations, i + 1.
    """

    print("run microphysics")

    return t, qv, qc, qi, qr, qs, qg, prr_gsp, pflx
