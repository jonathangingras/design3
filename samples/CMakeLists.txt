add_executable(detect_color detect_color.cc)
target_link_libraries(detect_color ${VISION_LIBS})

add_executable(atlas_asker atlas_asker.cc)
target_link_libraries(atlas_asker ${REST_LIBS})