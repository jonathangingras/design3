add_library(d3t12_common
	SIGINTHandler.cc
	ExitGuard.cc
	SystemCaller.cc
)

target_link_libraries(d3t12_common
	${D3_COMMON_LIBS}
)