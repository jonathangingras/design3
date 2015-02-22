#include <vision/ColoredCubeDetector.h>

namespace d3t12 {

cv::Rect ColoredCubeDetector::detectCube() {
	cv::Mat out;
	filter->filter(out, *sourceImage);

	std::vector<cv::Vec4i> hierarchy;
    std::vector<std::vector<cv::Point> > contours;
    cv::findContours(out, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

    d3t12::IncrementalRect incRect;
    for(int i = 0; i < contours.size(); ++i) {
        incRect += cv::boundingRect(contours[i]);
    }

    return incRect.toCvRect();
}

ColoredCubeDetector::~ColoredCubeDetector() {}

}