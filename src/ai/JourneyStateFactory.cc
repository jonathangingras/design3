#include <ai/JourneyStateFactory.h>

namespace d3t12 {

JourneyState::Ptr JourneyStateFactory::createState(std::string stateName) {
	JourneyState::Ptr statePtr;
	backpack->atlasZonePose = ATLAS_ZONE_POSE;
	backpack->detectionZonePose = SEEKING_CUBE_ZONE_POSE;

	if(stateName == "GoToAtlas") {
		GoToAtlasState* state = new GoToAtlasState;
		state->poseGetter = poseGetter;
		state->poseCommander = poseCommander;
		statePtr = JourneyState::Ptr(state);
	} else if(stateName == "HandleQuestion") {
		HandleQuestionState* state = new HandleQuestionState;
		state->questionGetter = questionGetter;
		state->questionAsker = questionAsker;
		state->confirmationGetter = confirmationGetter;
		statePtr = JourneyState::Ptr(state);
	} else if(stateName == "ShowFlagsOnLEDs") {
		ShowFlagsOnLEDsState* state = new ShowFlagsOnLEDsState;
		state->colorList = colorList;
		state->leds = leds;
		statePtr = JourneyState::Ptr(state);
	} else if(stateName == "GoToDetectionZone") {
		GoToDetectionZoneState* state = new GoToDetectionZoneState;
		state->poseGetter = poseGetter;
		state->poseCommander = poseCommander;
		state->pathPlanner = pathPlanner;		
		statePtr = JourneyState::Ptr(state);
	}

	statePtr->backpack = backpack;
	return statePtr;
}

} //d3t12