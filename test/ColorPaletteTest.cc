#include "testEssentials.h"
#include <vision/ColorPalette.h>

using namespace d3t12;

#define VALID_COLOR_NAME "blue"

TEST(ColorPalette, canStoreColor) {
	ColorPalette palette;

	EXPECT_NO_THROW(palette.storeColor(VALID_COLOR_NAME, Color()));
}

TEST(ColorPalette, throwsWhenStoreEmptyStringColor) {
	ColorPalette palette;

	EXPECT_THROW(palette.storeColor("", Color()), BadColorStringException);
}

TEST(ColorPalette, throwsWhenGettingColorNeverStoredBefore) {
	ColorPalette palette;

	EXPECT_THROW(palette.getColor(VALID_COLOR_NAME), BadColorStringException);
}

TEST(ColorPalette, throwsWhenGettingColorByEmptyColorString) {
	ColorPalette palette;

	EXPECT_THROW(palette.getColor(""), BadColorStringException);
}

TEST(ColorPalette, returnsGoodColorWhenGettingColor) {
	ColorPalette palette;

	Color color(Color::Range(cv::Scalar(10,10,10), cv::Scalar(20,20,20)));

	palette.storeColor(VALID_COLOR_NAME, color);

	EXPECT_EQ(color, palette.getColor(VALID_COLOR_NAME));
}

TEST(ColorPalette, overwritesLastColorWhenStoreWithSameString) {
	ColorPalette palette;

	Color color1(Color::Range(cv::Scalar(10,10,10), cv::Scalar(20,20,20)));
	palette.storeColor(VALID_COLOR_NAME, color1);

	Color color2(Color::Range(cv::Scalar(30,30,30), cv::Scalar(40,40,40)));
	palette.storeColor(VALID_COLOR_NAME, color2);

	EXPECT_EQ(color2, palette.getColor(VALID_COLOR_NAME));
}