#include <RosQtExitGuard.h>

namespace d3t12 {

void RosQtExitGuard::operator()() {
	ROS_INFO("Going to shutdown node");
	nodeHandle.shutdown();
	qtApp->quit();
}

bool RosQtExitGuard::good() {
	return nodeHandle.ok();
}

}