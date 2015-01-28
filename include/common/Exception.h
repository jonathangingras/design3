#ifndef _D3T12_EXCEPTION_H_
#define _D3T12_EXCEPTION_H_

#include <stdexcept>

namespace d3t12 {

class Exception : public std::exception {
public:
    explicit Exception(const char* p_msg) : message(p_msg) {}
    explicit Exception(const std::string& p_msg) : message(p_msg) {}

    virtual ~Exception() throw() {}

    virtual const char* what() const throw() {
       return message.c_str();
    }

protected:
    std::string message;
};

}

#endif