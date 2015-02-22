#ifndef _D3T12_VISIONESSENTIALS_H_
#define _D3T12_VISIONESSENTIALS_H_

#include <opencv2/opencv.hpp>
#include <boost/smart_ptr.hpp>

namespace d3t12 {
typedef boost::shared_ptr<cv::Mat> cvMatPtr;
}

#endif