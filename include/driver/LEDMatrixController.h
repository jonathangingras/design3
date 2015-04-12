#ifndef _D3T12_LEDMATRIXCONTROLLER_H_
#define _D3T12_LEDMATRIXCONTROLLER_H_

#include <driver/MicroControllerCommandPort.h>
#include <driver/MicroControllerCommandBuilder.h>
#include <common/LEDMatrixOrderList.h>

namespace d3t12 {

class LEDMatrixController {
private:
	LEDMatrixOrderList::Ptr orderList;
	MicroControllerCommandPort::Ptr commandPort;
	MicroControllerLEDCommandBuilder commandBuilder;
	int added;

public:
	typedef boost::shared_ptr<LEDMatrixController> Ptr;
	inline LEDMatrixController(MicroControllerCommandPort::Ptr _commandPort): 
		commandPort(_commandPort), orderList(new LEDMatrixOrderList), added(0) {}

	void turnMasterOn();
	void turnMasterOff();

	virtual void addNew(const std::string& colorStr);
	virtual void addBlank();
	virtual void removeCurrent();

	inline bool matrixFilled() {
		return orderList->current() == 7 && added;
	}

	inline LEDMatrixOrderList::Ptr getOrderList() {
		return orderList;
	}

	inline void reset() {
		orderList->reset();
		added = 0;
		turnAllOff();
	}

	virtual void turnAllOff();
};

}

#endif