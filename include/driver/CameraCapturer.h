#ifndef _D3T12_CAMERACAPTURER_H_
#define _D3T12_CAMERACAPTURER_H_

#include <opencv2/opencv.hpp>
#include <driver/kiki_v4l2_api.h>
#include <driver/CameraCapturerException.h>

namespace d3t12 {

class CameraCapturer {
private:
	device_handle_t device_handle;
	image_size_t imageSize;

	std::string devicePathFromId(int deviceId);
	void deactivateWhiteBalance();
	void setWhiteBalanceTemperature(int);

	bool checkMatrixDimensions(const cv::Mat& matrix);

public:
	CameraCapturer(int deviceId, int width = 640, int height = 480,
		int whiteBalanceTemperature = 0, bool _deactivateWhiteBalance = true);
	
	~CameraCapturer();

	void operator >> (cv::Mat& output);
};

}

#endif
