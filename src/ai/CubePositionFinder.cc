#include <ai/CubePositionFinder.h>

namespace d3t12 {

double CubePositionFinder::getAdjustedHeight(double pitch) {
	double r = sqrt( pow(eyeToPulleyWidth, 2) + pow(eyeToPulleyHeight, 2) );
	double hc = r * cos( ((M_PI/2) - atan2(eyeToPulleyHeight, eyeToPulleyWidth)) + ((M_PI/2) - pitch) );
	return pulleyHeight + hc;
}

double CubePositionFinder::getCameraEyeXOffset(double pitch) {
	double r = sqrt( pow(eyeToPulleyWidth, 2) + pow(eyeToPulleyHeight, 2) );
	return r * sin( ((M_PI/2) - atan2(eyeToPulleyHeight, eyeToPulleyWidth)) + ((M_PI/2) - pitch) );
}

CubeRelativePosition CubePositionFinder::findCubePosition() {
	double pitch = anglesGetter->getPitch();
	double yaw = anglesGetter->getYaw();

	double d = getAdjustedHeight(pitch) * tan(pitch);
	double x = d * sin(yaw) + getCameraEyeXOffset(pitch);
	double y = d * cos(yaw);

	return CubeRelativePosition(x, y);
}

}