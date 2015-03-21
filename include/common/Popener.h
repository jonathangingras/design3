#ifndef _D3T12_POPENER_H_
#define _D3T12_POPENER_H_

#include <stdlib.h>
#include <stdio.h>
#include <string>

namespace d3t12 {

class Popener {
public:
	inline Popener() {}
	virtual std::string popen(const std::string&) const;
};

}

#endif