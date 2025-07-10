# set cmake version
if(NOT DEFINED CMAKE_MINIMUM_REQUIRED_VERSION)
  cmake_minimum_required(VERSION 3.18.0)
endif()

# fetch and make cleo library available
include(FetchContent)
FetchContent_Declare(
  cleo
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  URL https://github.com/yoctoyotta1024/CLEO/archive/refs/tags/v0.47.0.zip
  GIT_TAG 2691853256e7449f9d5bb1469e2c30fda1d3e429
)
FetchContent_MakeAvailable(cleo)

message(STATUS "CLEO version v0.47.0, installation in: ${CLEO_BINARY_DIR}")
