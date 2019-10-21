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
elseif(CMAKE_SYSTEM_NAME STREQUAL Windows)
    set(BIN_DESTINATION_PATH bin)
    set(ASTROPHOTOPLUS_SOURCES ${ASTROPHOTOPLUS_SOURCES} ${CMAKE_CURRENT_SOURCE_DIR}/resources/icon.rc)
else()
    set(BIN_DESTINATION_PATH bin)
endif()
add_executable(${PROJECT_NAME} ${ASTROPHOTOPLUS_SOURCES})
target_link_libraries(${PROJECT_NAME} Qt5::Widgets Qt5::WebEngineWidgets Qt5::Multimedia)

install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION ${BIN_DESTINATION_PATH})
