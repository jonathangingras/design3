add_library(d3t12_ai
	CubePositionFinder.cc
)

target_link_libraries(d3t12_ai
	${D3_AI_LIBS}
)