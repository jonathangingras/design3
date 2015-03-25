#include <driver/Prehensor.h>

namespace d3t12 {

Prehensor::Prehensor() {
	ServoMotorControllerFactory factory;
	verticalController = factory.createController("prehensorVertical");
	horizontalController = factory.createController("prehensorHorizontal");
}

void Prehensor::open() {
	horizontalController->setAngle(0);
}

void Prehensor::close() {
	horizontalController->setAngle(90);
}

void Prehensor::rise() {
	verticalController->setAngle(0);
}

void Prehensor::lower() {
	verticalController->setAngle(90);
}

}