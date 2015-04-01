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
			adjuster->adjustX(2);
		} else {
			adjuster->adjustX(-2);
		}
	}
	if(!pointYInRect(imageCenter, rect)) {
		if(imageCenter.y <= rect.y) {
			adjuster->adjustY(-2);
		} else {
			adjuster->adjustY(2);
		}
	}
}

void CubeCenterTargeter::microAdjust(const cv::Point& imageCenter, const cv::Rect& rect) {
	cv::Point cubeCenter = rectCenter(rect);

	if(rect.width >= 5 && imageCenter.x - cubeCenter.x > rect.width/4) {
		adjuster->adjustX(-0.5);
	}
	if(rect.width >= 5 && cubeCenter.x - imageCenter.x > rect.width/4) {
		adjuster->adjustX(0.5);
	}

	if(rect.width >= 5 && imageCenter.y - cubeCenter.y > rect.height/4) {
		adjuster->adjustY(0.5);
	}
	if(rect.width >= 5 && cubeCenter.y - imageCenter.y > rect.height/4) {
		adjuster->adjustY(-0.5);
	}
}

bool CubeCenterTargeter::needMicroAdjust(const cv::Point& imageCenter, const cv::Rect& rect) {
	bool answer = false;
	cv::Point cubeCenter = rectCenter(rect);

	if(rect.width >= 5 && imageCenter.x - cubeCenter.x >= rect.width/4) {
		answer = true;
	}
	if(rect.width >= 5 && cubeCenter.x - imageCenter.x >= rect.width/4) {
		answer = true;
	}

	if(rect.width >= 5 && imageCenter.y - cubeCenter.y >= rect.height/4) {
		answer = true;
	}
	if(rect.width >= 5 && cubeCenter.y - imageCenter.y >= rect.height/4) {
		answer = true;
	}
	return answer;
}

static inline bool noDetection(const cv::Rect& cubeRect) {
	return cubeRect.width == 0 || cubeRect.height == 0;
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
		if( noDetection( rect ) ) break;
		imageCenter = cv::Point(320, 240);
		macroAdjust(imageCenter, rect);
	} while(!pointInRect(imageCenter, rect));

	do {
		capturer->capture();
		rect = detector->detectCube();
		if( noDetection( rect ) ) break;
		imageCenter = cv::Point(320, 240);
		microAdjust(imageCenter, rect);
	} while(needMicroAdjust(imageCenter, rect));
}

} //d3t12