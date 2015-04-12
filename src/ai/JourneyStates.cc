#include <ai/JourneyStates.h>

namespace d3t12 {

#define HEY std::cout << "hey" << std::endl;

void GoToAtlasState::run() {
	RobotPose pose = poseGetter->getPose();
	HEY
	if(pose != backpack->atlasZonePose) {
		std::vector<PathCommand> commands = pathPlanner->planPath(pose, backpack->atlasZonePose);
		pathInformer->informPath(commands);
		pathInformer->informPath(commands);
		pathInformer->informPath(commands);
		pathInformer->informPath(commands);
		pathInformer->informPath(commands);
		for(int i = 0; i < commands.size(); ++i) {
			std::cout << commands[i].x << ',' << commands[i].y << ',' << commands[i].yaw << std::endl;
			poseCommander->commandPose(commands[i].toRobotPose());
		}
	}
}

void HandleQuestionState::run() {
	leds->turnMasterOn();

	d3t12::sleepSecondsNanoSeconds(5,0);

	for(int i = 0; i < 2; ++i) {
		std::string questionStr = questionGetter->getQuestion();
		std::string answer = questionAsker->ask(questionStr);
		if(confirmationGetter->ok()) {
			break;
		}
	}
}

void ShowFlagsOnLEDsState::run() {
	for(int i = 0; i < 9; ++i) {
		StringPtr colorStr = colorList->current();
		if(colorStr->empty()) { leds->addBlank(); }
		else{leds->addNew(*colorStr); }
	}
	
	d3t12::sleepSecondsNanoSeconds(7,0);

	leds->turnAllOff();
}

void GoToDetectionZoneState::run() {
	RobotPose pose = poseGetter->getPose();
	if(pose != backpack->detectionZonePose) {
		std::vector<PathCommand> commands = pathPlanner->planPath(pose, backpack->detectionZonePose);
		pathInformer->informPath(commands);
		for(int i = 0; i < commands.size(); ++i) {
			poseCommander->commandPose(commands[i].toRobotPose());
		}
	}
}

void AskCubeState::run() {
	/*if(leds->matrixFilled()) {
		leds->turnMasterOn();
		d3t12::sleepSecondsNanoSeconds(5,0);
		leds->reset();

		throw FlagCompletedException("Flag done!");
	}*/

	for(int i = 0; i < 9; ++i) {
		backpack->currentColor = *colorList->current();

		if(!backpack->currentColor.empty()) {
			break;
		} else {
			leds->addBlank();
		}
	}
	leds->addNew(backpack->currentColor);
	std::cout << "asking color: " << backpack->currentColor << std::endl;

	d3t12::sleepSecondsNanoSeconds(5,0);
}

void FindCubeState::run() {
	CubeDetector::Ptr detector = detectorFactory->createCubeDetector(backpack->currentColor, image);
	cameraTargeter->setDetector(detector);
	cameraTargeter->resetAngle();
	
	for(int i = 0; i < 100; ++i) {
		bool error = true;
		while(error) {
			try {
				cameraTargeter->targetCenter();
			} catch(NoCubeFoundException& err) {
				error = true;
				continue;
			}
			error = false;
		}
	}

	backpack->cubeTarget = finder->findCubePosition();
	std::cout << "found cube position: " << backpack->cubeTarget << std::endl;
}

void PlanPathToCubeZoneState::run() {
	//TODO add logic to be able to grab cube when its right to table border
	// calculate plan poseTarget;
	RobotPose currentPose = poseGetter->getPose();
	/*double wantedYaw;
	if(backpack->cubeTarget.y <= 0.25) { wantedYaw = -M_PI; }
	else if(backpack->cubeTarget.y >= 0.75) { wantedYaw = M_PI; }
	else { wantedYaw = 0; }*/
	
	backpack->poseTarget = RobotPose( 
		currentPose.x + backpack->cubeTarget.x - 0.36, 
		currentPose.y + backpack->cubeTarget.y, 
		0 //wantedYaw
	);
	
	backpack->plannedCommands = pathPlanner->planPath(currentPose, backpack->poseTarget);
	pathInformer->informPath(backpack->plannedCommands);
}

void GoToCubeZoneState::run() {
	for(int i = 0; i < backpack->plannedCommands.size(); ++i) {
		poseCommander->commandPose(backpack->plannedCommands[i].toRobotPose());
	}
}

void GrabCubeState::run() {
	//TODO implement a motor targeter
	CubeDetector::Ptr detector = detectorFactory->createCubeDetector(backpack->currentColor, image);
	motorTargeter->setDetector(detector);
	motorTargeter->resetAngle();
	
	bool error = true;
	while(error) {
		try {
			motorTargeter->targetCenter();
		} catch(NoCubeFoundException& err) {
			error = true;
			continue;
		}
		error = false;
	}

	CubeRelativePosition target = finder->findCubePosition();
	poseCommander->commandDirectly(RobotPose(target.x - 0.36, target.y - 0.02, 0));

	prehensor->open();
	poseCommander->commandDirectly(RobotPose(0.20,0,0));
	d3t12::sleepSecondsNanoSeconds(2,0);
	prehensor->close();
	d3t12::sleepSecondsNanoSeconds(2,0);
	prehensor->open();
	poseCommander->commandDirectly(RobotPose(-0.025,0,0));
	d3t12::sleepSecondsNanoSeconds(1,0);
	poseCommander->commandDirectly(RobotPose(0.08,0,0));
	d3t12::sleepSecondsNanoSeconds(1,0);
	prehensor->close();
	//cameraTargeter->targetCenter();
	prehensor->rise();
}

void PlanReturnToDetectionZoneState::run() {
	RobotPose currentPose = poseGetter->getPose();
	backpack->plannedCommands = pathPlanner->planPath(currentPose, RETURN_SEEKING_CUBE_ZONE_POSE);
	pathInformer->informPath(backpack->plannedCommands);
}

void ReturnToDetectionZoneState::run() {
	for(int i = 0; i < backpack->plannedCommands.size(); ++i) {
		poseCommander->commandPose(backpack->plannedCommands[i].toRobotPose());
	}
}

void DropCubeState::run() {
	RobotPose dropPose = dropList->previous();
	std::cout << "drop pose: " << dropPose.x << ", " << dropPose.y << ", " << dropPose.yaw << std::endl;

	poseCommander->commandPose(RETURN_SEEKING_CUBE_ZONE_POSE);
	poseCommander->commandY(dropPose);
	poseCommander->commandX(dropPose);
	poseCommander->commandPose(dropPose);

	prehensor->lower();
	prehensor->open();
	prehensor->rise();

	poseCommander->commandDirectly(RobotPose(-0.30,0,0));

	prehensor->close();
	prehensor->lower();

	poseCommander->commandDirectly(RobotPose(-0.20,0,0));
	poseCommander->commandDirectly(RobotPose(0,0,M_PI));
}

} //d3t12