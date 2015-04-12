#ifndef _D3T12_IMAGEANGLESGETTER_H_
#define _D3T12_IMAGEANGLESGETTER_H_

#include <common/commonEssentials.h>

namespace d3t12 {

class ImageAngleGetter {
public:
	typedef boost::shared_ptr<ImageAngleGetter> Ptr;

	virtual ~ImageAngleGetter() {}
	virtual double getPitch() = 0;
	virtual double getYaw() = 0;
};

}

#endif