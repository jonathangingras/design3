#include <vision/ColorFilter.h>

namespace d3t12 {

void ColorFilter::filter(cv::Mat& dst, const cv::Mat& src) {
    if(src.type() != CV_8UC3) {
        throw BitmapFormatException("ColorFilter::filter : bad bitmap format, requires CV_8UC3!");
    }

    cv::Mat converted;
    cv::cvtColor(src, converted, CV_BGR2HSV);

    cv::inRange(converted, color.range.min, color.range.max, dst);

    int erosion_size = 1;
    cv::Mat element = cv::getStructuringElement(
    		cv::MORPH_CROSS,
    		cv::Size( 2*erosion_size + 1, 2*erosion_size+1 ),
        	cv::Point( erosion_size, erosion_size )
       	);
    
    cv::erode(dst, dst, element);
    cv::erode(dst, dst, element);
    cv::erode(dst, dst, element);

    cv::dilate(dst, dst, element);
    cv::dilate(dst, dst, element);
    cv::dilate(dst, dst, element);
    cv::dilate(dst, dst, element);
    cv::dilate(dst, dst, element);
}

}