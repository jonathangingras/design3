#include <vision/ColorJSONLoader.h>
#include "testEssentials.h"
#include "mocks/ColorPaletteMock.h"

using namespace d3t12;

TEST(ColorJSONLoader, throwsWhenNoSuchJSONFile) {
	ColorJSONLoader loader;
	loader.setFile("../test/test_jsons/nosuchfile");

	EXPECT_THROW(loader.loadJSON(), JanssonException);
}

TEST(ColorJSONLoader, throwsWhenJSONFileEmpty) {
	ColorJSONLoader loader;
	loader.setFile("../test/test_jsons/emptyfile.json");

	EXPECT_THROW(loader.loadJSON(), JanssonException);
}

TEST(ColorJSONLoader, throwsWhenJSONEmpty) {
	ColorJSONLoader loader;
	loader.setFile("../test/test_jsons/emptyjson.json");

	EXPECT_THROW(loader.loadJSON(), JanssonException);
}

TEST(ColorJSONLoader, throwsWhenNoFieldColorsInJSON) {
	ColorJSONLoader loader;
	loader.setFile("../test/test_jsons/nofieldcolors.json");

	EXPECT_THROW(loader.loadJSON(), JanssonException);
}

MATCHER(StrNotEmpty, "is not empty") { return !std::string(arg).empty(); }

TEST(ColorJSONLoader, callsColorPaletteToStoreColors) {
	ColorJSONLoader loader;
	loader.setFile("../test/test_jsons/colors.json");
	loader.loadJSON();
	ColorPaletteMock paletteMock;

	EXPECT_CALL(paletteMock, storeColor(StrNotEmpty(), _)).Times(AnyNumber());

	loader.fillPalette(paletteMock);
}

TEST(ColorJSONLoader, callsColorPaletteToStoreColorsOnceWhenOneColor) {
	ColorJSONLoader loader;
	loader.setFile("../test/test_jsons/onecolor.json");
	loader.loadJSON();
	ColorPaletteMock paletteMock;

	EXPECT_CALL(paletteMock, storeColor(StrNotEmpty(), _)).Times(1);

	loader.fillPalette(paletteMock);
}

MATCHER(GoodColorString, "color has good string") { return std::string(arg) == "blue"; }
MATCHER(GoodColorRanges, "color has good ranges") { return arg.range.min == cv::Scalar(90,110,80) && arg.range.max == cv::Scalar(110,255,200); }

TEST(ColorJSONLoader, colorIsAccuratelyCreated) {
	ColorJSONLoader loader;
	loader.setFile("../test/test_jsons/onecolor.json");
	loader.loadJSON();
	ColorPaletteMock paletteMock;

	EXPECT_CALL(paletteMock, storeColor(GoodColorString(), GoodColorRanges())).Times(1);

	loader.fillPalette(paletteMock);
}