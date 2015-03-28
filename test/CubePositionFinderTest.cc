#include <testEssentials.h>
#include <ai/ai.h>

using namespace d3t12;
using ::testing::Return;

class ImageAngleGetterMock : public d3t12::ImageAngleGetter {
public:
	MOCK_METHOD0(getPitch, double(void));
	MOCK_METHOD0(getYaw, double(void));
};

#define CAST_AGETTER(mock) *( (ImageAngleGetterMock*) mock .get() )

class CubePositionFinderTest : public d3t12::CubePositionFinder {
public:
	inline CubePositionFinderTest(ImageAngleGetter::Ptr _anglesGetter, double _pulleyHeight, double _eyeToPulleyHeight, double _eyeToPulleyWidth):
		CubePositionFinder::CubePositionFinder(_anglesGetter, _pulleyHeight, _eyeToPulleyHeight, _eyeToPulleyWidth) {}

	inline double getAdjustedHeight(double pitch) {
		return CubePositionFinder::getAdjustedHeight(pitch);
	}

	inline double getCameraEyeXOffset(double pitch) {
		return CubePositionFinder::getCameraEyeXOffset(pitch);
	} 
};

#define FLOAT_THRESHOLD 0.0000001

#define CAM_PULLEY_HEIGTH 0.03
#define CAM_PULLEY_WIDTH  0.02
#define PULLEY_HEIGHT     0.30

#define SETUP \
	ImageAngleGetter::Ptr angleGetterMock(new ImageAngleGetterMock); \
	CubePositionFinderTest finder(angleGetterMock, PULLEY_HEIGHT, CAM_PULLEY_HEIGTH, CAM_PULLEY_WIDTH);

TEST(CubePositionFinder, AdjustedHeightIsEqualToPulleyHeightMinusCamPulleyHeigthWhenAnglePiOn2) {
	SETUP

	EXPECT_LT(CAM_PULLEY_HEIGTH - finder.getAdjustedHeight(M_PI/2) - PULLEY_HEIGHT, FLOAT_THRESHOLD);
}

TEST(CubePositionFinder, XOffsetIsEqualToCamPulleyWidthWhenAnglePiOn2) {
	SETUP

	EXPECT_LT(CAM_PULLEY_WIDTH - finder.getCameraEyeXOffset(M_PI/2), FLOAT_THRESHOLD);
}

TEST(CubePositionFinder, AdjustedHeightIsEqualToPulleyHeightMinusPoint0071CamPulleyHeigthWhenAnglePiOn4) {
	SETUP

	EXPECT_LT(CAM_PULLEY_HEIGTH - finder.getAdjustedHeight(M_PI/4) - 0.0071*PULLEY_HEIGHT, FLOAT_THRESHOLD);
}

TEST(CubePositionFinder, AdjustedHeightIsEqualToPulleyHeightMinusPoint0023CamPulleyHeigthWhenAnglePiOn6) {
	SETUP

	EXPECT_LT(CAM_PULLEY_HEIGTH - finder.getAdjustedHeight(M_PI/6) - 0.0023*PULLEY_HEIGHT, FLOAT_THRESHOLD);
}

TEST(CubePositionFinder, AdjustedHeightIsEqualToPulleyHeightMinusCamPulleyWidthWhenAngle0) {
	SETUP

	EXPECT_LT(CAM_PULLEY_WIDTH - finder.getAdjustedHeight(0) - PULLEY_HEIGHT, FLOAT_THRESHOLD);
}

TEST(CubePositionFinder, positionReturnedIsGoodWhenPitchPiOn4AndYawPiOn4) {
	SETUP

	EXPECT_CALL(CAST_AGETTER(angleGetterMock), getPitch()).Times(1).WillRepeatedly(Return(M_PI/4));
	EXPECT_CALL(CAST_AGETTER(angleGetterMock), getYaw()).Times(1).WillRepeatedly(Return(M_PI/4));

	std::cout << finder.findCubePosition() << std::endl;
}

TEST(CubePositionFinder, positionReturnedIsGoodWhenPitchPiOn3AndYawPiOn3) {
	SETUP

	EXPECT_CALL(CAST_AGETTER(angleGetterMock), getPitch()).Times(1).WillRepeatedly(Return(M_PI/3));
	EXPECT_CALL(CAST_AGETTER(angleGetterMock), getYaw()).Times(1).WillRepeatedly(Return(M_PI/3));

	std::cout << finder.findCubePosition() << std::endl;
}

TEST(CubePositionFinder, positionReturnedIsGoodWhenPitchPiOn3AndYaw2PiOn3) {
	SETUP

	EXPECT_CALL(CAST_AGETTER(angleGetterMock), getPitch()).Times(1).WillRepeatedly(Return(M_PI/3));
	EXPECT_CALL(CAST_AGETTER(angleGetterMock), getYaw()).Times(1).WillRepeatedly(Return(2*M_PI/3));

	std::cout << finder.findCubePosition() << std::endl;
}