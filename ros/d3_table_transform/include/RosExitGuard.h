#ifndef _ROSEXITGUARD_H_
#define _ROSEXITGUARD_H_

#include <ros/ros.h>
#include <common/SIGINTHandler.h>

namespace d3t12 {

struct RosExitGuard : public d3t12::SignalFunctor {
	::ros::NodeHandle& nodeHandle;
	
	inline RosExitGuard(::ros::NodeHandle& _nodeHandle): nodeHandle(_nodeHandle) {}

	virtual void operator()();
	virtual bool good();
};

}

#endif