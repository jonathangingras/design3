#ifndef _D3T12_COLORFILTER_H_
#define _D3T12_COLORFILTER_H_

#include <vision/Color.h>
#include <vision/BitmapFormatException.h>

namespace d3t12 {

class ColorFilter {
private:
    Color color;

public:
    inline ColorFilter(Color p_color) : color(p_color) {}

    void filter(cv::Mat& dst, const cv::Mat& src);
};

}

#endif