#ifndef _SYSTEMCALLER_H_
#define _SYSTEMCALLER_H_

#include <boost/smart_ptr.hpp>
#include <unistd.h>
#include <stdio.h>

namespace d3t12 {

struct SystemCaller {
	typedef boost::shared_ptr<SystemCaller> Ptr;

	inline SystemCaller() {}

	virtual void call(const std::string& command);
};

}

#endif