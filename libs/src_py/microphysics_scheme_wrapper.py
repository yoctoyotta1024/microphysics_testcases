'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: microphysics_scheme_wrapper.py
Project: src_py
Created Date: Wednesday 28th February 2024
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
wrapper function for an instance of MicrophysicsScheme so it can be used by generic test cases
and run scripts
'''


from microphysics_scheme import MicrophysicsScheme

class MicrophysicsSchemeWrapper:
  """A class wrapping around Python MicrophysicsScheme for compatibility purposes"""

  def __init__(self, nvec, ke, ivstart, dz, qnc):
    """Init the MicrophysicsScheme object """

    self.nvec = nvec
    self.ke = ke
    self.ivstart = ivstart
    self.dz = dz
    self.qnc = qnc
    self.microphys = MicrophysicsScheme()

  def initialize(self):

    self.microphys.initialize()

  def finalize(self):

    self.microphys.finalize()

  def run(self, timestep, thermo):

   dt = timestep
   t = thermo.temp
   rho = thermo.rho
   p = thermo.press
   qv, qc, qi, qr, qs, qg = thermo.massmix_ratios

   t, qv, qc, qi, qr, qs, qg, prr_gsp, pflx = self.microphys.run(self.nvec, self.ke, self.ivstart,
                                                                 dt, self.dz, t, rho,
                                                                 p, qv, qc, qi, qr, qs, qg, self.qnc)

   thermo.temp = t
   thermo.massmix_ratios = [qv, qc, qi, qr, qs, qg]

   return thermo
