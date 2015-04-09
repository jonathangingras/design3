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
	orderList->increase();
}

void LEDMatrixController::addBlank() {
	orderList->increase();
}

void LEDMatrixController::removeCurrent() {
	*commandPort << commandBuilder.setLED(orderList->current()).setPower(false).build();
	orderList->cancelCurrent();
}

void LEDMatrixController::turnAllOff() {
	for(int i = 0; i < 10; ++i) {
		*commandPort << commandBuilder.setLED(i).setPower(false).build();
	}
}

}