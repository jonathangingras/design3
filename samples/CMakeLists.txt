add_executable(detect_color detect_color.cc)
target_link_libraries(detect_color ${VISION_LIBS})

add_executable(atlas_asker atlas_asker.cc)
target_link_libraries(atlas_asker ${REST_LIBS})

#next one is only for an example on shared pointers
add_executable(shared_ptr_howto shared_ptr_howto.cc)
target_link_libraries(shared_ptr_howto boost_container)