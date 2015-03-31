#ifndef _D3T12_AI_ROBOTPOSE_H_
#define _D3T12_AI_ROBOTPOSE_H_

namespace d3t12 {

struct RobotPose {
	double x, y, yaw;

	inline RobotPose(double _x, double _y, double _yaw):
		x(_x), y(_y), yaw(_yaw) {}

	inline bool operator == (const RobotPose& pose2) {
		return fabs(x - pose2.x) <= 0.01 &&
			fabs(y - pose2.y) <= 0.01 &&
			fabs(yaw - pose2.yaw) <= 0.01;
	}

	inline bool operator != (const RobotPose& pose2) {
		return !(*this == pose2);
	}

};

}

#endif