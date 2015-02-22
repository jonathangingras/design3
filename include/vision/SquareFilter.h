#ifndef _D3T12_SQUAREFILTER_H_
#define _D3T12_SQUAREFILTER_H_

#include <opencv2/opencv.hpp>

namespace d3t12 {

class SquareFilter {
protected:
	std::vector<std::vector<cv::Point> > squares;

	double angle(cv::Point pt1, cv::Point pt2, cv::Point pt0);

public:
	inline SquareFilter() {}

	void findSquares(const cv::Mat& image);
	void drawSquares(cv::Mat& image) const;
	
	inline std::vector<std::vector<cv::Point> > getSquares() const {
		return squares;
	}
};

}

#endif