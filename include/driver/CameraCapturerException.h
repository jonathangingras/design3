#ifndef _D3T12_CAMERACAPTUREREXCEPTION_H_
#define _D3T12_CAMERACAPTUREREXCEPTION_H_

#include <common/Exception.h>

namespace d3t12 {

class CameraCapturerException : public Exception {
public:
    CameraCapturerException(const char* p_msg) : Exception(p_msg) {}
    CameraCapturerException(const std::string& p_msg) : Exception(p_msg) {}
};

}

#endif