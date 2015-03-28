#ifndef _D3T12_CUBERELATIVEPOSITION_H_
#define _D3T12_CUBERELATIVEPOSITION_H_

#include <ostream>

namespace d3t12 {

struct CubeRelativePosition {
	double x;
	double y;

	inline CubeRelativePosition(double _x, double _y):
		x(_x), y(_y) {}
};

inline std::ostream& operator << (std::ostream& os, const CubeRelativePosition& position) {
	os << "[ relative position -> x: " << position.x << ", y: " << position.y << " ]";
	return os;
}

}

#endif