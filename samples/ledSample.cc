#include <driver/driver.h>
#include <unistd.h>

int main(int argc, char **argv) {
	d3t12::MicroControllerCommandPort portu(d3t12::MicroControllerCommandPort::OStreamPtr(new std::ofstream("/dev/ttyACM2")));
	d3t12::MicroControllerLEDCommandBuilder ledCommandbuilder;

	portu << ledCommandbuilder.setLED(0).setPower(true).build();
	sleep(2);
	portu << ledCommandbuilder.setLED(1).setColor("green").build();
	sleep(2);
	portu << ledCommandbuilder.setLED(2).setColor("red").build();
	sleep(2);
	portu << ledCommandbuilder.setLED(3).setColor("blue").build();
	sleep(2);
	portu << ledCommandbuilder.setLED(4).setColor("white").build();
	sleep(2);
	portu << ledCommandbuilder.setLED(5).setColor("black").build();


	return 0;
}