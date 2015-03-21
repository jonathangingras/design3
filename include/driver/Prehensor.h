#ifndef _D3T12_PREHENSOR_H_
#define _D3T12_PREHENSOR_H_

#include "ServoMotorControllerFactory.h"

namespace d3t12 {

class Prehensor {
private:
	ServoMotorController::Ptr verticalController;
	ServoMotorController::Ptr horizontalController;

public:
	Prehensor();

	void open();
	void close();
	void rise();
	void lower();
};

}

#endif