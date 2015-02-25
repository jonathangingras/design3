cmake_minimum_required(VERSION 2.8.3)
project(d3_robot_cam_broadcaster)

include(${CMAKE_SOURCE_DIR}/design3/design3team12.cmake)

find_package(
	catkin 
	REQUIRED 
	COMPONENTS 
	geometry_msgs 
	roscpp 
	image_transport
	cv_bridge
	std_msgs 
	tf
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
	image_transport
	cv_bridge
	std_msgs 
	tf
)

add_executable( robot_cam_broadcaster
	src/robot_cam_broadcaster.cc
)
target_link_libraries( robot_cam_broadcaster 
	${catkin_LIBRARIES} 
	${DESIGN3_LIBS}
)