#ifndef _D3T12_INCREMENTALRECT_H_
#define _D3T12_INCREMENTALRECT_H_

#include <opencv2/opencv.hpp>

namespace d3t12 {

class IncrementalRect {
private:
	cv::Rect rect;
	bool onceUsed;
public:
	inline IncrementalRect(): onceUsed(false) {}

	void operator += (cv::Rect _rect);

	inline cv::Rect toCvRect() {
		return rect;
	}

	inline cv::Point centerToCvPoint() {
		return cv::Point(rect.x + rect.width/2, rect.y + rect.height/2);
	}

	inline void reset() {
		onceUsed = false;
		rect = cv::Rect(0,0,0,0);
	}
};

}

#endif