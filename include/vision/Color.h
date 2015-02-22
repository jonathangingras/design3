#ifndef _D3T12_COLOR_H_
#define _D3T12_COLOR_H_

#include <iostream>
#include <opencv2/opencv.hpp>

namespace d3t12 {

struct ColorRange {
		cv::Scalar min, max;

		inline ColorRange() {}
		inline ColorRange(cv::Scalar _min, cv::Scalar _max) : min(_min), max(_max) {}
};

struct Color {
		typedef ColorRange Range;
		typedef enum {RGB = 0, HSV = 1} Space;

		Range range;

		inline Color() {}
		inline Color(Range p_range) : range(p_range) {}
};

inline bool operator == (Color first, Color other) {
		return first.range.min == other.range.min && first.range.max == other.range.max;
}

std::ostream& operator<<(std::ostream& os, Color color);

}

#endif