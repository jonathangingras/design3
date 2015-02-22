#ifndef _D3T12_SIGINT_HANDLER_H_
#define _D3T12_SIGINT_HANDLER_H_

#include "commonEssentials.h"
#include "SignalFunctor.h"

namespace d3t12 {

class SIGINTHandler {
private:
	static SIGINTHandler* self;
	static SignalFunctor::Ptr handler;
	
	static void handleSignal(int signal);
	void catchSignal();

	inline SIGINTHandler() {}

public:
	~SIGINTHandler();

	static SIGINTHandler& getInstance();
	void setSignalHandler(SignalFunctor::Ptr _handler);
};

}

#endif