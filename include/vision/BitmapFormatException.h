#ifndef _D3T12_BITMAPFORMATEXCEPTION_H_
#define _D3T12_BITMAPFORMATEXCEPTION_H_

#include <common/Exception.h>

namespace d3t12 {

class BitmapFormatException : public Exception {
public:
    BitmapFormatException(const char* p_msg) : Exception(p_msg) {}
    BitmapFormatException(const std::string& p_msg) : Exception(p_msg) {}
};

}

#endif