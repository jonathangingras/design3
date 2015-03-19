#ifndef _D3T12_SERVOMOTORCONTROLLER_H_
#define _D3T12_SERVOMOTORCONTROLLER_H_

#include <boost/smart_ptr.hpp>
#include "MicroControllerCommandPort.h"

namespace d3t12 {

class ServoMotorController {
friend class ServoMotorControllerFactory;

private:
	MicroControllerCommandPort::Ptr port;

public:
	typedef boost::shared_ptr<ServoMotorController> Ptr;

	void setAngle(float angle);
	void operator += (float angle);
	void operator -= (float angle);
};

} //d3t12

#endif