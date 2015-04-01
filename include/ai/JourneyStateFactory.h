#ifndef _D3T12_JOURNEYSTATEFACTORY_H_
#define _D3T12_JOURNEYSTATEFACTORY_H_

#include <vision/vision.h>
#include "JourneyStates.h"

namespace d3t12 {

class JourneyStateFactory {
private:
	PoseGetter::Ptr poseGetter;
	PoseCommander::Ptr poseCommander;
	QuestionGetter::Ptr questionGetter;
	QuestionAsker::Ptr questionAsker;
	ConfirmationGetter::Ptr confirmationGetter;
	PathInformer::Ptr pathInformer;

	LEDColorList::Ptr colorList;
	LEDMatrixController::Ptr leds;

	PathPlanner::Ptr pathPlanner;

	CubeDetectorFactory::Ptr detectorFactory;
	cvMatPtr image;
	CubeCenterTargeter::Ptr cameraTargeter;
	CubeCenterTargeter::Ptr motorTargeter;
	CubePositionFinder::Ptr finder;
	
	ImageAngleAdjuster::Ptr cameraPoseAdjuster;
	Prehensor::Ptr prehensor;

	JourneyBackPack::Ptr backpack;

public:
	inline JourneyStateFactory(
		PoseGetter::Ptr _poseGetter,
		PoseCommander::Ptr _poseCommander,
		QuestionGetter::Ptr _questionGetter,
		QuestionAsker::Ptr _questionAsker,
		ConfirmationGetter::Ptr _confirmationGetter,
		PathInformer::Ptr _pathInformer,

		LEDColorList::Ptr _colorList,
		LEDMatrixController::Ptr _leds,

		PathPlanner::Ptr _pathPlanner,

		CubeDetectorFactory::Ptr _detectorFactory,
		cvMatPtr _image,
		CubeCenterTargeter::Ptr _cameraTargeter,
		CubeCenterTargeter::Ptr _motorTargeter,
		CubePositionFinder::Ptr _finder,
	
		ImageAngleAdjuster::Ptr _cameraPoseAdjuster,
		Prehensor::Ptr _prehensor,

		JourneyBackPack::Ptr _backpack
	): 
		poseGetter(_poseGetter),
		poseCommander(_poseCommander),
		questionGetter(_questionGetter),
		questionAsker(_questionAsker),
		confirmationGetter(_confirmationGetter),
		pathInformer(_pathInformer),

		colorList(_colorList),
		leds(_leds),

		detectorFactory(_detectorFactory),
		image(_image),
		cameraTargeter(_cameraTargeter),
		motorTargeter(_motorTargeter),
		finder(_finder),

		pathPlanner(_pathPlanner),

		cameraPoseAdjuster(_cameraPoseAdjuster),
		prehensor(_prehensor),

		backpack(_backpack)
	{}
	
	JourneyState::Ptr createState(std::string stateName);
};

} //d3t12

#endif