#include <driver/ServoMotorControllerFactory.h>

namespace d3t12 {

ServoMotorController::Ptr ServoMotorControllerFactory::createController(const std::string& servoName, SystemCaller::Ptr systemCaller) {
	ServoMotorController* controller = new ServoMotorController;
	controller->command = getenv("HOME");
	controller->command += "/maestro-linux/UscCmd --servo ";

	if(servoName == "prehensorVertical") {
		controller->channel = 5;
		controller->min = 2500;
		controller->forcedMin = 2500;
		controller->max = 5500;
		controller->currentInt = 5500;
		controller->slope = (controller->max - controller->min)/(M_PI/2);
	} else if(servoName == "prehensorHorizontal") {
		controller->channel = 4;
		controller->min = 1600;
		controller->forcedMin = 1600;
		controller->max = 8000;
		controller->currentInt = 8000;
		controller->slope = (controller->max - controller->min)/(M_PI/2);
	} else if(servoName == "cameraVertical") {
		controller->channel = 3;
		controller->min = 2244;
		controller->max = 5952;
		controller->currentInt = 4268;
		controller->slope = (controller->max - controller->min)/(M_PI/2);
		//next one is because tag confilcts with white
		controller->forcedMin = 2244;//3950;
	} else if(servoName == "cameraHorizontal") {
		controller->channel = 2;
		controller->min = 2440;
		controller->forcedMin = 2440;
		controller->max = 9536;
		controller->currentInt = 5988;
		controller->slope = (controller->max - controller->min)/M_PI;
	}

	controller->systemCaller = systemCaller;
	return ServoMotorController::Ptr(controller);
}

ServoMotorController::Ptr ServoMotorControllerFactory::createController(const std::string& servoName) {
	return createController(servoName, SystemCaller::Ptr(new SystemCaller));
}

}