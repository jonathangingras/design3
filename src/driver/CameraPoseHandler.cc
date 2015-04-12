#include <driver/CameraPoseHandler.h>

namespace d3t12 {

CameraPoseHandler::CameraPoseHandler() {
	ServoMotorControllerFactory factory;
	verticalController = factory.createController("cameraVertical");
	horizontalController = factory.createController("cameraHorizontal");
}

void CameraPoseHandler::increasePitch(double angle) {
	*verticalController += angle;
}

void CameraPoseHandler::decreasePitch(double angle) {
	*verticalController -= angle;
}

void CameraPoseHandler::setPitch(double angle) {
	verticalController->setAngle(angle);
}

double CameraPoseHandler::getPitch() {
	return verticalController->getAngle();
}

void CameraPoseHandler::increaseYaw(double angle) {
	*horizontalController += angle;
}

void CameraPoseHandler::decreaseYaw(double angle) {
	*horizontalController -= angle;
}

void CameraPoseHandler::setYaw(double angle) {
	horizontalController->setAngle(angle);
}

double CameraPoseHandler::getYaw() {
	return horizontalController->getAngle();
}

} //d3t12