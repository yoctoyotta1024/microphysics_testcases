cmake_minimum_required(VERSION 3.18.0)
project(project
  LANGUAGES CXX
  DESCRIPTION "Microphysics Test Cases by Clara Bayley and other developers"
)

## Use the pybind11 package from .gitmodules
add_subdirectory(extern/pybind11)

## Create the Python extension module from C++ source files
set(SOURCES libs/src_mock_cxx/mock.cpp)
pybind11_add_module(mock_cxx MODULE ${SOURCES})

# ## Link any necessary libraries (if needed)
# target_link_libraries(mock_cxx PRIVATE pybind11::module)

# ## Set additional compile options if needed
# target_compile_options(mock_cxx PRIVATE -Wall -Wextra)

set_target_properties(mock_cxx PROPERTIES
  CXX_STANDARD 20
  CMAKE_CXX_STANDARD_REQUIRED ON
  CMAKE_CXX_EXTENSIONS ON)
