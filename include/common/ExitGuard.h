#ifndef _D3T12_EXITGUAD_H_
#define _D3T12_EXITGUAD_H_

#include "commonEssentials.h"
#include "SignalFunctor.h"

namespace d3t12 {

struct ExitGuard : public SignalFunctor {
    inline ExitGuard(): done(false) {}

    bool done;

    virtual void operator()();
    virtual bool good();
};

}

#endif