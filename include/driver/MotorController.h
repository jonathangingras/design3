#ifndef _D3T12_MOTORCONTROLLER_H_
#define _D3T12_MOTORCONTROLLER_H_

#include <driver/MicroControllerCommandPort.h>
#include <driver/MicroControllerCommandBuilder.h>

namespace d3t12 {

class MotorController {
private:
	MicroControllerCommandPort::Ptr commandPort;
	MicroControllerMotorControlCommandBuilder commandBuilder;

public:
	inline MotorController(MicroControllerCommandPort::Ptr _commandPort): 
		commandPort(_commandPort) {}

	void informPosition(float x, float y, float yaw);
	void commandPosition(float x, float y, float yaw);
};

}

#endif