#ifndef _D3T12_LEDMATRIXCONTROLLER_H_
#define _D3T12_LEDMATRIXCONTROLLER_H_

#include <driver/MicroControllerCommandPort.h>
#include <driver/MicroControllerCommandBuilder.h>
#include <common/LEDMatrixOrderList.h>

namespace d3t12 {

class LEDMatrixController {
private:
	LEDMatrixOrderList orderList;
	MicroControllerCommandPort::Ptr commandPort;
	MicroControllerLEDCommandBuilder commandBuilder;

public:
	typedef boost::shared_ptr<LEDMatrixController> Ptr;
	inline LEDMatrixController(MicroControllerCommandPort::Ptr _commandPort): 
		commandPort(_commandPort) {}

	void turnMasterOn();
	void turnMasterOff();

	void addNew(const std::string& colorStr);
	void addBlank();
	void removeCurrent();

	inline bool matrixFilled() {
		return orderList.current() == 3;
	}

	void turnAllOff();
};

}

#endif