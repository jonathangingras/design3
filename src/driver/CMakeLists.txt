add_library(d3t12_driver
	kiki_v4l2_mmap_capture.c
	yuv422_to_bgr888.c
	yuv422_to_rgb888.c

	CameraCapturer.cc

	MicroControllerCommand.cc
	MicroControllerCommandBuilder.cc
	MicroControllerCommandPort.cc
)

target_link_libraries(d3t12_driver
	${D3_DRIVER_LIBS}
)