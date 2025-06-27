# set cmake version
if(NOT DEFINED CMAKE_MINIMUM_REQUIRED_VERSION)
  cmake_minimum_required(VERSION 3.18.0)
endif()

# fetch and make cleo library available
include(FetchContent)
FetchContent_Declare(
  cleo
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  URL https://github.com/yoctoyotta1024/CLEO/archive/refs/tags/v0.44.3.zip
  GIT_TAG 283a5d4fe2c39f404f0ddcd4eebd40b17a8cbd25
)
FetchContent_MakeAvailable(cleo)

message(STATUS "CLEO version v0.44.3, installation in: ${CLEO_BINARY_DIR}")
