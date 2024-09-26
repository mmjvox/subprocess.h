cmake_minimum_required(VERSION 3.5)
project(subprocess.h
    VERSION 1.0.0
    LANGUAGES CXX
    DESCRIPTION "single header process launching solution for C and C++")

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)


set(SUBPROCESS_HEADER_FILE
    subprocess.h
)


target_include_directories(${PROJECT_NAME} PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:include>)



file(GLOB_RECURSE SUBPROCESS_HEADERS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/*.h)

target_include_directories(subprocess PUBLIC include)


string(JOIN ";" SUBPROCESS_HEADERS_STRING ${SUBPROCESS_HEADERS})
set_target_properties(subprocess PROPERTIES
    PUBLIC_HEADER "${SUBPROCESS_HEADERS_STRING}"
)

include(GNUInstallDirs)

include(CMakePackageConfigHelpers)
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/subprocessConfig.cmake"
    INSTALL_DESTINATION
    ${CMAKE_INSTALL_LIBDIR}/cmake/subprocess
)

install(FILES ${SUBPROCESS_HEADERS}
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/subprocess)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/subprocessConfig.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/subprocess)
install(TARGETS subprocess
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

