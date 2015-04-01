#ifndef _CUBEDETECTORFACTORY_H_
#define _CUBEDETECTORFACTORY_H_

#include <vision/visionEssentials.h>
#include <vision/ColorPalette.h>
#include <vision/CubeDetector.h>
#include <vision/ColoredCubeDetector.h>
#include <vision/WhiteCubeDetector.h>
#include <vision/BlackCubeDetector.h>

namespace d3t12 {

class CubeDetectorFactory {
protected:
	ColorPalette::Ptr palette;

public:
	typedef boost::shared_ptr<CubeDetectorFactory> Ptr;
	inline CubeDetectorFactory(ColorPalette::Ptr _palette): palette(_palette) {}

	virtual CubeDetector::Ptr createCubeDetector(std::string colorString, cvMatPtr image);
};

}

#endif