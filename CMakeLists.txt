cmake_minimum_required(VERSION 3.5.1)

execute_process(COMMAND git rev-parse --short HEAD OUTPUT_VARIABLE COMMIT_ID WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
string(STRIP ${COMMIT_ID} COMMIT_ID)
execute_process(COMMAND git show -s --format=%ci ${COMMIT_ID} OUTPUT_VARIABLE COMMIT_DATE WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
string(REPLACE "-" "" COMMIT_DATE ${COMMIT_DATE})
string(SUBSTRING ${COMMIT_DATE} 0 8 COMMIT_DATE)


set(PROJECT_VERSION_SUFFIX _${COMMIT_DATE}-${COMMIT_ID})
project(AstroPhotoPlus-Desktop VERSION 0.1.0)

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
endif()

find_package(Qt5 5.6 REQUIRED COMPONENTS Core Widgets WebEngineWidgets Multimedia)

add_subdirectory(src)
