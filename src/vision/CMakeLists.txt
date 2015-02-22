add_library(d3t12_vision
	Color.cc
	ColorFilter.cc
	ColorJSONLoader.cc
	ColorPalette.cc
	SquareFilter.cc
	IncrementalRect.cc
	CubeDetector.cc
	ColoredCubeDetector.cc
	BlackCubeDetector.cc
	WhiteCubeDetector.cc
	CubeDetectorFactory.cc
)

target_link_libraries(d3t12_vision
	${D3_VISION_LIBS}
)
