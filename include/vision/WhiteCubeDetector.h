#ifndef _WHITECUBEDETECTOR_H_
#define _WHITECUBEDETECTOR_H_

#include <vision/CubeDetector.h>
#include <vision/ColorFilter.h>
#include <vision/IncrementalRect.h>

namespace d3t12 {

class WhiteCubeDetector : public CubeDetector {
private:
	int threshold;

	inline WhiteCubeDetector(int _threshold): threshold(_threshold) {}
	friend class CubeDetectorFactory;

public:
	virtual cv::Rect detectCube();

	virtual ~WhiteCubeDetector();
};

}

#endif