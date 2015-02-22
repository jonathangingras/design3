#include <RosExitGuard.h>

namespace d3t12 {

void RosExitGuard::operator()() {
	ROS_INFO("Going to shutdown node");
	nodeHandle.shutdown();
}

bool RosExitGuard::good() {
	return nodeHandle.ok();
}

}