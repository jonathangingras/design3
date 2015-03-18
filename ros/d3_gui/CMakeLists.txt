cmake_minimum_required(VERSION 2.8.3)
project(d3_gui)

include(${CMAKE_SOURCE_DIR}/design3/design3team12.cmake)

find_package(
	catkin 
	REQUIRED 
	COMPONENTS 
	geometry_msgs 
	roscpp 
	std_msgs 
	tf
)

find_package(Qt4 COMPONENTS QtCore QtGui QtDeclarative QtOpenGL REQUIRED)
include(${QT_USE_FILE})

include_directories(
	include
	${catkin_INCLUDE_DIRS}
	${DESIGN3_INCLUDE_DIRS}
)

link_directories(
	${DESIGN3_LIBRARY_DIRS}
)

catkin_package(
	CATKIN_DEPENDS 
	geometry_msgs 
	roscpp 
	rospy 
	std_msgs 
	tf
)

#Qt stuff
 set(SOURCES
     src/base_station_gui.cc
     src/RosQtExitGuard.cc
     src/QmlApplicationViewer.cc
 )
 set(HEADERS
     include/QmlApplicationViewer.h
 )
 set(MOCS 
     include/QmlApplicationViewer.h
 )
# 
 set(UIS )
 set(RESOURCES )
# 
 qt4_add_resources(GENERATED_SOURCES ${RESOURCES})
 qt4_wrap_cpp(GENERATED_SOURCES ${MOCS})
# 
 source_group("Generated Sources - Do Not Edit" FILES ${GENERATED_SOURCES})
 include_directories("${CMAKE_BINARY_DIR}")
#end Qt stuff

add_executable( base_station_gui
	${SOURCES}
    ${GENERATED_SOURCES}
	${HEADERS}
    ${UIS}
    ${MOCS}
    ${RESOURCES}
)

target_link_libraries( base_station_gui
	${catkin_LIBRARIES} 
	${DESIGN3_LIBS}
	
	${QT_LIBRARIES}
	${Boost_LIBRARIES}
	boost_system
	boost_thread
)