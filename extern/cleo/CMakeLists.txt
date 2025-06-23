# set cmake version
if(NOT DEFINED CMAKE_MINIMUM_REQUIRED_VERSION)
  cmake_minimum_required(VERSION 3.18.0)
endif()

# fetch and make cleo library available
include(FetchContent)
FetchContent_Declare(
  cleo
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  URL https://github.com/yoctoyotta1024/CLEO/archive/refs/tags/v0.44.0.zip
  GIT_TAG bf7edc9391cfe027d3bff5436629b90a311ff4c8
)
FetchContent_MakeAvailable(cleo)

message(STATUS "CLEO version v0.44.0, installation in: ${CLEO_BINARY_DIR}")
