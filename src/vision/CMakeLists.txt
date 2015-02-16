add_library(d3t12_vision
	Color.cc
	ColorFilter.cc
	ColorJSONLoader.cc
	ColorPalette.cc
	SquareFilter.cc
)

target_link_libraries(d3t12_vision
	${D3_VISION_LIBS}
)
