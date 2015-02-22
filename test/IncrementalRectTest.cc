#include "testEssentials.h"
#include <vision/IncrementalRect.h>

using namespace d3t12;

#define ZERO_RECT cv::Rect(0,0,0,0)
#define ORIGIN_POINT cv::Point(0,0)

TEST(IncrementalRect, returnsZeroRectWhenNeverUsed) {
	IncrementalRect incRect;

	EXPECT_EQ(ZERO_RECT, incRect.toCvRect());
}

TEST(IncrementalRect, returnsOriginPointAsCenterWhenNeverUsed) {
	IncrementalRect incRect;

	EXPECT_EQ(ORIGIN_POINT, incRect.centerToCvPoint());
}

TEST(IncrementalRect, returnsSameRectWhenUsedOnce) {
	IncrementalRect incRect;

	incRect += cv::Rect(10,10,30,30);

	EXPECT_EQ(cv::Rect(10,10,30,30), incRect.toCvRect());
}

TEST(IncrementalRect, returnsSameRectCenterAsCenterWhenUsedOnce) {
	IncrementalRect incRect;

	incRect += cv::Rect(10,10,30,30);

	EXPECT_EQ(cv::Point(25,25), incRect.centerToCvPoint());
}

TEST(IncrementalRect, doesntChangeWhenIncrementedWithSameRectTwice) {
	IncrementalRect incRect;

	incRect += cv::Rect(10,10,30,30);
	incRect += cv::Rect(10,10,30,30);

	EXPECT_EQ(cv::Rect(10,10,30,30), incRect.toCvRect());
	EXPECT_EQ(cv::Point(25,25), incRect.centerToCvPoint());
}


TEST(IncrementalRect, incrementsWhenIncrementedWithOuterRectRight) {
	IncrementalRect incRect;

	incRect += cv::Rect(10,10,30,30);
	incRect += cv::Rect(20,20,30,30);

	EXPECT_EQ(cv::Rect(10,10,41,41), incRect.toCvRect());
	EXPECT_EQ(cv::Point(30,30), incRect.centerToCvPoint());
}

TEST(IncrementalRect, incrementsWhenIncrementedWithOuterRectLeft) {
	IncrementalRect incRect;

	incRect += cv::Rect(10,10,30,30);
	incRect += cv::Rect(5,5,30,30);

	EXPECT_EQ(cv::Rect(5,5,36,36), incRect.toCvRect());
	EXPECT_EQ(cv::Point(23,23), incRect.centerToCvPoint());
}

TEST(IncrementalRect, isZeroWhenReset) {
	IncrementalRect incRect;

	incRect += cv::Rect(10,10,30,30);
	incRect += cv::Rect(5,5,30,30);
	incRect.reset();

	EXPECT_EQ(ZERO_RECT, incRect.toCvRect());
	EXPECT_EQ(ORIGIN_POINT, incRect.centerToCvPoint());
}

TEST(IncrementalRect, hasSameBehaviorAsNewWhenReset) {
	IncrementalRect incRect;

	incRect += cv::Rect(10,10,30,30);
	incRect += cv::Rect(5,5,30,30);
	incRect.reset();
	incRect += cv::Rect(10,10,30,30);

	EXPECT_EQ(cv::Rect(10,10,30,30), incRect.toCvRect());
	EXPECT_EQ(cv::Point(25,25), incRect.centerToCvPoint());
}