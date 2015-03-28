#ifndef _D3T12_CUBEPOSITIONFINDER_H_
#define _D3T12_CUBEPOSITIONFINDER_H_

#include "CubeRelativePosition.h"
#include "ImageAngleGetter.h"
#include <math.h>

namespace d3t12 {

class CubePositionFinder {
private:
	double pulleyHeight;
	double eyeToPulleyHeight;
	double eyeToPulleyWidth;

	ImageAngleGetter::Ptr anglesGetter;

protected:
	double getAdjustedHeight(double pitch);
	double getCameraEyeXOffset(double pitch);

public:
	inline CubePositionFinder(ImageAngleGetter::Ptr _anglesGetter, double _pulleyHeight, double _eyeToPulleyHeight, double _eyeToPulleyWidth):
		anglesGetter(_anglesGetter), pulleyHeight(_pulleyHeight), eyeToPulleyHeight(_eyeToPulleyHeight), eyeToPulleyWidth(_eyeToPulleyWidth) {}

	virtual CubeRelativePosition findCubePosition();
};

}

#endif