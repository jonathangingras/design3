#ifndef _CUBEDETECTORMOCK_H_
#define _CUBEDETECTORMOCK_H_

#include <vision/CubeDetector.h>

class CubeDetectorMock : public d3t12::CubeDetector {
public:
	MOCK_METHOD0(detectCube, cv::Rect(void));
};

#endif