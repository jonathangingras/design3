include_directories(${CMAKE_CURRENT_LIST_DIR}/include)
link_directories(${CMAKE_CURRENT_LIST_DIR}/lib)
set( D3_TEST_LIBS 
	gtest
	gtest_main
	gmock
	gmock_main
	pthread
	${DESIGN3_LIBS}
)

function(add_design3_test test_name)
	add_executable( ${test_name}
		${test_name}.cc
	)
	target_link_libraries( ${test_name}
		${D3_TEST_LIBS}
	)
endfunction(add_design3_test)

#rest
add_design3_test(CURLGetterTest)

#vision
add_design3_test(AtlasJSONDecoderTest)
add_design3_test(ColorJSONLoaderTest)
add_design3_test(ColorPaletteTest)
add_design3_test(IncrementalRectTest)
add_design3_test(ColoredCubeDetectorTest)
add_design3_test(CubeCenterTargeterTest)

#driver
add_design3_test(MicroControllerCommandBuilderTest)
add_design3_test(ServoMotorControllerTest)
add_design3_test(LEDMatrixControllerTest)

#ai
add_design3_test(CubePositionFinderTest)
add_design3_test(JourneySchedulerTest)
add_design3_test(JourneyStatesTest)