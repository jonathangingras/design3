#ifndef _D3T12_BADCOLORSTRINGEXCEPTION_H_
#define _D3T12_BADCOLORSTRINGEXCEPTION_H_

#include <common/Exception.h>

namespace d3t12 {

class BadColorStringException : public Exception {
public:
    BadColorStringException(const char* p_msg) : Exception(p_msg) {}
    BadColorStringException(const std::string& p_msg) : Exception(p_msg) {}
};

}

#endif