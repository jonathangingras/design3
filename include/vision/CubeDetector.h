#ifndef _CUBEDETECTOR_H_
#define _CUBEDETECTOR_H_

#include <vision/visionEssentials.h>

namespace d3t12 {

class CubeDetector {
protected:
	cvMatPtr sourceImage;

public:
	typedef boost::shared_ptr<CubeDetector> Ptr;

	virtual ~CubeDetector();

	virtual cv::Rect detectCube() = 0;

	inline void setInputImage(cvMatPtr image) {
		sourceImage = image;
	}
};

}

#endif