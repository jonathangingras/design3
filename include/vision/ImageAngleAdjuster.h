#ifndef _D3T12_IMAGEANGLEADJUSTER_H_
#define _D3T12_IMAGEANGLEADJUSTER_H_

#include <common/commonEssentials.h>

namespace d3t12 {

class ImageAngleAdjuster {
public:
	typedef boost::shared_ptr<ImageAngleAdjuster> Ptr;
	virtual ~ImageAngleAdjuster() {}

	virtual void adjustY(float degrees) = 0;
	virtual void adjustX(float degrees) = 0;
};

}

#endif