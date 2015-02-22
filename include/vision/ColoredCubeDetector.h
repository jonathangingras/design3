#ifndef _COLOREDCUBEDETECTOR_H_
#define _COLOREDCUBEDETECTOR_H_

#include <vision/CubeDetector.h>
#include <vision/ColorFilter.h>
#include <vision/IncrementalRect.h>

namespace d3t12 {

class ColoredCubeDetector : public CubeDetector {
private:
	ColorFilter::Ptr filter;

	inline ColoredCubeDetector(ColorFilter::Ptr _filter): filter(_filter) {}
	friend class CubeDetectorFactory;

public:
	virtual cv::Rect detectCube();

	virtual ~ColoredCubeDetector();
};

}

#endif