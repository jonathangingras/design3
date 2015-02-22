#include <vision/IncrementalRect.h>

namespace d3t12 {

void IncrementalRect::operator += (cv::Rect _rect) {
	if(onceUsed && rect != _rect) {
		std::vector<cv::Point> points(4);
		points[0] = cv::Point(rect.x, rect.y);
		points[1] = cv::Point(rect.x + rect.width, rect.y + rect.height);
		points[2] = cv::Point(_rect.x, _rect.y);
		points[3] = cv::Point(_rect.x + _rect.width, _rect.y + _rect.height);

		rect = cv::boundingRect(points);
	} else if (!onceUsed) {
		rect = _rect;
		onceUsed = true;
	}
	else {

	}
}

}