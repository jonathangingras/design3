#ifndef _REDCUBEDETECTOR_H_
#define _REDCUBEDETECTOR_H_

#include <vision/CubeDetector.h>
#include <vision/ColorFilter.h>
#include <vision/IncrementalRect.h>

namespace d3t12 {

class RedCubeDetector : public CubeDetector {
private:
	ColorFilter::Ptr filter1, filter2; //names are not ugly, it's just that red needs 2 filters

	inline RedCubeDetector(ColorFilter::Ptr _filter1, ColorFilter::Ptr _filter2): 
		filter1(_filter1), filter2(_filter2) {}
	friend class CubeDetectorFactory;

public:
	virtual cv::Rect detectCube();

	virtual ~RedCubeDetector();
};

}

#endif