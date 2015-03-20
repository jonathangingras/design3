#include <driver/MicroControllerCommandPort.h>

namespace d3t12 {

void MicroControllerCommandPort::operator << (MicroControllerCommand command) {
	mutex.lock();
	*serialPort << command.command;
	serialPort->flush();
	mutex.unlock();
}

}