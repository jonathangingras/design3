#ifndef _D3T12_COMMONESSENTIALS_H_
#define _D3T12_COMMONESSENTIALS_H_

#include <signal.h>
#include <vector>
#include <string>
#include <iostream>
#include <boost/smart_ptr.hpp>
#include <math.h>

namespace d3t12 {
	typedef boost::shared_ptr<std::string> StringPtr;
	typedef std::vector<StringPtr> StringPtrVector;
}

#endif