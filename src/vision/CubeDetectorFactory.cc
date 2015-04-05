#include <vision/CubeDetectorFactory.h>

namespace d3t12 {

CubeDetector::Ptr CubeDetectorFactory::createCubeDetector(std::string colorString, cvMatPtr image) {
	CubeDetector::Ptr detector;

	if(colorString == "black") {
		detector = CubeDetector::Ptr(new BlackCubeDetector(100));
	} else if (colorString == "white") {
		detector = CubeDetector::Ptr(new WhiteCubeDetector(100));
	} else if (colorString == "red") {
		ColorFilter::Ptr colorFilter1(new ColorFilter(palette->getColor("red1")));
		ColorFilter::Ptr colorFilter2(new ColorFilter(palette->getColor("red2")));
		detector = CubeDetector::Ptr(new RedCubeDetector(colorFilter1, colorFilter2));
	} else {
		ColorFilter::Ptr colorFilter(new ColorFilter(palette->getColor(colorString)));
		detector = CubeDetector::Ptr(new ColoredCubeDetector(colorFilter));
	}

	detector->setInputImage(image);
	return detector;
}

}