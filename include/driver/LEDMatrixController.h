#ifndef _D3T12_LEDMATRIXCONTROLLER_H_
#define _D3T12_LEDMATRIXCONTROLLER_H_

#include <driver/MicroControllerCommandPort.h>
#include <driver/MicroControllerCommandBuilder.h>

namespace d3t12 {

class LEDMatrixController {
private:
	class LEDMatrixOrderList {
	private:
		const int indices[9];
		int currentIndex;

	public:
		inline int next() {
			if(currentIndex == 8) {
				currentIndex = -1;
			}
			return indices[++currentIndex];
		}

		inline int cancelCurrent() {
			if(currentIndex == -1) {
				currentIndex = 0;
			}
			return indices[currentIndex--];
		}

		inline int current() {
			return indices[currentIndex];
		}

		inline LEDMatrixOrderList(): 
			currentIndex(-1), indices({7,8,9,4,5,6,1,2,3}) {} //produces a warning, but wont add necessary flag 
			                                                  //to CMAKE_CXX_FLAGS, because -std=c++0x in confict with gmock
	};

	LEDMatrixOrderList orderList;
	MicroControllerCommandPort::Ptr commandPort;
	MicroControllerLEDCommandBuilder commandBuilder;

public:
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