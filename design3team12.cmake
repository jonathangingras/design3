set(D3_CV_LIBS opencv_core opencv_imgproc opencv_highgui)
set(D3_VISION_LIBS jansson ${D3_CV_LIBS} d3t12_vision)
set(D3_REST_LIBS curl jansson d3t12_rest)
set(DESIGN3_LIBS ${D3_VISION_LIBS} ${D3_REST_LIBS})

set(DESIGN3_INCLUDE_DIRS
	${CMAKE_CURRENT_LIST_DIR}/include
)

set(DESIGN3_LIBRARY_DIRS
	${CMAKE_CURRENT_LIST_DIR}/build/lib
)
