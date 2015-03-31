#ifndef _D3T12_JOURNEYSTATE_H_
#define _D3T12_JOURNEYSTATE_H_

#include <vector>
#include <common/commonEssentials.h>
#include "JourneyBackPack.h"

namespace d3t12 {

class JourneyState {
friend class JourneyStateFactory;
protected:
	JourneyBackPack::Ptr backpack;

public:
	typedef boost::shared_ptr<JourneyState> Ptr;
	typedef std::vector<JourneyState::Ptr> PtrVector;
	
	virtual void run() = 0;
};

}

#endif