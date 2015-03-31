#include <fstream>
#include <stdint.h>
#include <stdio.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>
#include <string.h>

struct PololuCommand {
	uint8_t channel;
	unsigned char bytes[4];

	inline void setBytes(uint16_t target) {
		bytes[0] = 0x84;
		bytes[1] = channel;
		bytes[2] = (target & 0x7f);
		bytes[3] = ((target >> 7) & 0x7f);
	}

	inline void writeBytes(unsigned char* _bytes) {
		memcpy(_bytes, bytes, 4);
	}

	inline PololuCommand(uint8_t _channel, uint16_t _target): channel(_channel) {
		setBytes(_target);
	}
};

int maestroGetPosition(int fd, unsigned char channel)
{
unsigned char command[] = {0x90, channel};
if(write(fd, command, sizeof(command)) == -1)
{
perror("error writing");
return -1;
}
unsigned char response[2];
if(read(fd,response,2) != 2)
{
perror("error reading");
return -1;
}
return response[0] + 256*response[1];
}

int main(int argc, char** argv) {
	int fd = open("/dev/ttyACM0", O_RDWR | O_NOCTTY);
	
	if (fd == -1) {
		perror("no file descriptor");
		return 1;
	}

	struct termios options;
	tcgetattr(fd, &options);
	options.c_lflag &= ~(ECHO | ECHONL | ICANON | ISIG | IEXTEN);
	options.c_oflag &= ~(ONLCR | OCRNL);
	tcsetattr(fd, TCSANOW, &options);

	//int position = maestroGetPosition(fd, 3);
	//printf("Current position is %d.\n", position);

	unsigned char command[4];
	PololuCommand(3, 2988).writeBytes(command);
	
	if (write(fd, command, 4*sizeof(unsigned char)) == -1) {
		perror("error writing");
		return -1;
	}
}