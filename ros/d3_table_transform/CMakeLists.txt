cmake_minimum_required(VERSION 2.8.3)
project(d3_table_transform)

include(${CMAKE_SOURCE_DIR}/design3/design3team12.cmake)

find_package(
	catkin 
	REQUIRED 
	COMPONENTS 
	geometry_msgs 
	roscpp 
	std_msgs 
	message_generation
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

add_message_files(
  FILES
  robotPose.msg
)

generate_messages(
  DEPENDENCIES
)

catkin_package(
	CATKIN_DEPENDS 
	geometry_msgs 
	roscpp 
	rospy 
	std_msgs
	message_runtime
	tf
)

set(D3_TF_SOURCE
	src/RosExitGuard.cc
	src/TfPublisher.cc
)

add_executable( table_origin_broadcaster
	src/table_origin_broadcaster.cc
	${D3_TF_SOURCE}
)
target_link_libraries( table_origin_broadcaster 
	${catkin_LIBRARIES} 
	${DESIGN3_LIBS}
)

add_executable( robot_center_broadcaster
	src/robot_center_broadcaster.cc
	${D3_TF_SOURCE}
)
target_link_libraries( robot_center_broadcaster 
	${catkin_LIBRARIES} 
	${DESIGN3_LIBS}
)

add_executable( robot_positioner
	src/robot_positioner.cc
	${D3_TF_SOURCE}
)
target_link_libraries( robot_positioner 
	${catkin_LIBRARIES} 
	${DESIGN3_LIBS}
)