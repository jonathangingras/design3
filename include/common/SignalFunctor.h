#ifndef _D3T12_SIGNALFUNCTOR_H_
#define _D3T12_SIGNALFUNCTOR_H_

#include "commonEssentials.h"

namespace d3t12 {

struct SignalFunctor {
	typedef boost::shared_ptr<SignalFunctor> Ptr;
	
	virtual void operator()() = 0;

	virtual bool good() = 0;
};

}

#endif