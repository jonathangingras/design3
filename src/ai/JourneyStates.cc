#include <ai/JourneyStates.h>

namespace d3t12 {

void GoToAtlasState::run() {
	RobotPose pose = poseGetter->getPose();
	if(pose != backpack->atlasZonePose) {
		std::vector<PathCommand> commands = pathPlanner->planPath(pose, backpack->atlasZonePose);
		
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

	std::string questionStr = questionGetter->getQuestion();
	std::string answer = questionAsker->ask(questionStr);
	if(!confirmationGetter->ok()) {
		throw BadAnswerException("bad country!");
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
	for(int i = 0; i < 9; ++i) {
		backpack->cubeCurrentIndex++;

		backpack->currentColor = *colorList->current();

		if(!backpack->currentColor.empty()) {
			break;
		} else {
			leds->addBlank();
		}
	}

	if(backpack->cubeCurrentIndex > 9) {
		backpack->cubeCurrentIndex = 0;
		leds->turnMasterOn();
		d3t12::sleepSecondsNanoSeconds(5,0);
		leds->reset();

		throw FlagCompletedException("Flag done!");
	}

	leds->addNew(backpack->currentColor);
	std::cout << "asking color: " << backpack->currentColor << std::endl;

	d3t12::sleepSecondsNanoSeconds(5,0);
}

void FindCubeState::run() {
	CubeDetector::Ptr detector = detectorFactory->createCubeDetector(backpack->currentColor, image);
	cameraTargeter->setDetector(detector);
	cameraTargeter->resetAngle();
	
	for(int i = 0; i < 10; ++i) {
		int error = 1;
		while(error) {
			if(error >= 100) {
				cameraTargeter->changeAngle();
				error = 1;
			}

			try {
				cameraTargeter->targetCenter();
			} catch(NoCubeFoundException& err) {
				error += 1;
				continue;
			}
			error = 0;
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
	RobotPose targetPose = RobotPose(target.x - 0.36, target.y - 0.02, 0);
	
	
	backpack->plannedCommands.clear();
	backpack->plannedCommands.push_back(backpack->poseTarget);
	backpack->plannedCommands.push_back(RobotPose(targetPose.x + backpack->poseTarget.x, targetPose.y + backpack->poseTarget.y, 0));
	pathInformer->informPath(backpack->plannedCommands);


	poseCommander->commandDirectly(targetPose);

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
	
	prehensor->rise();
}

void PlanReturnToDetectionZoneState::run() {
	RobotPose currentPose = poseGetter->getPose();
	backpack->plannedCommands = pathPlanner->planPath(currentPose, RETURN_SEEKING_CUBE_ZONE_POSE);

	RobotPose dropPose = dropList->previous(), frontDropPose = RETURN_SEEKING_CUBE_ZONE_POSE;
	backpack->plannedCommands.push_back(RobotPose(frontDropPose.x, dropPose.y, dropPose.yaw));
	backpack->plannedCommands.push_back(RobotPose(dropPose.x, dropPose.y, dropPose.yaw));

	pathInformer->informPath(backpack->plannedCommands);
}

void ReturnToDetectionZoneState::run() {
	for(int i = 0; i < backpack->plannedCommands.size() - 2; ++i) {
		poseCommander->commandPose(backpack->plannedCommands[i].toRobotPose());
	}
}

void DropCubeState::run() {
	RobotPose dropPose = dropList->previous();
	int cubeNo = dropList->getOrderList()->previous();

	if(cubeNo != 1 && cubeNo != 4 && cubeNo != 7) { dropPose.y -= 0.03; }
	std::cout << "drop pose #" << cubeNo << ": " << dropPose.x << ", " << dropPose.y << ", " << dropPose.yaw << std::endl;

	poseCommander->commandPose(RETURN_SEEKING_CUBE_ZONE_POSE);
	poseCommander->commandY(dropPose);
	poseCommander->commandY(dropPose);
	poseCommander->commandY(dropPose);
	poseCommander->commandY(dropPose);
	poseCommander->commandY(dropPose);

	poseCommander->commandX(dropPose);

	if(cubeNo == 2 || cubeNo == 5 || cubeNo == 8) { dropPose.y += 0.05; }
	if(cubeNo == 3 || cubeNo == 6 || cubeNo == 9) { dropPose.y += 0.07; }

	poseCommander->commandY(dropPose);

	prehensor->lower();
	prehensor->open();

	poseCommander->commandDirectly(RobotPose(-0.30,0,0));

	prehensor->close();

	poseCommander->commandDirectly(RobotPose(-0.20,0,0));
	poseCommander->commandDirectly(RobotPose(0,0,M_PI));
}

} //d3t12