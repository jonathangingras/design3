#ifndef _D3T12_PATHPLANNER_H_
#define _D3T12_PATHPLANNER_H_

#include <common/common.h>
#include "RobotPose.h"

namespace d3t12 {

struct PathCommand {
	double x, y, yaw;

	inline PathCommand(double _x, double _y, double _yaw): x(_x), y(_y), yaw(_yaw) {}
	inline RobotPose toRobotPose() {
		return RobotPose(x,y,yaw);
	}
};

class PathPlanner {
public:
	typedef boost::shared_ptr<PathPlanner> Ptr;
	inline PathPlanner() {}

	std::vector<PathCommand> planPath(RobotPose currentPose, RobotPose wantedPose);
};

} //d3t12

#endif