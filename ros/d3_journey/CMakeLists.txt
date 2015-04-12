cmake_minimum_required(VERSION 2.8.3)
project(d3_journey)

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

add_executable( journey
	src/journey.cc
)

target_link_libraries( journey
	${catkin_LIBRARIES} 
	
	${DESIGN3_LIBS}
	
	${Boost_LIBRARIES}
	boost_system
	boost_thread
	jansson
	curl
)