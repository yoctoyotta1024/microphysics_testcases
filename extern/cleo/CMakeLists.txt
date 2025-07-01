# set cmake version
if(NOT DEFINED CMAKE_MINIMUM_REQUIRED_VERSION)
  cmake_minimum_required(VERSION 3.18.0)
endif()

# fetch and make cleo library available
include(FetchContent)
FetchContent_Declare(
  cleo
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  URL https://github.com/yoctoyotta1024/CLEO/archive/refs/tags/v0.45.0.zip
  GIT_TAG 737964f8ea85914d7b73c28e0479d739fe2ea340
)
FetchContent_MakeAvailable(cleo)

message(STATUS "CLEO version v0.45.0, installation in: ${CLEO_BINARY_DIR}")
