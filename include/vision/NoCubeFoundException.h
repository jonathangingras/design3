#ifndef _D3T12_NOCUBEFOUNDEXCEPTION_H_
#define _D3T12_NOCUBEFOUNDEXCEPTION_H_

#include <common/Exception.h>

namespace d3t12 {

class NoCubeFoundException : public Exception {
public:
    NoCubeFoundException(const char* p_msg) : Exception(p_msg) {}
    NoCubeFoundException(const std::string& p_msg) : Exception(p_msg) {}
};

}

#endif