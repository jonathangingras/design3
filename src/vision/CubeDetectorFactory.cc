#include <vision/CubeDetectorFactory.h>

namespace d3t12 {

CubeDetector::Ptr CubeDetectorFactory::createCubeDetector(std::string colorString, cvMatPtr image) {
	CubeDetector::Ptr detector;

	if(colorString == "black") {
		detector = CubeDetector::Ptr(new BlackCubeDetector(100));
	} else if (colorString == "white") {
		detector = CubeDetector::Ptr(new WhiteCubeDetector(100));
	} else {
		ColorFilter::Ptr colorFilter(new ColorFilter(palette->getColor(colorString)));
		detector = CubeDetector::Ptr(new ColoredCubeDetector(colorFilter));
	}

	detector->setInputImage(image);
	return detector;
}

}