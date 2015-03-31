#include <driver/MotorController.h>

namespace d3t12 {

void MotorController::informPosition(float x, float y, float yaw) {
	*commandPort << commandBuilder.setCurrentPosition(x, y, yaw).build();
}

void MotorController::commandPosition(float x, float y, float yaw) {
	*commandPort << commandBuilder.setWantedPosition(x, y, yaw).build();
}

void MotorController::moveTo(float x, float y) {
	std::ostringstream oss;
	oss << "move " << x << ' ' << y;
	*commandPort << oss.str();
}

void MotorController::rotate(float yaw) {
	std::ostringstream oss;
	oss << "rot " << yaw;
	*commandPort << oss.str();
}

}