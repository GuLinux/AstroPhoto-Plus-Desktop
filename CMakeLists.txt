cmake_minimum_required(VERSION 3.5.1)
project(AstroPhotoPlus-Desktop VERSION 0.1.0)

include(cmake/SetProjectVersion.cmake)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set (CMAKE_CXX_STANDARD 14)
# Turn on automatic invocation of the MOC, UIC & RCC
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

# Make this a GUI application on Windows
if(WIN32)
  set(CMAKE_WIN32_EXECUTABLE ON)
  set(CMAKE_INSTALL_UCRT_LIBRARIES TRUE)
  include(InstallRequiredSystemLibraries)
endif()

find_package(Qt5 5.6 REQUIRED COMPONENTS Core Widgets WebEngineWidgets Multimedia)

add_subdirectory(src)

