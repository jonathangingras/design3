#ifndef _D3T12_IMAGECAPTURER_H_
#define _D3T12_IMAGECAPTURER_H_

#include <common/commonEssentials.h>

namespace d3t12 {

class ImageCapturer {
public:
	typedef boost::shared_ptr<ImageCapturer> Ptr;
	virtual ~ImageCapturer() {}

	virtual void capture() = 0;
};

}

#endif