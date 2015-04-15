#ifndef _D3T12_JOURNEYBACKPACK_H_
#define _D3T12_JOURNEYBACKPACK_H_

#include <common/commonEssentials.h>
#include <vector>
#include <common/LEDMatrixOrderList.h>
#include "RobotPose.h"
#include "PathPlanner.h"
#include "CubeRelativePosition.h"

#define ATLAS_ZONE_POSE RobotPose(0.22,0.12,0)
#define SEEKING_CUBE_ZONE_POSE RobotPose(0.88,0.55,0)
#define RETURN_SEEKING_CUBE_ZONE_POSE RobotPose(0.98,0.55,M_PI)

namespace d3t12 {

struct JourneyBackPack {
	typedef boost::shared_ptr<JourneyBackPack> Ptr;

	std::vector<PathCommand> plannedCommands;

	std::vector<RobotPose> cubeDroppedPoses;
	
	CubeRelativePosition cubeTarget;
	RobotPose poseTarget;
	std::string currentColor;

	RobotPose detectionZonePose;
	RobotPose atlasZonePose;

	int cubeCurrentIndex;

	inline JourneyBackPack(RobotPose _detectionZonePose, RobotPose _atlasZonePose):
		detectionZonePose(_detectionZonePose), atlasZonePose(_atlasZonePose), cubeTarget(0,0), poseTarget(0,0,0), cubeCurrentIndex(0) {}
	inline JourneyBackPack():
		detectionZonePose(SEEKING_CUBE_ZONE_POSE), atlasZonePose(ATLAS_ZONE_POSE), cubeTarget(0,0), poseTarget(0,0,0), cubeCurrentIndex(0) {}
};

}

#endif