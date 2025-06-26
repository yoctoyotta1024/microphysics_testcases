# set cmake version
if(NOT DEFINED CMAKE_MINIMUM_REQUIRED_VERSION)
  cmake_minimum_required(VERSION 3.18.0)
endif()

# fetch and make cleo library available
include(FetchContent)
FetchContent_Declare(
  cleo
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  URL https://github.com/yoctoyotta1024/CLEO/archive/refs/tags/v0.44.2.zip
  GIT_TAG 5dfbc88cf5b51b7a546f6fac76e1a5b6f4ada008
)
FetchContent_MakeAvailable(cleo)

message(STATUS "CLEO version v0.44.2, installation in: ${CLEO_BINARY_DIR}")
