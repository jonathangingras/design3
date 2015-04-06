#ifndef _D3T12_JOURNEYSTATES_H_
#define _D3T12_JOURNEYSTATES_H_

#include <driver/driver.h>
#include <vision/vision.h>
#include "CubePositionFinder.h"
#include "JourneyState.h"
#include "Interfaces.h"
#include "PathPlanner.h"

namespace d3t12 {

class GoToAtlasState : public JourneyState {
friend class JourneyStateFactory;

	PoseGetter::Ptr poseGetter;
	PoseCommander::Ptr poseCommander;
	PathPlanner::Ptr pathPlanner;

public:
	void run();
};

class HandleQuestionState : public JourneyState {
friend class JourneyStateFactory;

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

public:
	void run();
};

} //d3t12

#endif