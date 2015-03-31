#ifndef _D3T12_IMAGEADJUSTERMOCK_H_
#define _D3T12_IMAGEADJUSTERMOCK_H_

#include <vision/ImageAngleAdjuster.h>

class ImageAngleAdjusterMock : public d3t12::ImageAngleAdjuster {
public:
  MOCK_METHOD1(adjustX, void(float degrees));
  MOCK_METHOD1(adjustY, void(float degrees));
};

#define CAST_ADJUSTER(mock) *((ImageAngleAdjusterMock*) mock .get())

#endif