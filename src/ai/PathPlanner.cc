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

/*std::vector<PathCommand> PathPlanner::planPath(RobotPose initialPose, RobotPose finalPose) {
	std::vector<PathCommand> poses;	
	poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));

	if(finalPose.y - 0.40 < 0.1 && initialPose.y - 0.40 < 0.01 && fabs(finalPose.yaw) == M_PI/2) {
		poses.push_back(PathCommand(initialPose.x, initialPose.y + 0.2, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else if(finalPose.y + 0.55 > 1.2 && initialPose.y + 0.40 > 1.2 && fabs(finalPose.yaw) == M_PI/2) {
		poses.push_back(PathCommand(initialPose.x, initialPose.y - 0.2, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else {
		poses.push_back(PathCommand(initialPose.x, finalPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	}

	return poses;
}*/

/*std::vector<PathCommand> PathPlanner::planPath(RobotPose initialPose, RobotPose finalPose) {
	std::vector<PathCommand> poses;	
	poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));
	if(initialPose.x + 0.40 > 2.30) {
		initialPose.x -= 0.4;
		poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));
	}
	if(finalPose.y - initialPose.y < 0.20 && finalPose.yaw == -M_PI/2) {
		poses.push_back(PathCommand(initialPose.x, initialPose.y + 0.2, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else if(finalPose.y - initialPose.y > 0.20 && finalPose.yaw == M_PI/2) {
		poses.push_back(PathCommand(initialPose.x, initialPose.y - 0.2, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else {
		poses.push_back(PathCommand(initialPose.x, finalPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	}

	return poses;
}*/

/*std::vector<PathCommand> PathPlanner::planPath(RobotPose initialPose, RobotPose finalPose) {
	std::vector<PathCommand> poses;	
	poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));
	if(initialPose.x + 0.50 > 2.30) {
		initialPose.x -= 0.4;
		poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));
	}
	if(finalPose.y - initialPose.y < 0.20 && finalPose.yaw == -M_PI/2) {
		initialPose.y += 0.2;
		poses.push_back(PathCommand(initialPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else if(finalPose.y - initialPose.y > 0.20 && finalPose.yaw == M_PI/2) {
		initialPose.y -= 0.2;
		poses.push_back(PathCommand(initialPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else if(finalPose.x - initialPose.x < -0.01) {
		initialPose.x = initialPose.x - 0,4;
		poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));
		poses.push_back(PathCommand(initialPose.x , finalPose.y, initialPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	}else {
		poses.push_back(PathCommand(initialPose.x, finalPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	}

	return poses;
}*/

std::vector<PathCommand> PathPlanner::planPath(RobotPose initialPose, RobotPose finalPose) {
	std::vector<PathCommand> poses;	
	poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));
	if (finalPose.y - 0.35 < 0.01) {
            finalPose.y += 0.15;
	} else if (finalPose.y + 0.15 > 1.12) {
            finalPose.y -= 0.15;
	}
	if(fabs(initialPose.y - finalPose.y) < 0.20 && finalPose.yaw == -M_PI/2) {
		poses.push_back(PathCommand(initialPose.x, initialPose.y + 0.2, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else if(finalPose.y - initialPose.y > 0.20 && finalPose.yaw == M_PI/2) {
		poses.push_back(PathCommand(initialPose.x, initialPose.y - 0.2, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, initialPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else if(finalPose.x - initialPose.x < -0.01) {
		initialPose.x = initialPose.x - 0,4;
		poses.push_back(PathCommand(initialPose.x, initialPose.y, initialPose.yaw));
		poses.push_back(PathCommand(initialPose.x , finalPose.y, initialPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	} else {
		poses.push_back(PathCommand(initialPose.x, finalPose.y, finalPose.yaw));
		poses.push_back(PathCommand(finalPose.x, finalPose.y, finalPose.yaw));
	}

	return poses;
}

} //d3t12