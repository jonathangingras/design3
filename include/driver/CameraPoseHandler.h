#ifndef _D3T12_CAMERAPOSEHANDLER_H_
#define _D3T12_CAMERAPOSEHANDLER_H_

#include "ServoMotorControllerFactory.h"

namespace d3t12 {

class CameraPoseHandler {
private:
	ServoMotorController::Ptr verticalController;
	ServoMotorController::Ptr horizontalController;

public:
	CameraPoseHandler();

	void increasePitch(double angle);
	void decreasePitch(double angle);
	void setPitch(double angle);
	double getPitch();

	void increaseYaw(double angle);
	void decreaseYaw(double angle);
	void setYaw(double angle);
	double getYaw();
};

}

#endif