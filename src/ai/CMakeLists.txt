add_library(d3t12_ai
	CubePositionFinder.cc
	JourneyStates.cc
	JourneyStateFactory.cc
	PathPlanner.cc
)

target_link_libraries(d3t12_ai
	${DESIGN3_LIBS}
)