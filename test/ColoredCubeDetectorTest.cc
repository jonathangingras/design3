#include <testEssentials.h>
#include <vision/vision.h>

#include <CubeDetectorTester.h>

using namespace d3t12;

CubeDetectorTester tester;
#define IMAGE_FILENAME "../test/test_images/image2.png"

TEST(ColoredCubeDetector, canDetectBlue) {
	tester.setImageFromFile(IMAGE_FILENAME);
	cv::Rect cubeRect = tester.detectColor("blue");
	std::cout << cubeRect;
	tester.showImage(cubeRect);

	EXPECT_GE(cubeRect.x, 390);
	EXPECT_LE(cubeRect.x, 400);
	EXPECT_GE(cubeRect.y, 275);
	EXPECT_LE(cubeRect.y, 285);

	EXPECT_GE(cubeRect.width, 65);
	EXPECT_LE(cubeRect.width, 75);
	EXPECT_GE(cubeRect.height, 40);
	EXPECT_LE(cubeRect.height, 50);
}

TEST(ColoredCubeDetector, canDetectYellow) {
	tester.setImageFromFile(IMAGE_FILENAME);
	cv::Rect cubeRect = tester.detectColor("yellow");
	std::cout << cubeRect;
	tester.showImage(cubeRect);

	EXPECT_GE(cubeRect.x, 390);
	EXPECT_LE(cubeRect.x, 400);
	EXPECT_GE(cubeRect.y, 315);
	EXPECT_LE(cubeRect.y, 325);

	EXPECT_GE(cubeRect.width, 85);
	EXPECT_LE(cubeRect.width, 100);
	EXPECT_GE(cubeRect.height, 90);
	EXPECT_LE(cubeRect.height, 100);
}

TEST(ColoredCubeDetector, canDetectGreen) {
	tester.setImageFromFile(IMAGE_FILENAME);
	cv::Rect cubeRect = tester.detectColor("green");
	std::cout << cubeRect;
	tester.showImage(cubeRect);

	EXPECT_GE(cubeRect.x, 410);
	EXPECT_LE(cubeRect.x, 420);
	EXPECT_GE(cubeRect.y, 350);
	EXPECT_LE(cubeRect.y, 360);

	EXPECT_GE(cubeRect.width, 110);
	EXPECT_LE(cubeRect.width, 120);
	EXPECT_GE(cubeRect.height, 115);
	EXPECT_LE(cubeRect.height, 125);
}

TEST(ColoredCubeDetector, canDetectRed) {
	tester.setImageFromFile(IMAGE_FILENAME);
	cv::Rect cubeRect = tester.detectColor("red");
	std::cout << cubeRect;
	tester.showImage(cubeRect);

	EXPECT_GE(cubeRect.x, 510);
	EXPECT_LE(cubeRect.x, 520);
	EXPECT_GE(cubeRect.y, 345);
	EXPECT_LE(cubeRect.y, 355);

	EXPECT_GE(cubeRect.width, 110);
	EXPECT_LE(cubeRect.width, 120);
	EXPECT_GE(cubeRect.height, 115);
	EXPECT_LE(cubeRect.height, 125);
}