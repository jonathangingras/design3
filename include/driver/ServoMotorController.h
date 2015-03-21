#ifndef _D3T12_SERVOMOTORCONTROLLER_H_
#define _D3T12_SERVOMOTORCONTROLLER_H_

#include <string>
#include <sstream>
#include <math.h>
#include <boost/smart_ptr.hpp>
#include <common/SystemCaller.h>

namespace d3t12 {

class ServoMotorController {
friend class ServoMotorControllerFactory;

private:
	SystemCaller::Ptr systemCaller;
	std::string command;
	
	int currentInt;

	double slope;
	double min;
	double max;

	inline ServoMotorController() {}
	void sendCommand();

public:
	typedef boost::shared_ptr<ServoMotorController> Ptr;

	double getAngle();
	void setAngle(double angle);
	void operator += (double angle);
	void operator -= (double angle);
};

} //d3t12

#endif