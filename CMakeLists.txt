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

if(CMAKE_SYSTEM_NAME STREQUAL Darwin)
	set(CMAKE_INSTALL_PREFIX "")
	set(MACOSX_BUNDLE_BUNDLE_NAME "AstroPhoto Plus")
	set(MACOSX_BUNDLE_BUNDLE_VERSION "${${PROJECT_NAME}_VERSION}")
	set(MACOSX_BUNDLE_GUI_IDENTIFIER "net.gulinux.astrophotoplus-desktop")
	set(MACOSX_BUNDLE_ICON_FILE AstroPhoto-Plus.icns)
	message("Automatically crating MACOSX Bundle")
endif()
# 	SET(CPACK_PACKAGE_DESCRIPTION_SUMMARY "AstroPhoto Plus desktop client")
# 	SET(CPACK_PACKAGE_VENDOR "GuLinux <marco@gulinux.net>")
# 	SET(CPACK_PACKAGE_DESCRIPTION_FILE "${CMAKE_SOURCE_DIR}/README.md")
# 	#SET(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_SOURCE_DIR}/src/")
# 	SET(CPACK_PACKAGE_VERSION_MAJOR "${${PROJECT_NAME}_VERSION_MAJOR}")
# 	SET(CPACK_PACKAGE_VERSION_MINOR "${${PROJECT_NAME}_VERSION_MINOR}")
# 	SET(CPACK_PACKAGE_VERSION_PATCH "${${PROJECT_NAME}_VERSION_PATCH}${${PROJECT_NAME}_VERSION_TWEAK}")
# 	set(CPACK_PACKAGE_FILE_NAME PlanetaryImager-${FULL_VERSION}-${PACKAGE_SYSTEM_NAME}-${PlanetaryImager_ARCH}${PACKAGE_NAME_SUFFIX})
# 	SET(CPACK_PACKAGE_CONTACT "marco@gulinux.net")
# 	set(CPACK_SET_DESTDIR On)
# 
# 	SET(CPACK_GENERATOR Bundle)
# 	SET(CPACK_BUNDLE_NAME "AstroPhoto Plus Desktop")
# 	INCLUDE(CPack)
# endif()
