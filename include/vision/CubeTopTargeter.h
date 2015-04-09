#ifndef _D3T12_CUBETOPTARGETER_H_
#define _D3T12_CUBETOPTARGETER_H_

#include "CubeCenterTargeter.h"

namespace d3t12 {

class CubeTopTargeter : public CubeCenterTargeter {
public:
	inline CubeTopTargeter(ImageCapturer::Ptr _capturer, ImageAngleAdjuster::Ptr _adjuster, CenterTargetParameters _targetParameters):
		CubeCenterTargeter(_capturer, _adjuster, _targetParameters) {}

	virtual void targetCenter();
};

}

#endif