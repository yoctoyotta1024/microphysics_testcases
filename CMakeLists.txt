cmake_minimum_required(VERSION 3.18.0)
project(project
  LANGUAGES CXX
  DESCRIPTION "Microphysics Test Cases by Clara Bayley and other developers"
  VERSION 0.0.0
)

# # Add the location of pybind11Config.cmake to the CMake module path
# list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/path/to/pybind11Config.cmake")

# Use the pybind11 package from .gitmodules
add_subdirectory(extern/pybind11)

# Define the C++ source files
set(SOURCES libs/src_cxx/mock.cpp)

# Create the Python extension module
pybind11_add_module(mock_cxx MODULE ${SOURCES})

# Link any necessary libraries (if needed)
target_link_libraries(mock_cxx PRIVATE pybind11::module)

# Set additional compile options if needed
# target_compile_options(mock PRIVATE -Wall -Wextra)

# Optionally install the Python extension module
# install(TARGETS mock LIBRARY DESTINATION "${CMAKE_INSTALL_PREFIX}")

set_target_properties(mock_cxx PROPERTIES
  CMAKE_CXX_STANDARD_REQUIRED ON
  CMAKE_CXX_EXTENSIONS ON
  CXX_STANDARD 20)
