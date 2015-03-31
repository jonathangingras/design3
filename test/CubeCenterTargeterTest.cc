#include <testEssentials.h>
#include <vision/CubeCenterTargeter.h>

#include "mocks/ImageAngleAdjusterMock.h"
#include "mocks/CubeDetectorMock.h"

using namespace d3t12;
using ::testing::Return;

class ImageCapturerMock : public d3t12::ImageCapturer {
public:
	MOCK_METHOD0(capture, void(void));
};

#define CAST_CAPTURER(mock) *((ImageCapturerMock*) mock .get())

#define SETUP \
CubeDetector::Ptr detector(new CubeDetectorMock); \
ImageAngleAdjuster::Ptr adjuster(new ImageAngleAdjusterMock); \
ImageCapturer::Ptr capturer(new ImageCapturerMock); \
CubeCenterTargeter targeter(capturer, detector, adjuster);

TEST(CubeCenterTargeter, doesntAdjustWhenInMiddle) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(2);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(2).WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	targeter.targetCenter();
}

TEST(CubeCenterTargeter, adjustsXLeftOnceWhenNeededOnce) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(3);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(3).WillOnce(Return(cv::Rect(309,235,10,10)))
																.WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustX(-2)).Times(1);

	targeter.targetCenter();
}

/*TEST(CubeCenterTargeter, microAdjustsXLeftOnceWhenNeededOnce) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(310,230,20,20)));

	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(3).WillOnce(Return(cv::Rect(285,235,20,20)))
																.WillOnce(Return(cv::Rect(295,235,20,20)))
																.WillOnce(Return(cv::Rect(290,235,20,20)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustX(-2)).Times(2);
	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustX(-1)).Times(1);

	targeter.targetCenter();
}*/


TEST(CubeCenterTargeter, adjustsXRightOnceWhenNeededOnce) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(3);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(3).WillOnce(Return(cv::Rect(321,235,10,10)))
																.WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustX(2)).Times(1);

	targeter.targetCenter();
}

TEST(CubeCenterTargeter, adjustsYUpOnceWhenNeededOnce) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(3);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(3).WillOnce(Return(cv::Rect(315,229,10,10)))
																.WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustY(2)).Times(1);

	targeter.targetCenter();
}

TEST(CubeCenterTargeter, adjustsYDownOnceWhenNeededOnce) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(3);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(3).WillOnce(Return(cv::Rect(315,241,10,10)))
																.WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustY(-2)).Times(1);

	targeter.targetCenter();
}

TEST(CubeCenterTargeter, adjustsXLeftTwiceWhenNeededTwice) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(4);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(4).WillOnce(Return(cv::Rect(294,235,10,10)))
																.WillOnce(Return(cv::Rect(309,235,10,10)))
																.WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustX(-2)).Times(2);

	targeter.targetCenter();
}

TEST(CubeCenterTargeter, adjustsXRightTwiceWhenNeededTwice) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(4);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(4).WillOnce(Return(cv::Rect(326,235,10,10)))
																.WillOnce(Return(cv::Rect(321,235,10,10)))
																.WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustX(2)).Times(2);

	targeter.targetCenter();
}

TEST(CubeCenterTargeter, adjustsYUpTwiceWhenNeededTwice) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(4);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(4).WillOnce(Return(cv::Rect(315,224,10,10)))
																.WillOnce(Return(cv::Rect(315,229,10,10)))
																.WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustY(2)).Times(2);

	targeter.targetCenter();
}

TEST(CubeCenterTargeter, adjustsYDownTwiceWhenNeededTwice) {
	SETUP

	ON_CALL(CAST_DECTECTOR(detector), detectCube()).WillByDefault(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_CAPTURER(capturer), capture()).Times(4);
	EXPECT_CALL(CAST_DECTECTOR(detector), detectCube()).Times(4).WillOnce(Return(cv::Rect(315,246,10,10)))
																.WillOnce(Return(cv::Rect(315,241,10,10)))
																.WillRepeatedly(Return(cv::Rect(315,235,10,10)));

	EXPECT_CALL(CAST_ADJUSTER(adjuster), adjustY(-2)).Times(2);

	targeter.targetCenter();
}