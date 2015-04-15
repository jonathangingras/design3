#ifndef _D3T12_JOURNEYSTATES_H_
#define _D3T12_JOURNEYSTATES_H_

#include <driver/driver.h>
#include <vision/vision.h>
#include "CubePositionFinder.h"
#include "JourneyState.h"
#include "Interfaces.h"
#include "PathPlanner.h"
#include "FlagCompletedException.h"
#include "BadAnswerException.h"

namespace d3t12 {

typedef CubeList<RobotPose> CubeDropPoseList;

class GoToAtlasState : public JourneyState {
friend class JourneyStateFactory;

	PoseGetter::Ptr poseGetter;
	PoseCommander::Ptr poseCommander;
	PathPlanner::Ptr pathPlanner;
	PathInformer::Ptr pathInformer;

public:
	void run();
};

class HandleQuestionState : public JourneyState {
friend class JourneyStateFactory;

	LEDMatrixController::Ptr leds;
	QuestionGetter::Ptr questionGetter;
	QuestionAsker::Ptr questionAsker;
	ConfirmationGetter::Ptr confirmationGetter;

public:
	void run();
};

class ShowFlagsOnLEDsState : public JourneyState {
friend class JourneyStateFactory;

	LEDColorList::Ptr colorList;
	LEDMatrixController::Ptr leds;

public:
	void run();
};

class GoToDetectionZoneState : public JourneyState {
friend class JourneyStateFactory;

	PoseGetter::Ptr poseGetter;
	PoseCommander::Ptr poseCommander;
	PathPlanner::Ptr pathPlanner;
	PathInformer::Ptr pathInformer;

public:
	void run();
};

class AskCubeState : public JourneyState {
friend class JourneyStateFactory;

	LEDColorList::Ptr colorList;
	LEDMatrixController::Ptr leds;

public:
	void run();
};

class FindCubeState : public JourneyState {
friend class JourneyStateFactory;

	CubeCenterTargeter::Ptr cameraTargeter;
	CubePositionFinder::Ptr finder;
	CubeDetectorFactory::Ptr detectorFactory;
	cvMatPtr image;

public:
	void run();
};

class PlanPathToCubeZoneState : public JourneyState {
friend class JourneyStateFactory;

	PathInformer::Ptr pathInformer;
	PoseGetter::Ptr poseGetter;
	PathPlanner::Ptr pathPlanner;

public:
	void run();
};

class GoToCubeZoneState : public JourneyState {
friend class JourneyStateFactory;

	PoseCommander::Ptr poseCommander;

public:
	void run();
};

class GrabCubeState : public JourneyState {
friend class JourneyStateFactory;

	PathInformer::Ptr pathInformer;
	CubePositionFinder::Ptr finder;
	Prehensor::Ptr prehensor;
	CubeDetectorFactory::Ptr detectorFactory;
	cvMatPtr image;
	CubeCenterTargeter::Ptr cameraTargeter;
	CubeCenterTargeter::Ptr motorTargeter;
	PoseGetter::Ptr poseGetter;
	PoseCommander::Ptr poseCommander;

public:
	void run();
};

class PlanReturnToDetectionZoneState : public JourneyState {
friend class JourneyStateFactory;
	
	CubeDropPoseList::Ptr dropList;
	PathInformer::Ptr pathInformer;
	PoseGetter::Ptr poseGetter;
	PathPlanner::Ptr pathPlanner;

public:
	void run();
};

class ReturnToDetectionZoneState : public JourneyState {
friend class JourneyStateFactory;

	PoseCommander::Ptr poseCommander;

public:
	void run();
};

class DropCubeState : public JourneyState {
friend class JourneyStateFactory;

	Prehensor::Ptr prehensor;
	PoseGetter::Ptr poseGetter;
	PoseCommander::Ptr poseCommander;
	CubeDropPoseList::Ptr dropList;

public:
	void run();
};

} //d3t12

#endif