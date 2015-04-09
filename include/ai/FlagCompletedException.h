#ifndef _D3T12_FLAGCOMPLETEDEXCEPTION_H_
#define _D3T12_FLAGCOMPLETEDEXCEPTION_H_

#include <common/common.h>

namespace d3t12 {

class FlagCompletedException : public Exception {
public:
	FlagCompletedException(const std::string& msg): Exception(msg) {}
};

} //d3t12

#endif