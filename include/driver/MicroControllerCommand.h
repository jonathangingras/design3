#ifndef _D3T12_MICROCONTROLLERCOMMAND_H_
#define _D3T12_MICROCONTROLLERCOMMAND_H_

#include <boost/smart_ptr.hpp>

namespace d3t12 {

class MicroControllerCommand {
friend class MicroControllerCommandBuilder;
friend class MicroControllerCommandPort;

private:
	std::string command;

	inline MicroControllerCommand(std::string _command): command(_command) {}
};

} //d3t12

#endif