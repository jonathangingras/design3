#include <testEssentials.h>
#include <driver/driver.h>

using namespace d3t12;

struct MockSystemCaller : public ::d3t12::SystemCaller {
	std::string commandReceived;

	virtual void call(const std::string& command) {
		commandReceived = command;
	}
};

#define SETUP SystemCaller::Ptr caller(new MockSystemCaller);\
				ServoMotorControllerFactory controllerFactory;

#define CASTMOCK(mock) (reinterpret_cast<MockSystemCaller*>( mock .get()))

static inline int rad2deg(double rad) {
	return (rad*180)/M_PI;
}

static inline double deg2rad(int deg) {
	return (deg*M_PI)/180;
}

#define TEST_hasGoodAngleAtInstanciation(servoStr, angle) 																			\
TEST(ServoMotorController_##servoStr, hasGoodAngleAtInstanciation) {														\
	SETUP																																													\
	ServoMotorController::Ptr controller = controllerFactory.createController(#servoStr, caller); \
																																																\
	EXPECT_EQ(angle, rad2deg(controller->getAngle()));																						\
}

#define TEST_systemCallerIsCalledWhenAngleSet(servoStr) 										  									\
TEST(ServoMotorController_##servoStr, SystemCallerIsCalledWhenAngleSet) { 						  				\
	SETUP 																						  																					\
	ServoMotorController::Ptr controller = controllerFactory.createController(#servoStr, caller); \
																																																\
	controller->setAngle(deg2rad(0)); 															  														\
																																																\
	EXPECT_FALSE((reinterpret_cast<MockSystemCaller*>(caller.get()))->commandReceived.empty());   \
}

#define TEST_hasGoodAngleWhenSetDeg(servoStr, x) 												  											\
TEST(ServoMotorController_##servoStr, hasGoodAngleWhenSet##x##Degrees) { 						  					\
	SETUP 																						  																					\
	ServoMotorController::Ptr controller = controllerFactory.createController(#servoStr, caller); \
																																																\
	controller->setAngle(deg2rad(x)); 															  														\
																																																\
	EXPECT_EQ(x, rad2deg(controller->getAngle())); 												  											\
}

#define TEST_doesntExceedMinMax(servoStr, min, max) 																						\
TEST(ServoMotorController_##servoStr, DoesntExceedMaxWhenAngleSet) { 														\
	SETUP 																																												\
	ServoMotorController::Ptr controller = controllerFactory.createController(#servoStr, caller); \
																																																\
	controller->setAngle(deg2rad(max + 1)); 																											\
 																																																\
	EXPECT_EQ(max, rad2deg(controller->getAngle())); 																							\
} 																																															\
 																																																\
TEST(ServoMotorController_##servoStr, DoesntExceedMinWhenAngleSet) { 														\
	SETUP 																																												\
	ServoMotorController::Ptr controller = controllerFactory.createController(#servoStr, caller); \
 																																																\
	controller->setAngle(deg2rad(min - 1)); 																											\
 																																																\
	EXPECT_EQ(min, rad2deg(controller->getAngle())); 																							\
}

#define TEST_goodCommandWhenAngleSetAtDegree(servoStr, servoNumber, angle, wantedInt) 					\
TEST(ServoMotorController_##servoStr, goodCommandWhenAngleSetAt##angle##Degrees) {							\
	SETUP 																																												\
	ServoMotorController::Ptr controller = controllerFactory.createController(#servoStr, caller); \
 																																																\
	controller->setAngle(deg2rad(angle)); 																												\
																																																\
	std::ostringstream oss;																																				\
	oss << getenv("HOME");																																				\
	oss << "/maestro-linux/UscCmd --servo ";																											\
	oss << servoNumber;																																						\
	oss << ',';																																										\
	oss << wantedInt;																																							\
																																																\
	EXPECT_EQ(oss.str(), CASTMOCK(caller)->commandReceived);																			\
}


//Camera Horizontal

TEST_hasGoodAngleAtInstanciation(cameraHorizontal, 87)

TEST_systemCallerIsCalledWhenAngleSet(cameraHorizontal)

TEST_hasGoodAngleWhenSetDeg(cameraHorizontal, 0)
TEST_hasGoodAngleWhenSetDeg(cameraHorizontal, 45)
TEST_hasGoodAngleWhenSetDeg(cameraHorizontal, 90)
TEST_hasGoodAngleWhenSetDeg(cameraHorizontal, 135)
TEST_hasGoodAngleWhenSetDeg(cameraHorizontal, 180)

TEST_doesntExceedMinMax(cameraHorizontal, 0, 180)

TEST_goodCommandWhenAngleSetAtDegree(cameraHorizontal, 2, 0, 2440)
TEST_goodCommandWhenAngleSetAtDegree(cameraHorizontal, 2, 45, 4214)
TEST_goodCommandWhenAngleSetAtDegree(cameraHorizontal, 2, 90, 5988)
TEST_goodCommandWhenAngleSetAtDegree(cameraHorizontal, 2, 135, 7762)
TEST_goodCommandWhenAngleSetAtDegree(cameraHorizontal, 2, 180, 9536)


//Camera Vertical

TEST_hasGoodAngleAtInstanciation(cameraVertical, 49)

TEST_systemCallerIsCalledWhenAngleSet(cameraVertical)

TEST_hasGoodAngleWhenSetDeg(cameraVertical, 0)
TEST_hasGoodAngleWhenSetDeg(cameraVertical, 45)
TEST_hasGoodAngleWhenSetDeg(cameraVertical, 90)

TEST_doesntExceedMinMax(cameraVertical, 0, 90)

TEST_goodCommandWhenAngleSetAtDegree(cameraVertical, 3, 0, 2244)
TEST_goodCommandWhenAngleSetAtDegree(cameraVertical, 3, 45, 4098)
TEST_goodCommandWhenAngleSetAtDegree(cameraVertical, 3, 90, 5952)


//Prehensor Vertical

TEST_hasGoodAngleAtInstanciation(prehensorVertical, 0)

TEST_systemCallerIsCalledWhenAngleSet(prehensorVertical)

TEST_hasGoodAngleWhenSetDeg(prehensorVertical, 0)
TEST_hasGoodAngleWhenSetDeg(prehensorVertical, 90)

TEST_doesntExceedMinMax(prehensorVertical, 0, 90)

TEST_goodCommandWhenAngleSetAtDegree(prehensorVertical, 5, 0, 3584)
TEST_goodCommandWhenAngleSetAtDegree(prehensorVertical, 5, 90, 5120)


//Prehensor Vertical

TEST_hasGoodAngleAtInstanciation(prehensorHorizontal, 90)

TEST_systemCallerIsCalledWhenAngleSet(prehensorHorizontal)

TEST_hasGoodAngleWhenSetDeg(prehensorHorizontal, 0)
TEST_hasGoodAngleWhenSetDeg(prehensorHorizontal, 90)

TEST_doesntExceedMinMax(prehensorHorizontal, 0, 90)

TEST_goodCommandWhenAngleSetAtDegree(prehensorHorizontal, 4, 0, 1600)
TEST_goodCommandWhenAngleSetAtDegree(prehensorHorizontal, 4, 90, 6080)