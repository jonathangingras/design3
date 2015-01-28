#ifndef _D3T12_CURLEXCEPTION_H_
#define _D3T12_CURLEXCEPTION_H_

#include <common/Exception.h>

namespace d3t12 {

class CURLException : public Exception {
public:
    CURLException(const char* p_msg) : Exception(p_msg) {}
    CURLException(const std::string& p_msg) : Exception(p_msg) {}
};

}

#endif