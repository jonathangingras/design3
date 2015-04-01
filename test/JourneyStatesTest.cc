#include <testEssentials.h>
#include <ai/ai.h>
#include <vision/vision.h>

#include "mocks/ImageAngleAdjusterMock.h"

using namespace d3t12;
using ::testing::Return;
using ::testing::ElementsAre;

struct PoseGetterMock : public PoseGetter {
	MOCK_METHOD0(getPose, RobotPose(void));
};
#define CAST_POSEGETTER(x) *((PoseGetterMock*) x .get())

struct PoseCommanderMock : public PoseCommander {
	MOCK_METHOD1(commandPose, void(RobotPose));
};
#define CAST_POSECOMMANDER(x) *((PoseCommanderMock*) x .get())

struct QuestionGetterMock : public QuestionGetter {
	MOCK_METHOD0(getQuestion, std::string(void));
};
#define CAST_QUESTIONGETTER(x) *((QuestionGetterMock*) x .get())

struct QuestionAskerMock : public QuestionAsker {
	MOCK_METHOD1(ask, std::string(std::string));
};
#define CAST_QUESTIONASKER(x) *((QuestionAskerMock*) x .get())

struct ConfirmationGetterMock : public ConfirmationGetter {
	MOCK_METHOD0(ok, bool(void));
};
#define CAST_CONFIRMATIONGETTER(x) *((ConfirmationGetterMock*) x .get())

struct PathInformerMock : public PathInformer {
	MOCK_METHOD1(informPath, void(const std::vector<PathCommand>&));
};
#define CAST_PATHINFORMER(x) *((PathInformerMock*) x .get())

struct CubeCenterTargeterMock : public CubeCenterTargeter {
	MOCK_METHOD0(targetCenter, void(void));

	inline CubeCenterTargeterMock(): CubeCenterTargeter(ImageCapturer::Ptr(), CubeDetector::Ptr(), ImageAngleAdjuster::Ptr()) {}
};
#define CAST_TARGETER(x) *((CubeCenterTargeterMock*) x .get())

struct CubePositionFinderMock : public CubePositionFinder {
	MOCK_METHOD0(findCubePosition, CubeRelativePosition(void));

	inline CubePositionFinderMock(): CubePositionFinder(ImageAngleGetter::Ptr(), 0, 0, 0) {}
};
#define CAST_FINDER(x) *((CubePositionFinderMock*) x .get())

struct PathPlannerMock : public PathPlanner {
	//std::vector<PathCommand> planPath(RobotPose currentPose, RobotPose wantedPose);
	MOCK_METHOD2(planPath, std::vector<PathCommand>(RobotPose, RobotPose));
};
#define CAST_PATHPLANNER(x) *((PathPlannerMock*) x .get())

struct CubeDetectorMock : public CubeDetector {
	MOCK_METHOD0(detectCube, cv::Rect(void));
};

struct CubeDetectorFactoryMock : public CubeDetectorFactory {
	MOCK_METHOD2(createCubeDetector, CubeDetector::Ptr(std::string, cvMatPtr));

	inline CubeDetectorFactoryMock(): CubeDetectorFactory(ColorPalette::Ptr(new ColorPalette)) {
		palette->storeColor("somecolor", Color());
	}
};
#define CAST_DETECTORFACTORY(x) *((CubeDetectorFactoryMock*) x .get())

struct PrehensorMock : public Prehensor {
	MOCK_METHOD0(open, void(void));
	MOCK_METHOD0(close, void(void));
	MOCK_METHOD0(rise, void(void));
	MOCK_METHOD0(lower, void(void));
};
#define CAST_PREHENSOR(x) *((PrehensorMock*) x .get())

struct LEDMatrixControllerMock : public LEDMatrixController {
	MOCK_METHOD1(addNew, void(const std::string&));
	MOCK_METHOD0(addBlank, void(void));
	MOCK_METHOD0(removeCurrent, void(void));
	MOCK_METHOD0(turnAllOff, void(void));

	inline LEDMatrixControllerMock(MicroControllerCommandPort::Ptr _port): LEDMatrixController(_port) {}
};
#define CAST_LEDS(x) *((LEDMatrixControllerMock*) x .get())


#include <common/CountryToColorLister.h>

#define SETUP \
 \
PoseGetter::Ptr poseGetter(new PoseGetterMock); \
PoseCommander::Ptr poseCommander(new PoseCommanderMock); \
QuestionGetter::Ptr questionGetter(new QuestionGetterMock); \
QuestionAsker::Ptr questionAsker(new QuestionAskerMock); \
ConfirmationGetter::Ptr confirmationGetter(new ConfirmationGetterMock); \
PathInformer::Ptr pathInformer(new PathInformerMock); \
 \
std::vector<StringPtr> colors = CountryToColorLister(std::string(getenv("HOME")) + "/catkin_ws/src/design3/ros/d3_gui/flags.json").getColorList("Germany"); \
LEDColorList::Ptr colorList(new LEDColorList(LEDMatrixOrderList::Ptr(new LEDMatrixOrderList))); \
colorList->setColorList(colors); \
std::ostringstream* portStream = new std::ostringstream; \
LEDMatrixController::Ptr leds(new LEDMatrixControllerMock( MicroControllerCommandPort::Ptr(new MicroControllerCommandPort ( MicroControllerCommandPort::OStreamPtr(portStream) ) ) )  ); \
PathPlanner::Ptr pathPlanner(new PathPlannerMock); \
 \
CubeDetectorFactory::Ptr detectorFactory(new CubeDetectorFactoryMock); \
cvMatPtr image(new cv::Mat); \
CubeCenterTargeter::Ptr cameraTargeter(new CubeCenterTargeterMock);\
CubeCenterTargeter::Ptr motorTargeter(new CubeCenterTargeterMock);\
CubePositionFinder::Ptr finder(new CubePositionFinderMock);\
 \
ImageAngleAdjuster::Ptr cameraPoseAdjuster(new ImageAngleAdjusterMock); \
Prehensor::Ptr prehensor(new PrehensorMock); \
 \
JourneyBackPack::Ptr backpack(new JourneyBackPack); \
 \
JourneyStateFactory factory( \
	poseGetter, \
	poseCommander, \
	questionGetter, \
	questionAsker, \
	confirmationGetter, \
	pathInformer, \
	colorList, \
	leds, \
	pathPlanner, \
	detectorFactory, \
	image, \
	cameraTargeter, \
	motorTargeter, \
	finder, \
	cameraPoseAdjuster, \
	prehensor, \
	backpack \
); \
CubeDetector::Ptr cubeDetectorMock(new CubeDetectorMock);

TEST(LEDMatrixOrderList, outputsGoodColors) {
	SETUP

	for(int i = 0; i < 9; ++i) {
		std::cout << *colorList->next() << std::endl;
	}
}

MATCHER(AtlasPose, "is atlas pose") { return arg == ATLAS_ZONE_POSE; }

TEST(GoToAtlasState, goesToAtlasWhenNotThere) {
	SETUP

	std::vector<PathCommand> commands;
	PathCommand c1(1,0,0), c2(0,1,0), c3(0,0,1);
	commands.push_back(c1);
	commands.push_back(c2);
	commands.push_back(c3);

	JourneyState::Ptr state = factory.createState("GoToAtlas");
	EXPECT_CALL(CAST_POSEGETTER(poseGetter), getPose()).Times(1).WillOnce(Return(RobotPose(0.50,0.75,0)));
	
	EXPECT_CALL(CAST_PATHPLANNER(pathPlanner), planPath(RobotPose(0.50,0.75,0), ATLAS_ZONE_POSE)).Times(1).WillOnce(Return(commands));

	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(RobotPose(1,0,0)) ).Times(1);
	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(RobotPose(0,1,0)) ).Times(1);
	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(RobotPose(0,0,1)) ).Times(1);

	state->run();
}

TEST(GoToAtlasState, doesNotGoToAtlasWhenNotThere) {
	SETUP

	JourneyState::Ptr state = factory.createState("GoToAtlas");

	EXPECT_CALL(CAST_POSEGETTER(poseGetter), getPose()).Times(1).WillOnce(Return(ATLAS_ZONE_POSE));
	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(ATLAS_ZONE_POSE)).Times(0);

	state->run();
}

TEST(HandleQuestionState, asksQuestionOnceWhenGetConfirmation) {
	SETUP

	JourneyState::Ptr state = factory.createState("HandleQuestion");

	EXPECT_CALL(CAST_QUESTIONGETTER(questionGetter), getQuestion()).Times(1).WillOnce(Return("some question?"));
	EXPECT_CALL(CAST_QUESTIONASKER(questionAsker), ask("some question?")).Times(1);
	EXPECT_CALL(CAST_CONFIRMATIONGETTER(confirmationGetter), ok()).WillOnce(Return(true));

	state->run();
}

TEST(HandleQuestionState, asksQuestionTwiceWhenGetNegativeConfirmation) {
	SETUP

	JourneyState::Ptr state = factory.createState("HandleQuestion");

	EXPECT_CALL(CAST_QUESTIONGETTER(questionGetter), getQuestion()).Times(2).WillOnce(Return("some question?")).WillOnce(Return("another one?"));
	EXPECT_CALL(CAST_QUESTIONASKER(questionAsker), ask("some question?")).Times(1);
	EXPECT_CALL(CAST_QUESTIONASKER(questionAsker), ask("another one?")).Times(1);
	EXPECT_CALL(CAST_CONFIRMATIONGETTER(confirmationGetter), ok()).WillOnce(Return(false)).WillOnce(Return(true));

	state->run();
}

TEST(ShowFlagsOnLEDsState, stateRunsWhitoutException) {
	SETUP

	JourneyState::Ptr state = factory.createState("ShowFlagsOnLEDs");

	EXPECT_CALL(CAST_LEDS(leds), addBlank()).Times(6);
	EXPECT_CALL(CAST_LEDS(leds), addNew("yellow")).Times(1);
	EXPECT_CALL(CAST_LEDS(leds), addNew("red")).Times(1);
	EXPECT_CALL(CAST_LEDS(leds), addNew("black")).Times(1);
	EXPECT_CALL(CAST_LEDS(leds), turnAllOff()).Times(1);

	state->run();
}

TEST(GoToDetectionZoneState, stateRunsWhitoutException) {
	SETUP

	std::vector<PathCommand> commands;
	PathCommand c1(1,0,0), c2(0,1,0), c3(0,0,1);
	commands.push_back(c1);
	commands.push_back(c2);
	commands.push_back(c3);

	JourneyState::Ptr state = factory.createState("GoToDetectionZone");
	EXPECT_CALL(CAST_POSEGETTER(poseGetter), getPose()).Times(1).WillOnce(Return(RobotPose(0.50,0.75,0)));
	
	EXPECT_CALL(CAST_PATHPLANNER(pathPlanner), planPath(RobotPose(0.50,0.75,0), SEEKING_CUBE_ZONE_POSE)).Times(1).WillOnce(Return(commands));

	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(RobotPose(1,0,0)) ).Times(1);
	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(RobotPose(0,1,0)) ).Times(1);
	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(RobotPose(0,0,1)) ).Times(1);

	state->run();
}

TEST(AskCubeState, addsColorsInGoodOrder) {
	SETUP

	JourneyState::Ptr state = factory.createState("AskCube");

	EXPECT_CALL(CAST_LEDS(leds), addBlank()).Times(1);
	EXPECT_CALL(CAST_LEDS(leds), addNew("yellow")).Times(1);

	state->run();
}

TEST(FindCubeState, runsHowExpected) {
	SETUP

	JourneyState::Ptr state = factory.createState("FindCube");
	backpack->currentColor = "somecolor";
	CubeRelativePosition relativePosition(1.0,-0.5);

	EXPECT_CALL(CAST_DETECTORFACTORY(detectorFactory), createCubeDetector("somecolor", _)).Times(1).WillOnce(Return(cubeDetectorMock));
	EXPECT_CALL(CAST_TARGETER(cameraTargeter), targetCenter()).Times(1);
	EXPECT_CALL(CAST_FINDER(finder), findCubePosition()).Times(1).WillOnce(Return(relativePosition));

	state->run();

	EXPECT_EQ(relativePosition.x, backpack->cubeTarget.x);
	EXPECT_EQ(relativePosition.y, backpack->cubeTarget.y);
}

MATCHER(AnyPose, "is a pose") { return true; }

TEST(PlanPathToCubeZoneState, runsHowExpected) {
	SETUP

	JourneyState::Ptr state = factory.createState("PlanPathToCubeZone");
	backpack->cubeTarget = CubeRelativePosition(0.75, 0.4);
	std::vector<PathCommand> commands;
	PathCommand c1(0.75, 0.4, 0);
	commands.push_back(c1);

	EXPECT_CALL(CAST_POSEGETTER(poseGetter), getPose()).Times(1).WillOnce(Return(SEEKING_CUBE_ZONE_POSE));
	EXPECT_CALL(CAST_PATHPLANNER(pathPlanner), planPath(SEEKING_CUBE_ZONE_POSE, AnyPose())).Times(1).WillOnce(Return(commands));
	EXPECT_CALL(CAST_PATHINFORMER(pathInformer), informPath(ElementsAre(c1))).Times(1);

	state->run();
}

TEST(GoToCubeZoneState, runsHowExpected) {
	SETUP

	JourneyState::Ptr state = factory.createState("GoToCubeZone");
	std::vector<PathCommand> commands;
	PathCommand c1(0.75, 0.4, 0), c2(0.5, 0.5, 0);
	commands.push_back(c1);
	commands.push_back(c2);
	backpack->plannedCommands = commands;

	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(c1.toRobotPose())).Times(1);
	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(c2.toRobotPose())).Times(1);

	state->run();
}
