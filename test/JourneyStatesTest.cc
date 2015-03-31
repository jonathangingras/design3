#include <testEssentials.h>
#include <ai/JourneyStateFactory.h>

#include "mocks/ImageAngleAdjusterMock.h"

using namespace d3t12;
using ::testing::Return;

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

struct PrehensorMock : public Prehensor {
	MOCK_METHOD0(open, void(void));
	MOCK_METHOD0(close, void(void));
	MOCK_METHOD0(rise, void(void));
	MOCK_METHOD0(lower, void(void));
};
#define CAST_PREHENSOR(x) *((PrehensorMock*) x .get())

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
LEDMatrixController::Ptr leds(new LEDMatrixController (MicroControllerCommandPort::Ptr(new MicroControllerCommandPort ( MicroControllerCommandPort::OStreamPtr(portStream) ) ) )  ); \
PathPlanner::Ptr pathPlanner(new PathPlanner); \
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
	cameraPoseAdjuster, \
	prehensor, \
	backpack \
); \

MATCHER(AtlasPose, "is atlas pose") { return arg == ATLAS_ZONE_POSE; }

TEST(GoToAtlasState, goesToAtlasWhenNotThere) {
	SETUP

	JourneyState::Ptr state = factory.createState("GoToAtlas");

	EXPECT_CALL(CAST_POSEGETTER(poseGetter), getPose()).Times(1).WillOnce(Return(RobotPose(0.15,0.63,-M_PI/2)));
	EXPECT_CALL(CAST_POSECOMMANDER(poseCommander), commandPose(ATLAS_ZONE_POSE)).Times(1);

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

	state->run();
}

TEST(GoToDetectionZoneState, stateRunsWhitoutException) {
	SETUP

	JourneyState::Ptr state = factory.createState("GoToDetectionZone");
	EXPECT_CALL(CAST_POSEGETTER(poseGetter), getPose()).Times(1).WillOnce(Return(RobotPose(0.50,0.75,0)));

	state->run();
}