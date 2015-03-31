#include <ai/PathPlanner.h>

namespace d3t12 {

std::vector<PathCommand> PathPlanner::planPath(RobotPose currentPose, RobotPose wantedPose) {
	std::vector<PathCommand> commandVector;
	double distanceXBetweenRobotAndWantedPose = wantedPose.x - currentPose.x;
	double distanceYBetweenRobotAndWantedPose = wantedPose.y - currentPose.y;
	bool isWantedPoseNearLeftWall = false;
	bool isWantedPoseNearRightWall = false;
	bool isRobotPoseNearLeftWall = false;
	bool isRobotPoseNearRightWall = false;
	
	// this is the secured buffer zone for the wantedPose approach
	if(wantedPose.y + 0.30 >= 1.10) {
		isWantedPoseNearLeftWall = true;
	}
	else if(wantedPose.y - 0.3 <= 0) {
		isWantedPoseNearRightWall = true;
	}
	// this is the secure buffer zone for the robot rotation command 
	if(currentPose.y + 0.30 >= 1.10) {
		isRobotPoseNearLeftWall = true;
	}
	else if(currentPose.y - 0.3 <= 0) {
		isRobotPoseNearRightWall = true;
	}
	
	//this section is for the command decision ordering

	if( distanceXBetweenRobotAndWantedPose < 0 && fabs(currentPose.yaw - M_PI) > 0.01 ) {
		if(isRobotPoseNearLeftWall) {
			commandVector.push_back(PathCommand(0,0, - M_PI - currentPose.yaw ));//"move 0 0 (Robot.angle - 180)"
		} 
		else if(isRobotPoseNearRightWall) {
			commandVector.push_back(PathCommand(0,0, M_PI - currentPose.yaw));//"move 0 0 (180 - Robot.angle)"
		}
		else {
			commandVector.push_back(PathCommand(0,0, currentPose.yaw - M_PI)); //"move 0 0 (Robot.angle - 180)"
		}
	}
		
	else if( distanceXBetweenRobotAndWantedPose > 0 && fabs(currentPose.yaw) > 0.01 ) {
		if(isRobotPoseNearLeftWall) {
			commandVector.push_back(PathCommand(0,0, M_PI - currentPose.yaw));//"move 0 0 (180 - currentPose.angle)"
		}
		else if(isRobotPoseNearRightWall) {
			commandVector.push_back(PathCommand(0,0, currentPose.yaw - M_PI));//"move 0 0 (currentPose.angle - 180)"
		}
		else {
			commandVector.push_back(PathCommand(0,0, M_PI - currentPose.yaw));//"move 0 0 (180 - currentPose.angle)"
		}
	}
	
	if(!isWantedPoseNearLeftWall && !isWantedPoseNearRightWall) {
		commandVector.push_back(PathCommand(fabs(distanceXBetweenRobotAndWantedPose), -distanceYBetweenRobotAndWantedPose, 0));//"move absolute(distanceXBetweenRobotAndWantedPose) -(distanceYBetweenRobotAndWantedPose) 0 "
	}
	
	else {
		commandVector.push_back(PathCommand(fabs(distanceXBetweenRobotAndWantedPose), 0, 0));//"move absolute(distanceXBetweenRobotAndWantedPose) 0 0"
		commandVector.push_back(PathCommand(0, -distanceYBetweenRobotAndWantedPose, 0));//"move 0 absolute(distanceYBetweenRobotAndWantedPose) 0"
	}

	return commandVector;
}

} //d3t12