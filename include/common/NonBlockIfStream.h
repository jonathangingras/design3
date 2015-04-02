#ifndef _D3T12_NONBLOCKIFSTREAM_H_
#define _D3T12_NONBLOCKIFSTREAM_H_

#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

#include <string>

namespace d3t12 {

class NonBlockIfStream {
private:
	int fileDescriptor;

public:
	inline NonBlockIfStream(const std::string& file) {
		fileDescriptor = open(file.c_str(), O_RDWR | O_NONBLOCK);
	}

	virtual ~NonBlockIfStream() {
		close(fileDescriptor);
	}

	friend void operator >> (NonBlockIfStream& nbifstream, std::string& outStr);
};

inline void operator >> (NonBlockIfStream& nbifstream, std::string& outStr) {
	signed char c;

	while(read(nbifstream.fileDescriptor, &c, 1) > 0) {
		outStr += c;
	}
}

} //d3t12

#endif