#include <ai/JourneyStates.h>

namespace d3t12 {

#define HEY std::cout << "hey" << std::endl;

void GoToAtlasState::run() {
	RobotPose pose = poseGetter->getPose();
	if(pose != backpack->atlasZonePose) {
		std::vector<PathCommand> commands = pathPlanner->planPath(pose, backpack->atlasZonePose);
		for(int i = 0; i < commands.size(); ++i) {
			std::cout << commands[i].x << ',' << commands[i].y << ',' << commands[i].yaw << std::endl;
			poseCommander->commandPose(commands[i].toRobotPose());
		}
	}
}

void HandleQuestionState::run() {
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
		StringPtr colorStr = colorList->next();
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
		for(int i = 0; i < commands.size(); ++i) {
			poseCommander->commandPose(commands[i].toRobotPose());
		}
	}
}

void AskCubeState::run() {
	for(int i = 0; i < 9; ++i) {
		backpack->currentColor = *colorList->next();

		if(!backpack->currentColor.empty()) {
			break;
		} else {
			leds->addBlank();
		}
	}
	leds->addNew(backpack->currentColor);

	d3t12::sleepSecondsNanoSeconds(5,0);
}

void FindCubeState::run() {
	CubeDetector::Ptr detector = detectorFactory->createCubeDetector(backpack->currentColor, image);
	cameraTargeter->setDetector(detector);
	
	for(int i = 0; i < 5; ++i) {
		cameraTargeter->targetCenter();
	}

	backpack->cubeTarget = finder->findCubePosition();
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
		currentPose.x + backpack->cubeTarget.x, 
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
	//motorTargeter->targetCenter();
	prehensor->open();
	poseCommander->commandDirectly(RobotPose(0.05,0,0));
	prehensor->close();
	prehensor->open();
	poseCommander->commandDirectly(RobotPose(-0.025,0,0));
	poseCommander->commandDirectly(RobotPose(0.03,0,0));
	prehensor->close();
	cameraTargeter->targetCenter();
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
	//TODO add code for dropping at good place

	prehensor->lower();
	prehensor->open();
	prehensor->rise();

	poseCommander->commandDirectly(RobotPose(-0.30,0,0));

	prehensor->close();
	prehensor->lower();

	poseCommander->commandDirectly(RobotPose(-0.20,0,0));
}

} //d3t12