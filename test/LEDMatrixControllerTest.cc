#include <testEssentials.h>
#include <driver/LEDMatrixController.h>

using namespace d3t12;

#define SETUP \
	std::ostringstream* oss = new std::ostringstream; \
	LEDMatrixController leds( \
		MicroControllerCommandPort::Ptr(  \
			new MicroControllerCommandPort(MicroControllerCommandPort::OStreamPtr(oss))  \
		) \
	);

TEST(LEDMatrixController, canTurnMasterOn) {
	SETUP

	leds.turnMasterOn();

	EXPECT_EQ("setled on\n", oss->str());
}

TEST(LEDMatrixController, canTurnMasterOff) {
	SETUP

	leds.turnMasterOn();
	leds.turnMasterOff();

	EXPECT_EQ("setled on\nsetled off\n", oss->str());
}

TEST(LEDMatrixController, hasGoodOrder) {
	SETUP

	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");

	EXPECT_EQ("setledrgb 7 bk\nsetledrgb 8 bk\nsetledrgb 9 bk\nsetledrgb 4 bk\nsetledrgb 5 bk\nsetledrgb 6 bk\nsetledrgb 1 bk\nsetledrgb 2 bk\nsetledrgb 3 bk\n", oss->str());
}

TEST(LEDMatrixController, resumesWhenDoneOnce) {
	SETUP

	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");

	leds.addNew("blue");

	EXPECT_EQ("setledrgb 7 bk\nsetledrgb 8 bk\nsetledrgb 9 bk\nsetledrgb 4 bk\nsetledrgb 5 bk\nsetledrgb 6 bk\nsetledrgb 1 bk\nsetledrgb 2 bk\nsetledrgb 3 bk\nsetledrgb 7 b\n", oss->str());
}

TEST(LEDMatrixController, canTurnFirstLEDRed) {
	SETUP

	leds.addNew("red");

	EXPECT_EQ("setledrgb 7 r\n", oss->str());
}

TEST(LEDMatrixController, canTurnSecondLEDBlack) {
	SETUP

	leds.addNew("red");
	leds.addNew("black");

	EXPECT_EQ("setledrgb 7 r\nsetledrgb 8 bk\n", oss->str());
}

TEST(LEDMatrixController, canSkipFirst) {
	SETUP

	leds.addBlank();
	leds.addNew("black");

	EXPECT_EQ("setledrgb 8 bk\n", oss->str());
}

TEST(LEDMatrixController, canCancelFirst) {
	SETUP

	leds.addNew("red");
	leds.removeCurrent();

	EXPECT_EQ("setledrgb 7 r\nsetledrgb 7 x\n", oss->str());
}

TEST(LEDMatrixController, canCancelFirstAndResumeOnSameLEDNumber) {
	SETUP

	leds.addNew("red");
	leds.removeCurrent();
	leds.addNew("white");

	EXPECT_EQ("setledrgb 7 r\nsetledrgb 7 x\nsetledrgb 7 w\n", oss->str());
}

TEST(LEDMatrixController, canSkipSecond) {
	SETUP

	leds.addNew("black");
	leds.addBlank();
	leds.addNew("black");
	leds.addNew("black");

	EXPECT_EQ("setledrgb 7 bk\nsetledrgb 9 bk\nsetledrgb 4 bk\n", oss->str());
}

TEST(LEDMatrixController, canCancelSecondAndResumeOnSameLEDNumber) {
	SETUP

	leds.addNew("green");
	leds.addNew("red");
	leds.removeCurrent();
	leds.addNew("white");
	leds.addNew("yellow");

	EXPECT_EQ("setledrgb 7 g\nsetledrgb 8 r\nsetledrgb 8 x\nsetledrgb 8 w\nsetledrgb 9 y\n", oss->str());
}

TEST(LEDMatrixController, canCancelLastAndResumeOnSameLEDNumber) {
	SETUP

	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");

	leds.removeCurrent();
	
	leds.addNew("white");

	EXPECT_EQ("setledrgb 7 bk\nsetledrgb 8 bk\nsetledrgb 9 bk\nsetledrgb 4 bk\nsetledrgb 5 bk\nsetledrgb 6 bk\nsetledrgb 1 bk\nsetledrgb 2 bk\nsetledrgb 3 bk\nsetledrgb 3 x\nsetledrgb 3 w\n", oss->str());
}

TEST(LEDMatrixController, matrixFilledWhenAdded9LEDs) {
	SETUP

	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");

	EXPECT_TRUE(leds.matrixFilled());
}

TEST(LEDMatrixController, matrixNotFilledWhenAdded8LEDs) {
	SETUP

	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");

	EXPECT_FALSE(leds.matrixFilled());
}

TEST(LEDMatrixController, matrixNotFilledAfterResumingAfterFillingOnce) {
	SETUP

	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");
	leds.addNew("black");

	leds.addNew("black");

	EXPECT_FALSE(leds.matrixFilled());
}