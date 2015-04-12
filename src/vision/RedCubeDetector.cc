#include <vision/RedCubeDetector.h>

namespace d3t12 {

cv::Rect RedCubeDetector::detectCube() {
	cv::Mat out, out1, out2;
	filter1->filter(out1, *sourceImage);
    filter2->filter(out2, *sourceImage);
    cv::bitwise_or(out1, out2, out);

	std::vector<cv::Vec4i> hierarchy;
    std::vector<std::vector<cv::Point> > contours;
    cv::findContours(out, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

    d3t12::IncrementalRect incRect;
    for(int i = 0; i < contours.size(); ++i) {
        incRect += cv::boundingRect(contours[i]);
    }

    return incRect.toCvRect();
}

RedCubeDetector::~RedCubeDetector() {}

}