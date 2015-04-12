#ifndef _D3T12_JOURNEYSCHEDULER_H_
#define _D3T12_JOURNEYSCHEDULER_H_

#include "JourneyState.h"

namespace d3t12 {

class JourneyScheduler {
private:
	JourneyState::Ptr currentState;
	JourneyState::PtrVector states;

public:
	inline JourneyScheduler() {}
};

}

#endif