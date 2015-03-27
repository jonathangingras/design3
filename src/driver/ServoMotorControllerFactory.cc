#include <driver/ServoMotorControllerFactory.h>

namespace d3t12 {

ServoMotorController::Ptr ServoMotorControllerFactory::createController(const std::string& servoName, SystemCaller::Ptr systemCaller) {
	ServoMotorController* controller = new ServoMotorController;
	controller->command = getenv("HOME");
	controller->command += "/maestro-linux/UscCmd --servo ";

	if(servoName == "prehensorVertical") {
		controller->command += "5,";
		controller->min = 3700;//584;
		controller->max = 5120;
		controller->currentInt = 3584;
		controller->slope = (controller->max - controller->min)/(M_PI/2);
	} else if(servoName == "prehensorHorizontal") {
		controller->command += "4,";
		controller->min = 1600;
		controller->max = 6080;
		controller->currentInt = 6080;
		controller->slope = (controller->max - controller->min)/(M_PI/2);
	} else if(servoName == "cameraVertical") {
		controller->command += "3,";
		controller->min = 2244;
		controller->max = 5952;
		controller->currentInt = 4268;
		controller->slope = (controller->max - controller->min)/(M_PI/2);
	} else if(servoName == "cameraHorizontal") {
		controller->command += "2,";
		controller->min = 2440;
		controller->max = 9536;
		controller->currentInt = 5896;
		controller->slope = (controller->max - controller->min)/M_PI;
	}

	controller->systemCaller = systemCaller;
	return ServoMotorController::Ptr(controller);
}

ServoMotorController::Ptr ServoMotorControllerFactory::createController(const std::string& servoName) {
	return createController(servoName, SystemCaller::Ptr(new SystemCaller));
}

}