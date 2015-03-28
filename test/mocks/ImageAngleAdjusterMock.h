#ifndef _D3T12_COLORPALETTEMOCK_H_
#define _D3T12_COLORPALETTEMOCK_H_

#include <vision/ImageAngleAdjuster.h>

class ImageAngleAdjusterMock : public d3t12::ImageAngleAdjuster {
public:
  MOCK_METHOD1(adjustX, void(float degrees));
  MOCK_METHOD1(adjustY, void(float degrees));
};

#endif