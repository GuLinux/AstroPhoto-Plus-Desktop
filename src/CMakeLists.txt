add_subdirectory(resources)
set(ASTROPHOTOPLUS_SOURCES
   main.cpp
   mainwindow.cpp
   mainwindow.ui
   serverdiscovery.cpp
   customwebpage.cpp
   api.cpp
   astrophotopluswidget.cpp
   notifications.cpp
   settings.cpp
   notification.ui
   ${ASTROPHOTOPLUS_RESOURCES}
)
   
if(CMAKE_SYSTEM_NAME STREQUAL Darwin)
    set(BIN_DESTINATION_PATH /)
    set(astrophotoplus_ICON ${CMAKE_CURRENT_BINARY_DIR}/resources/AstroPhoto-Plus.icns)
    set_source_files_properties(${astrophotoplus_ICON} PROPERTIES MACOSX_PACKAGE_LOCATION "Resources")

elseif(CMAKE_SYSTEM_NAME STREQUAL Windows)
    set(BIN_DESTINATION_PATH bin)
    set(ASTROPHOTOPLUS_SOURCES ${ASTROPHOTOPLUS_SOURCES} ${CMAKE_CURRENT_SOURCE_DIR}/resources/icon.rc)
else()
    set(BIN_DESTINATION_PATH bin)
endif()
add_executable(${PROJECT_NAME} MACOSX_BUNDLE ${astrophotoplus_ICON} ${ASTROPHOTOPLUS_SOURCES})
target_link_libraries(${PROJECT_NAME} Qt5::Widgets Qt5::WebEngineWidgets Qt5::Multimedia)

install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION ${BIN_DESTINATION_PATH} BUNDLE DESTINATION /)
