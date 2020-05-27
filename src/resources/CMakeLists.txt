set(ASTROPHOTOPLUS_RESOURCES ${CMAKE_CURRENT_SOURCE_DIR}/resources.qrc CACHE INTERNAL "")
set(ASTROPHOTOPLUS_REPO_DIR "" CACHE STRING "AstroPhoto Plus main repository path (to copy/update resources)")
if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    foreach(res 16 32 48 64 72 96 256 512)
        if(ASTROPHOTOPLUS_REPO_DIR)
            execute_process(COMMAND ${CMAKE_COMMAND} -E copy_if_different ${CMAKE_SOURCE_DIR}/../frontend/public/icon-${res}.png ${CMAKE_CURRENT_SOURCE_DIR}/app-icon/appicon-${res}.png) 
        endif()
        install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/app-icon/appicon-${res}.png DESTINATION share/icons/hicolor/${res}x${res}/apps RENAME ${PROJECT_NAME}.png)
    endforeach()

    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/launcher.desktop.in ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.desktop)
    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.desktop DESTINATION share/applications)
endif()


if(CMAKE_SYSTEM_NAME STREQUAL Darwin)
    file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/AstroPhoto-Plus.iconset/)
    foreach(res 16 32 48 64 72 96 256)
        math(EXPR res_2x "${res} * 2")
        execute_process(COMMAND ${CMAKE_COMMAND} -E copy_if_different ${CMAKE_CURRENT_SOURCE_DIR}/app-icon/appicon-${res}.png    ${CMAKE_CURRENT_BINARY_DIR}/AstroPhoto-Plus.iconset/icon_${res}x${res}.png)
        execute_process(COMMAND ${CMAKE_COMMAND} -E copy_if_different ${CMAKE_CURRENT_SOURCE_DIR}/app-icon/appicon-${res_2x}.png ${CMAKE_CURRENT_BINARY_DIR}/AstroPhoto-Plus.iconset/icon_${res}x${res}@2x.png)
    endforeach()
    execute_process(COMMAND iconutil -c icns ${CMAKE_CURRENT_BINARY_DIR}/AstroPhoto-Plus.iconset)
endif()
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/version.env.in ${CMAKE_CURRENT_BINARY_DIR}/version.env)


