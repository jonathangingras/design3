set(D3_CV_LIBS opencv_core opencv_imgproc opencv_highgui)
set(D3_VISION_LIBS jansson ${D3_CV_LIBS} d3t12_vision)
set(D3_REST_LIBS ${CURL_LIBRARIES} ${JANSSON_LIBRARIES} d3t12_rest)
set(D3_DRIVER_LIBS d3t12_driver)
set(D3_AI_LIBS d3t12_ai)
set(D3_COMMON_LIBS d3t12_common)

set(DESIGN3_LIBS ${D3_VISION_LIBS} ${D3_REST_LIBS} ${D3_DRIVER_LIBS} ${D3_AI_LIBS} ${D3_COMMON_LIBS})

set(DESIGN3_INCLUDE_DIRS
	${CMAKE_CURRENT_LIST_DIR}/include
	${CMAKE_CURRENT_LIST_DIR}/include/driver
	${CURL_INCLUDE_DIRS}
	${JANSSON_INCLUDE_DIRS}
	${CMAKE_CURRENT_LIST_DIR}/build/extern/jansson-2.7/include
	${CMAKE_CURRENT_LIST_DIR}/extern/nsgif/include
)

set(DESIGN3_LIBRARY_DIRS
	${CMAKE_CURRENT_LIST_DIR}/build/lib
	${CMAKE_CURRENT_LIST_DIR}/build/extern/jansson-2.7/lib
	${CMAKE_CURRENT_LIST_DIR}/build/extern/nsgif/lib
)
