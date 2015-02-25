#include <driver/CameraCapturer.h>
#include <iostream>

namespace d3t12 {

std::string CameraCapturer::devicePathFromId(int deviceId) {
	std::ostringstream oss;
	oss << "/dev/video" << deviceId;
	return oss.str();
}

void CameraCapturer::deactivateWhiteBalance() {
	int param_value = 0;
	if(kiki_v4l2_get_parameter(&device_handle, V4L2_CID_AUTO_WHITE_BALANCE, &param_value)) {
		throw CameraCapturerException("could not get parameter V4L2_CID_HUE_AUTO");
	}
	
	if(param_value) {
		if(kiki_v4l2_set_parameter(&device_handle, V4L2_CID_AUTO_WHITE_BALANCE, 0)) {
			throw CameraCapturerException("could not set parameter V4L2_CID_HUE_AUTO");
		}
	}

	if(kiki_v4l2_get_parameter(&device_handle, V4L2_CID_AUTO_WHITE_BALANCE, &param_value)) {
		throw CameraCapturerException("could not get parameter V4L2_CID_HUE_AUTO");
	}

	if(param_value) {
		throw CameraCapturerException("White balance stays on");
	}
}

void CameraCapturer::setWhiteBalanceTemperature(int temp_value) {
	int param_value = 0;
	if(kiki_v4l2_get_parameter(&device_handle, V4L2_CID_WHITE_BALANCE_TEMPERATURE, &param_value)) {
		throw CameraCapturerException("could not get parameter V4L2_CID_WHITE_BALANCE_TEMPERATURE");
	}
	
	if(param_value != temp_value) {
		if(kiki_v4l2_set_parameter(&device_handle, V4L2_CID_WHITE_BALANCE_TEMPERATURE, temp_value)) {
			throw CameraCapturerException("could not set parameter V4L2_CID_WHITE_BALANCE_TEMPERATURE");
		}
	}

	if(kiki_v4l2_get_parameter(&device_handle, V4L2_CID_WHITE_BALANCE_TEMPERATURE, &param_value)) {
		throw CameraCapturerException("could not get parameter V4L2_CID_WHITE_BALANCE_TEMPERATURE");
	}

	if(param_value != temp_value) {
		std::ostringstream oss;
		oss << "White temperature stays on at: " << param_value << ", resetting parameter.";
		std::cerr << oss.str();
		if(kiki_v4l2_reset_parameter(&device_handle, V4L2_CID_WHITE_BALANCE_TEMPERATURE)) {
			throw CameraCapturerException("could not reset parameter V4L2_CID_WHITE_BALANCE_TEMPERATURE");
		}
	}
}

CameraCapturer::CameraCapturer(int deviceId, int width, int height, int whiteBalanceTemperature, bool _deactivateWhiteBalance) {
	imageSize.width = width;
	imageSize.height = height;

	std::string path = devicePathFromId(deviceId);

	if(kiki_v4l2_open_device(&device_handle, path.c_str(), 640, 480)) {
		throw CameraCapturerException("could not open device");
	}

	device_handle.image_treatment = &kiki_v4l2_YUV422toBGR888;

	setWhiteBalanceTemperature(whiteBalanceTemperature);
	if(_deactivateWhiteBalance) {
		deactivateWhiteBalance();
	}

	if(kiki_v4l2_turn_device_on(&device_handle)) {
		throw CameraCapturerException("could not turn on device");
	}
}

CameraCapturer::~CameraCapturer() {
	if(kiki_v4l2_turn_device_off(&device_handle)) {
		throw CameraCapturerException("could not turn off device");
	}
	if(kiki_v4l2_close_device(&device_handle)) {
		throw CameraCapturerException("could not clode device");
	}
}

bool CameraCapturer::checkMatrixDimensions(const cv::Mat& matrix) {
	if(matrix.dims != 2 
		|| matrix.cols != imageSize.width 
		|| matrix.rows != imageSize.height
		|| matrix.elemSize() != 3
	) {
		return false;
	}
	return true;
}

void CameraCapturer::operator >> (cv::Mat& output) {
	if(!checkMatrixDimensions(output)) {
		output = cv::Mat(imageSize.height, imageSize.width, CV_8UC3, cv::Scalar(0));
	}
	if(kiki_v4l2_capture_frame(&device_handle, output.data)) {
		throw CameraCapturerException("could not capture frame");
	}
}

}
