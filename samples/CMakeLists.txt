add_executable(detect_color detect_color.cc)
target_link_libraries(detect_color ${D3_VISION_LIBS})

add_executable(detect_color_live detect_color_live.cc)
target_link_libraries(detect_color_live ${D3_VISION_LIBS} pthread)

add_executable(atlas_asker atlas_asker.cc)
target_link_libraries(atlas_asker ${D3_REST_LIBS})

add_executable(harris_example harris.cc)
target_link_libraries(harris_example ${Boost_LIBRARIES} pthread boost_thread ${D3_VISION_LIBS})

add_executable(color_detector color_detector.cc)
target_link_libraries(color_detector ${Boost_LIBRARIES} pthread boost_thread ${D3_VISION_LIBS})

add_executable(detect_cube detect_cube.cc)
target_link_libraries(detect_cube ${Boost_LIBRARIES} pthread boost_thread ${D3_VISION_LIBS} ${D3_COMMON_LIBS} ${D3_DRIVER_LIBS})

add_executable(motor_adjust motor_adjust.cc)
target_link_libraries(motor_adjust ${Boost_LIBRARIES} pthread boost_thread ${DESIGN3_LIBS})

add_executable(cube_targeter cube_targeter.cc)
target_link_libraries(cube_targeter ${Boost_LIBRARIES} pthread boost_thread ${DESIGN3_LIBS})

add_executable(capture_frame capture_frame.cc)
target_link_libraries(capture_frame ${D3_VISION_LIBS} ${D3_COMMON_LIBS} ${D3_DRIVER_LIBS})

add_executable(sample_squares sample_squares.cc)
target_link_libraries(sample_squares ${D3_VISION_LIBS} ${D3_COMMON_LIBS} ${D3_DRIVER_LIBS})

add_executable(ledSample ledSample.cc)
target_link_libraries(ledSample ${D3_VISION_LIBS} ${D3_COMMON_LIBS} ${D3_DRIVER_LIBS})

#next one is only for an example on shared pointers
add_executable(shared_ptr_howto shared_ptr_howto.cc)
target_link_libraries(shared_ptr_howto ${Boost_LIBRARIES})

add_executable(serial_populu serial_populu.cc)