#ifndef _D3T12_SERVOMOTORCONTROLLERFACTORY_H_
#define _D3T12_SERVOMOTORCONTROLLERFACTORY_H_

#include <common/SystemCaller.h>
#include "ServoMotorController.h"

namespace d3t12 {

class ServoMotorControllerFactory {
public:
	inline ServoMotorControllerFactory() {}

	ServoMotorController::Ptr createController(const std::string& servoName, SystemCaller::Ptr systemCaller);
	ServoMotorController::Ptr createController(const std::string& servoName);
};

}

#endif