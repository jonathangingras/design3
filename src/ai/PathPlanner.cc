#include <ai/PathPlanner.h>

namespace d3t12 {

PathCommand PathPlanner::planPathAngle(RobotPose currentPose, RobotPose wantedPose) {
	PathCommand command(0,0,0);
	double distanceXBetweenRobotAndWantedPose = wantedPose.x - currentPose.x;
	double distanceYBetweenRobotAndWantedPose = wantedPose.y - currentPose.y;
	bool isRobotPoseNearLeftWall = false;
	bool isRobotPoseNearRightWall = false;
	// this is the secure buffer zone for the robot rotation command 
	if(currentPose.y + 0.35 >= 1.10) {
		isRobotPoseNearLeftWall = true;
	}
	else if(currentPose.y - 0.35 <= 0) {
		isRobotPoseNearRightWall = true;
	}
	
	//this section is for the command decision ordering

	if( distanceXBetweenRobotAndWantedPose < 0) {
		if(fabs(currentPose.yaw - M_PI) > 0.08) {

			if(isRobotPoseNearLeftWall) {
				command = PathCommand(0, 0, -M_PI - currentPose.yaw);
			} 
			else if (isRobotPoseNearRightWall) {
				command = PathCommand(0, 0, M_PI - currentPose.y);
			}
			else {
				command = PathCommand(0, 0, M_PI - currentPose.y);
			}
		}
		distanceYBetweenRobotAndWantedPose = -distanceYBetweenRobotAndWantedPose;
	}
		
	else if( distanceXBetweenRobotAndWantedPose > 0) {
		if( fabs(currentPose.yaw) > 0.08 )
		{
			if(isRobotPoseNearLeftWall) {
				command = PathCommand(0, 0, M_PI - currentPose.yaw);//"move 0 0 (180 - currentPose.angle)"
			}
			else if(isRobotPoseNearRightWall) {
				command = PathCommand(0, 0, currentPose.yaw - M_PI);//"move 0 0 (currentPose.angle - 180)"
			}
			else {
				command = PathCommand(0, 0, M_PI - currentPose.yaw);//"move 0 0 (180 - currentPose.angle)"
			}
		}
	}
	return command;
}
std::vector<PathCommand> PathPlanner::planPath(RobotPose currentPose, RobotPose wantedPose) {
	std::vector<PathCommand> poses;
	double distanceXBetweenRobotAndWantedPose = wantedPose.x - currentPose.x;
	double distanceYBetweenRobotAndWantedPose = wantedPose.y - currentPose.y;
	bool isWantedPoseNearLeftWall = false;
	bool isWantedPoseNearRightWall = false;
	bool isRobotPoseNearLeftWall = false;
	bool isRobotPoseNearRightWall = false;
	double destinationYaw = 0;
	// this is the secured buffer zone for the wantedPose approach
	if(wantedPose.y + 0.35 >= 1.10) {
		isWantedPoseNearLeftWall = true;
		destinationYaw = M_PI/2;
	}
	else if(wantedPose.y - 0.35 <= 0) {
		isWantedPoseNearRightWall = true;
		destinationYaw = -M_PI/2;
	}
	// this is the secure buffer zone for the robot rotation command 
	if(currentPose.y + 0.35 >= 1.10) {
		isRobotPoseNearLeftWall = true;
	}
	else if(currentPose.y - 0.35 <= 0) {
		isRobotPoseNearRightWall = true;
	}
	if ( distanceXBetweenRobotAndWantedPose < 0)
	{
		destinationYaw = M_PI;
	}
	
	if( isWantedPoseNearLeftWall == true)
	{
		if( currentPose.y - 0.55 > 0.01)
		{
			poses.push_back(PathCommand(currentPose.x, currentPose.y - 0.33, currentPose.yaw));
		}
	}
	if ( isWantedPoseNearRightWall == true)
	{	
		float newXPose = currentPose.x;
		float newYPose = currentPose.y;
		float newAnglePose = currentPose.yaw;
		if( currentPose.y - 0.55 > 0.01) {
			newYPose = currentPose.y - 0.33;
			poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		}
		if(distanceXBetweenRobotAndWantedPose > 0) {
			newAnglePose = 0;
			poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		}
		else {
			newAnglePose = M_PI;
			poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		}
		newXPose = wantedPose.x;
		poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		newAnglePose = M_PI/2;
		poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		newYPose = wantedPose.y;
		poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
	}
	else if ( isWantedPoseNearLeftWall == true) {	
		float newXPose = currentPose.x;
		float newYPose = currentPose.y;
		float newAnglePose = currentPose.yaw;
		if( currentPose.y - 0.55 < 0.01) {
			newYPose = currentPose.y + 0.33;
			poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		}
		if(distanceXBetweenRobotAndWantedPose > 0) {
			newAnglePose = 0;
			poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		}
		else {
			newAnglePose = M_PI;
			poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		}
		newXPose = wantedPose.x;
		poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		newAnglePose = -M_PI/2;
		poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		newYPose = wantedPose.y;
		poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
	}
	else
	{
		float newXPose = currentPose.x;
		float newYPose = currentPose.y;
		float newAnglePose = currentPose.yaw;
		if(distanceXBetweenRobotAndWantedPose > 0)
		{
			newAnglePose = 0;
			poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		}
		else
		{
			newAnglePose = M_PI;
			poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		}
		newXPose = wantedPose.x;
		poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
		newYPose = wantedPose.y;
		poses.push_back(PathCommand(newXPose, newYPose, newAnglePose));
	}

	return poses;
}

} //d3t12