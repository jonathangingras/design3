cmake_minimum_required(VERSION 2.8.3)
project(d3_color_detector)

find_package(catkin REQUIRED COMPONENTS
  pcl_conversions
  pcl_ros
  roscpp
  sensor_msgs
  std_msgs
  pcl_msgs
  cv_bridge
)

find_package( PCL REQUIRED )
find_package( OpenCV REQUIRED )

include(${CMAKE_SOURCE_DIR}/design3/design3team12.cmake)

include_directories(
	${DESIGN3_INCLUDE_DIRS}
	${catkin_INCLUDE_DIRS}
	${PCL_INCLUDE_DIRS}
	${OpenCV_INCLUDE_DIRS}
)

link_directories(
	${DESIGN3_LIBRARY_DIRS}
	${PCL_LIBRARY_DIRS}
	${OpenCV_DIRS}
)

add_definitions(
	${PCL_DEFINITIONS}
)

catkin_package(
	CATKIN_DEPENDS message_runtime
)

add_executable( color_detector
	src/color_detector.cc
)

target_link_libraries( color_detector
	${DESIGN3_LIBS}
	${catkin_LIBRARIES}
	${PCL_LIBRARIES}
	${OpenCV_LIBRARIES}
)
