#include <driver/MicroControllerCommandBuilder.h>

namespace d3t12 {

MicroControllerLEDCommandBuilder& MicroControllerLEDCommandBuilder::setLED(int _ledNumber) {
	ledNumber = _ledNumber;
	on = true;
	colorStr = "";
	return *this;
}

MicroControllerLEDCommandBuilder& MicroControllerLEDCommandBuilder::setColor(std::string _colorStr) {
	colorStr = _colorStr;
	return *this;
}

MicroControllerLEDCommandBuilder& MicroControllerLEDCommandBuilder::setPower(bool _on) {
	on = _on;
	return *this;
}

std::string MicroControllerLEDCommandBuilder::getControllerColorStr() const {
	if(colorStr == "white") {
		return "w";
	}
	if(colorStr == "black") {
		return "bk";
	}
	if(colorStr == "red") {
		return "r";
	}
	if(colorStr == "green") {
		return "g";
	}
	if(colorStr == "blue") {
		return "b";
	}
	if(colorStr == "yellow") {
		return "y";
	}
	return "";
}

MicroControllerCommand MicroControllerLEDCommandBuilder::build() {
	std::ostringstream commandStream;
	if(ledNumber == 0) {
		commandStream << "setled " << (on ? "on" : "off") << '\n';
	} else {
		commandStream << "setledrgb " << ledNumber << ' ' << (on ? getControllerColorStr() : "x") << '\n';
	}
	return createCommand(commandStream.str());
}


MicroControllerMotorControlCommandBuilder& MicroControllerMotorControlCommandBuilder::setCurrentPosition(float _x, float _y, float _yaw) {
	state = current;
	setPosition(_x, _y, _yaw);
	return *this;
}

MicroControllerMotorControlCommandBuilder& MicroControllerMotorControlCommandBuilder::setWantedPosition(float _x, float _y, float _yaw) {
	state = wanted;
	setPosition(_x, _y, _yaw);
	return *this;
}

MicroControllerCommand MicroControllerMotorControlCommandBuilder::build() {
	std::ostringstream commandStream;
	commandStream << (state == current ? "setpos " : "goto " )
				  << x << ' '
				  << y << ' '
				  << yaw << '\n';
	return createCommand(commandStream.str());
}

} //d3t12