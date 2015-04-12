add_executable(showgif
	showgif.cc
)

target_link_libraries(showgif
	nsgif_decode
	${D3_VISION_LIBS}
	${JANSSON_LIBS}
	${Boost_LIBRARIES}
	boost_filesystem
	boost_system
	boost_regex
)