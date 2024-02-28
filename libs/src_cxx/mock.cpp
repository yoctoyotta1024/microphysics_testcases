/*
 * Copyright (c) 2024 MPI-M, Clara Bayley
 *
 * ----- Microphysics Test Cases -----
 * File: mock.cpp
 * Project: src_cxx
 * Created Date: Wednesday 28th February 2024
 * Author: Clara Bayley (CB)
 * Additional Contributors:
 * -----
 * Last Modified: Wednesday 28th February 2024
 * Modified By: CB
 * -----
 * License: BSD 3-Clause "New" or "Revised" License
 * https://opensource.org/licenses/BSD-3-Clause
 * -----
 * File Description:
 * Implementation of pybind11 for binding mock C++ module to Python
 */


#include "mock.hpp"

PYBIND11_MODULE(mock, m) {
    m.doc() = "pybind11 example plugin";   // optional module docstring

    m.def("area_circle", &area_circle,
          "A function that calculates the area of a circle given its radius.");

    m.def("add", &add, "A function that adds two integers");
}
