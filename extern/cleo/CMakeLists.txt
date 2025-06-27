# set cmake version
if(NOT DEFINED CMAKE_MINIMUM_REQUIRED_VERSION)
  cmake_minimum_required(VERSION 3.18.0)
endif()

# fetch and make cleo library available
include(FetchContent)
FetchContent_Declare(
  cleo
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
  URL https://github.com/yoctoyotta1024/CLEO/archive/refs/tags/v0.44.4.zip
  GIT_TAG f4283f4e4941b01e78eab33e1029383b08383b5f
)
FetchContent_MakeAvailable(cleo)

message(STATUS "CLEO version v0.44.4, installation in: ${CLEO_BINARY_DIR}")
