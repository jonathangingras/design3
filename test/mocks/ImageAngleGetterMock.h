#ifndef _D3T12_IMAGEANGLEGETTER_H_
#define _D3T12_IMAGEANGLEGETTER_H_

#include <testEssentials.h>
#include <ai/ai.h>

class ImageAngleGetterMock : public d3t12::ImageAngleGetter {
public:
	MOCK_METHOD0(getPitch, double(void));
	MOCK_METHOD0(getYaw, double(void));
};

#define CAST_AGETTER(mock) *( (ImageAngleGetterMock*) mock .get() )

#endif