#ifndef _D3T12_MICROCONTROLLERCOMMANDPORT_H_
#define _D3T12_MICROCONTROLLERCOMMANDPORT_H_

#include <fstream>
#include <boost/smart_ptr.hpp>
#include <boost/thread.hpp>
#include "MicroControllerCommand.h"

namespace d3t12 {

class MicroControllerCommandPort {
public:
	typedef boost::shared_ptr<std::ostream> OStreamPtr;
	typedef boost::shared_ptr<MicroControllerCommandPort> Ptr;
	
private:
	OStreamPtr serialPort;
	boost::mutex mutex;

public:
	inline MicroControllerCommandPort(OStreamPtr _serialPort): serialPort(_serialPort) {}

	~MicroControllerCommandPort() {}

	void operator << (MicroControllerCommand command);
	void operator << (std::string command);
};

} //d3t12

#endif