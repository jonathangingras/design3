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

add_executable(capture_frame capture_frame.cc)
target_link_libraries(capture_frame ${D3_VISION_LIBS} ${D3_COMMON_LIBS} ${D3_DRIVER_LIBS})

add_executable(sample_squares sample_squares.cc)
target_link_libraries(sample_squares ${D3_VISION_LIBS} ${D3_COMMON_LIBS} ${D3_DRIVER_LIBS})


#next one is only for an example on shared pointers
add_executable(shared_ptr_howto shared_ptr_howto.cc)
target_link_libraries(shared_ptr_howto ${Boost_LIBRARIES})
