#include <testEssentials.h>
#include <driver/driver.h>

using namespace d3t12;

#define SETUP MicroControllerCommandPort::OStreamPtr os(new std::ostringstream);\
			  MicroControllerCommandPort port(os);
#define osStr reinterpret_cast<std::ostringstream*>(os.get())->str()

TEST(MicroControllerLEDCommandBuilderTest, canTurnOnMasterLED) {
	SETUP
	MicroControllerLEDCommandBuilder ledCommandbuilder;

	port << ledCommandbuilder.setLED(0).setPower(true).build();

	EXPECT_EQ("setled on\n", osStr);
}

TEST(MicroControllerLEDCommandBuilderTest, canTurnOffMasterLED) {
	SETUP
	MicroControllerLEDCommandBuilder ledCommandbuilder;

	port << ledCommandbuilder.setLED(0).setPower(false).build();

	EXPECT_EQ("setled off\n", osStr);
}

TEST(MicroControllerLEDCommandBuilderTest, canTurnRedLED1) {
	SETUP
	MicroControllerLEDCommandBuilder ledCommandbuilder;

	port << ledCommandbuilder.setLED(1).setColor("red").build();

	EXPECT_EQ("setledrgb 1 r\n", osStr);
}

TEST(MicroControllerLEDCommandBuilderTest, canTurnRedLED1WhenPowerSetOnAtEnd) {
	SETUP
	MicroControllerLEDCommandBuilder ledCommandbuilder;

	port << ledCommandbuilder.setLED(1).setColor("red").setPower(true).build();

	EXPECT_EQ("setledrgb 1 r\n", osStr);
}

TEST(MicroControllerLEDCommandBuilderTest, canTurnLED1OffWhenPowerSetOffAtEnd) {
	SETUP
	MicroControllerLEDCommandBuilder ledCommandbuilder;

	port << ledCommandbuilder.setLED(1).setColor("red").setPower(false).build();

	EXPECT_EQ("setledrgb 1 x\n", osStr);
}

TEST(MicroControllerLEDCommandBuilderTest, canTurnLED1OffWhenPowerSetOffAtBeginning) {
	SETUP
	MicroControllerLEDCommandBuilder ledCommandbuilder;

	port << ledCommandbuilder.setLED(1).setPower(false).build();

	EXPECT_EQ("setledrgb 1 x\n", osStr);
}

TEST(MicroControllerLEDCommandBuilderTest, canDoLastJobAfterMultipleSettings) {
	SETUP
	MicroControllerLEDCommandBuilder ledCommandbuilder;

	port << ledCommandbuilder.setLED(1).setColor("red").setPower(false).setLED(0).setPower(true).build();

	EXPECT_EQ("setled on\n", osStr);
}

TEST(MicroControllerLEDCommandBuilderTest, doesntAccumulateStringsWhenBuilding) {
	SETUP
	MicroControllerLEDCommandBuilder ledCommandbuilder;

	port << ledCommandbuilder.setLED(0).setPower(true).build();
	port << ledCommandbuilder.setLED(0).setPower(false).build();

	EXPECT_EQ("setled on\nsetled off\n", osStr);
}

TEST(MicroControllerMotorControlCommandBuilderTest, canSendCurrentPosition) {
	SETUP
	MicroControllerMotorControlCommandBuilder motorCommandbuilder;

	port << motorCommandbuilder.setCurrentPosition(1.1, 1.1, 1.1).build();

	EXPECT_EQ("setpos 1.1 1.1 1.1\n", osStr);
}

TEST(MicroControllerMotorControlCommandBuilderTest, canSendCurrentPositionAtEnd) {
	SETUP
	MicroControllerMotorControlCommandBuilder motorCommandbuilder;

	port << motorCommandbuilder.setWantedPosition(1.1, 1.1, 1.1).setCurrentPosition(1.1, 1.1, 1.1).build();

	EXPECT_EQ("setpos 1.1 1.1 1.1\n", osStr);
}

TEST(MicroControllerMotorControlCommandBuilderTest, canSendWantedPosition) {
	SETUP
	MicroControllerMotorControlCommandBuilder motorCommandbuilder;

	port << motorCommandbuilder.setWantedPosition(1.1, 1.1, 1.1).build();

	EXPECT_EQ("goto 1.1 1.1 1.1\n", osStr);
}

TEST(MicroControllerMotorControlCommandBuilderTest, canSendWantedPositionAtEnd) {
	SETUP
	MicroControllerMotorControlCommandBuilder motorCommandbuilder;

	port << motorCommandbuilder.setCurrentPosition(1.1, 1.1, 1.1).setWantedPosition(1.1, 1.1, 1.1).build();

	EXPECT_EQ("goto 1.1 1.1 1.1\n", osStr);
}

TEST(MicroControllerMotorControlCommandBuilderTest, doesntAccumulateStringsWhenBuilding) {
	SETUP
	MicroControllerMotorControlCommandBuilder motorCommandbuilder;

	port << motorCommandbuilder.setCurrentPosition(1.1, 1.1, 1.1).build();
	port << motorCommandbuilder.setWantedPosition(1.1, 1.1, 1.1).build();

	EXPECT_EQ("setpos 1.1 1.1 1.1\ngoto 1.1 1.1 1.1\n", osStr);
}