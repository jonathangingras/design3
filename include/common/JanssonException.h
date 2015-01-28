#ifndef _D3T12_JANSSONEXCEPTION_H_
#define _D3T12_JANSSONEXCEPTION_H_

#include <common/Exception.h>

namespace d3t12 {

class JanssonException : public Exception {
public:
    JanssonException(const char* p_msg) : Exception(p_msg) {}
    JanssonException(const std::string& p_msg) : Exception(p_msg) {}
};

}

#endif