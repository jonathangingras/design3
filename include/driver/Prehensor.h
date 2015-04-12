#ifndef _D3T12_PREHENSOR_H_
#define _D3T12_PREHENSOR_H_

#include <common/common.h>
#include "ServoMotorControllerFactory.h"

namespace d3t12 {

class Prehensor {
private:
	ServoMotorController::Ptr verticalController;
	ServoMotorController::Ptr horizontalController;

	void waitUntilDone();

public:
	typedef boost::shared_ptr<Prehensor> Ptr;
	Prehensor();

	virtual void open();
	virtual void close();
	virtual void rise();
	virtual void lower();
};

}

#endif