#include <driver/Prehensor.h>

namespace d3t12 {

Prehensor::Prehensor() {
	ServoMotorControllerFactory factory;
	verticalController = factory.createController("prehensorVertical");
	horizontalController = factory.createController("prehensorHorizontal");
}

void Prehensor::waitUntilDone() {
	sleepSecondsNanoSeconds(0, 500000000);
}

void Prehensor::open() {
	horizontalController->setAngle(0);
	waitUntilDone();
}

void Prehensor::close() {
	horizontalController->setAngle(90);
	waitUntilDone();
}

void Prehensor::rise() {
	verticalController->setAngle(0);
	waitUntilDone();
}

void Prehensor::lower() {
	verticalController->setAngle(90);
	waitUntilDone();
}

}