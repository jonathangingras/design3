#include <vision/NoCubeFoundException.h>
#include <vision/CubeTopTargeter.h>

namespace d3t12 {

static inline cv::Point rectCenter(const cv::Rect& rect) {
	return cv::Point(rect.x + rect.width/2, rect.y + rect.height/2);
}

static inline bool pointXInRect(const cv::Point& point, const cv::Rect& rect) {
	return point.x >= rect.x && point.x <= rect.x + rect.width;
}

static inline bool pointYInRect(const cv::Point& point, const cv::Rect& rect) {
	return point.y >= rect.y && point.y <= rect.y + rect.height;
}

static inline bool pointInRect(const cv::Point& point, const cv::Rect& rect) {
	return pointXInRect(point, rect) && pointYInRect(point, rect);
}

static inline bool noDetection(const cv::Rect& cubeRect) {
	return cubeRect.width == 0 || cubeRect.height == 0;
}

void CubeTopTargeter::targetCenter() {
	if(!detector.get()) {
		std::cerr << "detector is null!!" << std::endl;
	}

	cv::Rect rect;
	cv::Point imageCenter;

	do {
		capturer->capture();
		rect = detector->detectCube();
		if( noDetection( rect ) ) throw NoCubeFoundException("targetCenter: could not find cube!");
		rect.height = 5;
		imageCenter = targetParameters.centerTarget;
		macroAdjust(imageCenter, rect);
	} while(!pointInRect(imageCenter, rect));

	do {
		capturer->capture();
		rect = detector->detectCube();
		if( noDetection( rect ) ) throw NoCubeFoundException("targetCenter: could not find cube!");
		rect.height = 5;
		imageCenter = targetParameters.centerTarget;
		microAdjust(imageCenter, rect);
	} while(needMicroAdjust(imageCenter, rect));
}

} //d3t12