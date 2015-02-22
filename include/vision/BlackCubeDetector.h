#ifndef _BLACKCUBEDETECTOR_H_
#define _BLACKCUBEDETECTOR_H_

#include <vision/CubeDetector.h>
#include <vision/ColorFilter.h>
#include <vision/IncrementalRect.h>
#include <vision/SquareFilter.h>

namespace d3t12 {

class BlackCubeDetector : public CubeDetector {
private:
	int threshold;

	inline BlackCubeDetector(int _threshold): threshold(_threshold) {}
	friend class CubeDetectorFactory;

public:
	virtual cv::Rect detectCube();

	virtual ~BlackCubeDetector();
};

}

#endif