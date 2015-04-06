#include <ai/PathPlanner.h>

namespace d3t12 {

PathCommand PathPlanner::planPathAngle(RobotPose initialPose, RobotPose finalPose) {
	double finalYaw = 0.0;
    
    if(finalPose.y - 0.30 < 0.01) {
      	finalYaw = M_PI / 2;
        finalPose.y += 0.05;
    } else if(finalPose.y - 0.40 < 0.01 && finalPose.x <= 0.20) {
        finalYaw = M_PI / 2;
        finalPose.y += 0.05;
	} else if(finalPose.y + 0.30 > 1.10) {
        finalYaw = -M_PI / 2;
        finalPose.y -= 0.05;
	} else if(finalPose.x - initialPose.x < -0.01) {
        finalYaw = M_PI;
	}

    return PathCommand(0,0,finalYaw);
}

std::vector<PathCommand> PathPlanner::planPath(RobotPose initialPose, RobotPose finalPose) {
	std::vector<PathCommand> poses;	
	poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));
	double finalYaw = 0.0;

	if(finalPose.y - 0.3 < 0.01 || (finalPose.y - 0.40 < 0.01 && finalPose.x <= 0.20)) {
		finalYaw = M_PI/2;
		finalPose.y += 0.05;
	} else if(finalPose.y + 0.30 > 1.10) {
		finalYaw = -M_PI/2;
		finalPose.y -= 0.05;
	} else if(finalPose.x - initialPose.x < -0.01) {
		finalYaw = M_PI;
	}

	if(finalPose.y - 0.55 < 0.1 && initialPose.y - 0.55 < 0.01 && fabs(finalYaw) == M_PI/4) {
		poses.push_back(PathCommand(initialPose.x, initialPose.y + 0.3, finalYaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalYaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalYaw));
	} else if(finalPose.y + 0.55 > 1.2 && initialPose.y + 0.55 > 1.2 && fabs(finalYaw) == M_PI/4) {
		poses.push_back(PathCommand(initialPose.x, initialPose.y - 0.3, finalYaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalYaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalYaw));
	} else {
		poses.push_back(PathCommand(initialPose.x, finalPose.y, finalYaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalYaw));
	}

	return poses;
}

} //d3t12