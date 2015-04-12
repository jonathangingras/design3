#include <driver/LEDMatrixController.h>

namespace d3t12 {

void LEDMatrixController::turnMasterOn() {
	*commandPort << commandBuilder.setLED(0).setPower(true).build();
}

void LEDMatrixController::turnMasterOff() {
	*commandPort << commandBuilder.setLED(0).setPower(false).build();
}

void LEDMatrixController::addNew(const std::string& colorStr) {
	*commandPort << commandBuilder.setLED(orderList->current()).setColor(colorStr).build();

	++added;
	if(added > 9) {
		added -= 9;
	}

	orderList->increase();
}

void LEDMatrixController::addBlank() {
	orderList->increase();
}

void LEDMatrixController::removeCurrent() {
	orderList->cancelCurrent();
	*commandPort << commandBuilder.setLED(orderList->current()).setPower(false).build();
}

void LEDMatrixController::turnAllOff() {
	for(int i = 0; i < 10; ++i) {
		*commandPort << commandBuilder.setLED(i).setPower(false).build();
	}
}

}