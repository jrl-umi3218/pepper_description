cmake_minimum_required(VERSION 2.8.3)
project(pepper_description)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS xacro)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

catkin_package(
    SKIP_PKG_CONFIG_GENERATION
    CATKIN_DEPENDS xacro mc_rbdyn_urdf
)

# Configure the develspace pkg-config file
set(DATADIR "${PROJECT_SOURCE_DIR}")
configure_file(
  "${PROJECT_SOURCE_DIR}/${PROJECT_NAME}.pc.cmake"
  "${CATKIN_DEVEL_PREFIX}/lib/pkgconfig/${PROJECT_NAME}.pc")

# Configure the installspace pkg-config file
set(DATADIR "${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}")
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/catkin_generated/installspace)
configure_file(
  "${PROJECT_SOURCE_DIR}/${PROJECT_NAME}.pc.cmake"
  "${CMAKE_CURRENT_BINARY_DIR}/catkin_generated/installspace/${PROJECT_NAME}.pc")
install(
  FILES ${CMAKE_CURRENT_BINARY_DIR}/catkin_generated/installspace/${PROJECT_NAME}.pc
  DESTINATION lib/pkgconfig)

# Generate URDF models???


catkin_python_setup()

# Instructions to install launch files
install(DIRECTORY launch/
     DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch)

# Instructions to install config files
install(DIRECTORY config/
     DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config)

# Instructions to install launch files
install(DIRECTORY urdf/
     DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf)

install(DIRECTORY meshes/
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/meshes)
