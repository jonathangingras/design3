#ifndef _D3T12_BADANSWEREXCEPTION_H_
#define _D3T12_BADANSWEREXCEPTION_H_

#include <common/common.h>

namespace d3t12 {

class BadAnswerException : public Exception {
public:
	BadAnswerException(const std::string& msg): Exception(msg) {}
};

} //d3t12

#endif