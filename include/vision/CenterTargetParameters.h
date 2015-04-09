#ifndef _CENTERTARGETPARAMENTERS_H_
#define _CENTERTARGETPARAMENTERS_H_

namespace d3t12 {

struct CenterTargetParameters {
	float microUnit;
	float macroUnit;
	float scaleFactor;
	cv::Point centerTarget;

	inline CenterTargetParameters():
		microUnit(0.5), macroUnit(2.0), scaleFactor(0.25), centerTarget(320,240) {}
	inline CenterTargetParameters(float _microUnit, float _macroUnit, float _scaleFactor, cv::Point _centerTarget):
		microUnit(_microUnit), macroUnit(_macroUnit), scaleFactor(_scaleFactor), centerTarget(_centerTarget) {}
};

} //d3t12

#endif