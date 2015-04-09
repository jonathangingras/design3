#include <vision/NoCubeFoundException.h>
#include <vision/CubeCenterTargeter.h>

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

void CubeCenterTargeter::macroAdjust(const cv::Point& imageCenter, const cv::Rect& rect) {
	if(!pointXInRect(imageCenter, rect)) {
		if(imageCenter.x <= rect.x) {
			adjuster->adjustX(targetParameters.macroUnit);
		} else {
			adjuster->adjustX(-targetParameters.macroUnit);
		}
	}
	if(!pointYInRect(imageCenter, rect)) {
		if(imageCenter.y <= rect.y) {
			adjuster->adjustY(-targetParameters.macroUnit);
		} else {
			adjuster->adjustY(targetParameters.macroUnit);
		}
	}
}

void CubeCenterTargeter::microAdjust(const cv::Point& imageCenter, const cv::Rect& rect) {
	cv::Point cubeCenter = rectCenter(rect);

	if(rect.width >= 5 && imageCenter.x - cubeCenter.x > rect.width*targetParameters.scaleFactor) {
		adjuster->adjustX(-targetParameters.microUnit);
	}
	if(rect.width >= 5 && cubeCenter.x - imageCenter.x > rect.width*targetParameters.scaleFactor) {
		adjuster->adjustX(targetParameters.microUnit);
	}

	if(rect.height >= 5 && imageCenter.y - cubeCenter.y > rect.height*targetParameters.scaleFactor) {
		adjuster->adjustY(targetParameters.microUnit);
	}
	if(rect.height >= 5 && cubeCenter.y - imageCenter.y > rect.height*targetParameters.scaleFactor) {
		adjuster->adjustY(-targetParameters.microUnit);
	}
}

bool CubeCenterTargeter::needMicroAdjust(const cv::Point& imageCenter, const cv::Rect& rect) {
	bool answer = false;
	cv::Point cubeCenter = rectCenter(rect);

	if(rect.width >= 5 && imageCenter.x - cubeCenter.x >= rect.width*targetParameters.scaleFactor) {
		answer = true;
	}
	if(rect.width >= 5 && cubeCenter.x - imageCenter.x >= rect.width*targetParameters.scaleFactor) {
		answer = true;
	}

	if(rect.height >= 5 && imageCenter.y - cubeCenter.y >= rect.height*targetParameters.scaleFactor) {
		answer = true;
	}
	if(rect.height >= 5 && cubeCenter.y - imageCenter.y >= rect.height*targetParameters.scaleFactor) {
		answer = true;
	}
	return answer;
}

static inline bool noDetection(const cv::Rect& cubeRect) {
	return cubeRect.width == 0 || cubeRect.height == 0;
}

void CubeCenterTargeter::resetAngle() {
	adjuster->resetAngle();
}

void CubeCenterTargeter::targetCenter() {
	if(!detector.get()) {
		std::cerr << "detector is null!!" << std::endl;
	}

	cv::Rect rect;
	cv::Point imageCenter;

	do {
		capturer->capture();
		rect = detector->detectCube();
		if( noDetection( rect ) ) throw NoCubeFoundException("targetCenter: could not find cube!");
		imageCenter = targetParameters.centerTarget;
		macroAdjust(imageCenter, rect);
	} while(!pointInRect(imageCenter, rect));

	do {
		capturer->capture();
		rect = detector->detectCube();
		if( noDetection( rect ) ) throw NoCubeFoundException("targetCenter: could not find cube!");
		imageCenter = targetParameters.centerTarget;
		microAdjust(imageCenter, rect);
	} while(needMicroAdjust(imageCenter, rect));
}

} //d3t12