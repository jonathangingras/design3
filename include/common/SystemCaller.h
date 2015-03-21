#ifndef _SYSTEMCALLER_H_
#define _SYSTEMCALLER_H_

#include <boost/smart_ptr.hpp>
#include <unistd.h>

namespace d3t12 {

struct SystemCaller {
	typedef boost::shared_ptr<SystemCaller> Ptr;

	inline SystemCaller() {}

	virtual void call(const std::string& command);
};

}

#endif