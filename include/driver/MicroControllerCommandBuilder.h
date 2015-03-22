#ifndef _D3T12_MICROCONTROLLERCOMMANDBUILDER_H_
#define _D3T12_MICROCONTROLLERCOMMANDBUILDER_H_

#include <sstream>
#include <boost/smart_ptr.hpp>
#include "MicroControllerCommand.h"

namespace d3t12 {

class MicroControllerCommandBuilder {
protected:
	inline MicroControllerCommand createCommand(const std::string& command) {
		return MicroControllerCommand(command);
	}

public:
	virtual MicroControllerCommand build() = 0;
};

class MicroControllerLEDCommandBuilder : public MicroControllerCommandBuilder {
private:
	int ledNumber;
	std::string colorStr;
	bool on;

	std::string getControllerColorStr() const;
public:
	inline MicroControllerLEDCommandBuilder(): ledNumber(-1), on(true) {};

	MicroControllerLEDCommandBuilder& setLED(int _ledNumber);
	MicroControllerLEDCommandBuilder& setColor(std::string _colorStr);
	MicroControllerLEDCommandBuilder& setPower(bool on);

	MicroControllerCommand build();
};

class MicroControllerMotorControlCommandBuilder : public MicroControllerCommandBuilder {
private:
	typedef enum {current = 0, wanted} State;

	State state;
	float x, y, yaw;

	inline void setPosition(float _x, float _y, float _yaw) {
		x = _x; y = _y; yaw = _yaw; 
	}
public:
	inline MicroControllerMotorControlCommandBuilder() {};

	MicroControllerMotorControlCommandBuilder& setCurrentPosition(float _x, float _y, float _yaw);
	MicroControllerMotorControlCommandBuilder& setWantedPosition(float _x, float _y, float _yaw);

	MicroControllerCommand build();
};

}

#endif