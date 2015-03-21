#include <driver/ServoMotorController.h>

namespace d3t12 {

void ServoMotorController::sendCommand() {
	std::ostringstream os;
	os << command << currentInt;
	systemCaller->call(os.str());
}

double ServoMotorController::getAngle() {
	return ((double)currentInt - min)/slope;
}

void ServoMotorController::setAngle(double angle) {
	double correspondingInt = slope*angle + min;
	if(correspondingInt <= min) {
		currentInt = min;
	} else if(correspondingInt >= max) {
		currentInt = max;
	} else {
		currentInt = correspondingInt;
	}

	sendCommand();
}

void ServoMotorController::operator += (double angle) {
	setAngle(getAngle() + angle);
}

void ServoMotorController::operator -= (double angle) {
	setAngle(getAngle() - angle);
}

}