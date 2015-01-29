cmake_minimum_required (VERSION 2.8)

project(design3team12)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set(SRC ${CMAKE_SOURCE_DIR}/src)

set(CV_LIBS opencv_core opencv_imgproc opencv_highgui)

find_package(CURL)
IF(CURL_FOUND)
  MESSAGE(STATUS "Curl libraries found at: ${CURL_LIBRARIES}")
  MESSAGE(STATUS "Curl includes found at: ${CURL_INCLUDE_DIRS}")
else()
  MESSAGE(SEND_ERROR "Could not find cURL on your system")
ENDIF(CURL_FOUND)

include_directories(${CMAKE_SOURCE_DIR}/include)

set(VISION_LIBS ${CV_LIBS} jansson d3t12_vision)
set(REST_LIBS curl jansson d3t12_rest)


add_subdirectory(${SRC})
add_subdirectory(samples)
