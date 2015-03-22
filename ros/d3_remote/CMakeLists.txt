cmake_minimum_required(VERSION 2.8.3)
project(d3_remote)

include(${CMAKE_SOURCE_DIR}/design3/design3team12.cmake)

find_package(
	catkin 
	REQUIRED 
	COMPONENTS 
	geometry_msgs 
	roscpp 
	std_msgs
	tf
	d3_table_transform
)

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
	d3_table_transform
)

set(PKG_SOURCE
	src/remote.cc
)

add_executable( robot_remote
	${PKG_SOURCE}
)
target_link_libraries( robot_remote 
	${catkin_LIBRARIES} 
	${DESIGN3_LIBS}
)