#include <vision/ColorFilter.h>

namespace d3t12 {

void ColorFilter::filter(cv::Mat& dst, const cv::Mat& src) {
    if(src.type() != CV_8UC3) {
        throw BitmapFormatException("ColorFilter::filter : bad bitmap format, requires CV_8UC3!");
    }

    cv::Mat converted;
    cv::cvtColor(src, converted, CV_BGR2HSV);

    cv::inRange(converted, color.range.min, color.range.max, dst);
}

}