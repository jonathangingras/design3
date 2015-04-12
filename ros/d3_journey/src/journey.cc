#include <ros/ros.h>
#include <std_msgs/String.h>

#include <common/common.h>
#include <driver/driver.h>
#include <rest/rest.h>
#include <vision/vision.h>
#include <ai/ai.h>

#include <geometry_msgs/Point.h>
#include <tf/transform_listener.h>

#include <d3_table_transform/robotPose.h>
#include <d3_table_transform/robotPoseArray.h>

namespace d3t12 {
	namespace tf = d3_table_transform;
}

struct PoseReceiver : public d3t12::PoseGetter {
	d3t12::RobotPose robotPose;
	boost::mutex mutex, fmutex;
	bool firstReceived;

	inline PoseReceiver(): robotPose(0,0,0), firstReceived(false) {
		fmutex.lock();
	}

	void callback(const d3t12::tf::robotPose::ConstPtr& inputPose) {
		if(!firstReceived) {
			firstReceived = true;
			fmutex.unlock();
		}

		mutex.lock();
		robotPose = d3t12::RobotPose(inputPose->x, inputPose->y, inputPose->yaw);
		mutex.unlock();
	}

	d3t12::RobotPose getPose() {
		if(!firstReceived) {
			fmutex.lock();
		}

		mutex.lock();
		d3t12::RobotPose pose = robotPose;
		mutex.unlock();
		ROS_ERROR_STREAM(pose.x << "," << pose.y << "," << pose.yaw);
		return pose;
	}
};

struct ConcretePoseCommander : public d3t12::PoseCommander {
	d3t12::MicroControllerCommandPort::Ptr commandPort;
	d3t12::MotorController motors;
	tf::TransformListener listener;

	inline ConcretePoseCommander(d3t12::MicroControllerCommandPort::Ptr _commandPort): 
		commandPort(_commandPort), motors(_commandPort), listener(ros::Duration(10)) {
		*commandPort << "clcmode p";
	}

	inline bool check(const std::string& str) {
		if(str.length() < 12) return false;
		
		std::string::const_reverse_iterator it = str.rbegin();
		std::string rstr;
		for(int i = 0; it != str.rbegin() + 12; ++it, ++i) {
			if(i < 2) continue;
			rstr += *it;
		}
		
		return rstr == "1\r\ngalfteg";//"getflag\n1\n>";
	}

	void getFlag() {
		d3t12::NonBlockIfStream inPort("/dev/ttySTM32");
		std::string inStr;
		/*do {
			*commandPort << "getflag";
			d3t12::sleepSecondsNanoSeconds(0, 10000000);
			inPort >> inStr;
		} while(inStr.empty() || *(inStr.end() - 3) != '1');*/
		for(int i = 0; i < 3; ++i) {
			do {
				*commandPort << "getflag";
				d3t12::sleepSecondsNanoSeconds(0, 10000000);
				inPort >> inStr;
			} while(!check(inStr));
		}
	}

	void commandDirectly(d3t12::RobotPose pose) {
		ROS_ERROR_STREAM("command: " << pose.x << ',' << pose.y << ',' << pose.yaw);

		*commandPort << "clcmode p";

		if( fabs(pose.yaw) >= 0.01 ) {
			motors.rotate( pose.yaw );
			getFlag();
		}
		if( fabs(pose.x) >= 0.01 || fabs(pose.y) >= 0.01 ) {
			motors.moveTo( (fabs(pose.x) >= 0.01 ? pose.x : 0), (fabs(pose.y) >= 0.01 ? pose.y : 0) );
			getFlag();
		}
	}

	void updateTf(const d3t12::RobotPose& pose, geometry_msgs::PoseStamped& currentRobotPoseOnTable, geometry_msgs::PoseStamped& wantedRobotPoseOnRobot, double& diffYaw) {
		geometry_msgs::PoseStamped currentRobotPoseOnRobot;
		currentRobotPoseOnRobot.header.frame_id = "robot_center";
		currentRobotPoseOnRobot.header.stamp = ros::Time();
		currentRobotPoseOnRobot.pose.position.x = 0;
		currentRobotPoseOnRobot.pose.position.y = 0;
		currentRobotPoseOnRobot.pose.position.z = 0;
		currentRobotPoseOnRobot.pose.orientation = tf::createQuaternionMsgFromYaw(0);

		//geometry_msgs::PoseStamped currentRobotPoseOnTable;

		geometry_msgs::PoseStamped wantedRobotPoseOnTable;
		wantedRobotPoseOnTable.header.frame_id = "d3_table_origin";
		wantedRobotPoseOnTable.header.stamp = currentRobotPoseOnRobot.header.stamp;
		wantedRobotPoseOnTable.pose.position.x = pose.x;
		wantedRobotPoseOnTable.pose.position.y = pose.y;
		wantedRobotPoseOnTable.pose.position.z = 0;
		wantedRobotPoseOnTable.pose.orientation = tf::createQuaternionMsgFromYaw(pose.yaw);

		//geometry_msgs::PoseStamped wantedRobotPoseOnRobot;

		bool error = true;
		while(error) {
			try {
				listener.transformPose("d3_table_origin", currentRobotPoseOnRobot, currentRobotPoseOnTable);
				listener.transformPose("robot_center", wantedRobotPoseOnTable, wantedRobotPoseOnRobot);
			} catch(tf::TransformException& ex) {
				error = true;
				continue;
			}
			error = false;
		}

		diffYaw = tf::getYaw(currentRobotPoseOnTable.pose.orientation) - tf::getYaw(wantedRobotPoseOnTable.pose.orientation);
		if(2*M_PI - fabs(diffYaw) <= 0.1) diffYaw = 0;

		ROS_ERROR_STREAM("tf ouputed:" << wantedRobotPoseOnTable.pose.position.x << ' ' << wantedRobotPoseOnTable.pose.position.y << ' ' << tf::getYaw(wantedRobotPoseOnTable.pose.orientation));
	}

	void commandPose(d3t12::RobotPose pose) {
		geometry_msgs::PoseStamped currentRobotPoseOnTable;
		geometry_msgs::PoseStamped wantedRobotPoseOnRobot;

		double diffYaw;
		updateTf(pose, currentRobotPoseOnTable, wantedRobotPoseOnRobot, diffYaw);

		d3t12::RobotPose angleCommand(0.0, 0.0, diffYaw);

		commandDirectly(angleCommand);


		updateTf(pose, currentRobotPoseOnTable, wantedRobotPoseOnRobot, diffYaw);

		d3t12::RobotPose translationCommand(wantedRobotPoseOnRobot.pose.position.x, wantedRobotPoseOnRobot.pose.position.y, 0.0);

		commandDirectly(translationCommand);

		ROS_ERROR_STREAM("pathplanner ouputed:" << pose.x << ',' << pose.y << ',' << pose.yaw);
	}

	void commandX(d3t12::RobotPose pose) {
		geometry_msgs::PoseStamped currentRobotPoseOnTable;
		geometry_msgs::PoseStamped wantedRobotPoseOnRobot;

		double diffYaw;
		updateTf(pose, currentRobotPoseOnTable, wantedRobotPoseOnRobot, diffYaw);

		d3t12::RobotPose translationCommand(wantedRobotPoseOnRobot.pose.position.x, wantedRobotPoseOnRobot.pose.position.y, 0.0);

		commandDirectly(d3t12::RobotPose(translationCommand.x, 0, 0));
	}

	void commandY(d3t12::RobotPose pose) {
		geometry_msgs::PoseStamped currentRobotPoseOnTable;
		geometry_msgs::PoseStamped wantedRobotPoseOnRobot;

		double diffYaw;
		updateTf(pose, currentRobotPoseOnTable, wantedRobotPoseOnRobot, diffYaw);

		d3t12::RobotPose translationCommand(wantedRobotPoseOnRobot.pose.position.x, wantedRobotPoseOnRobot.pose.position.y, 0.0);

		commandDirectly(d3t12::RobotPose(0, translationCommand.y, 0));		
	}
};

struct ConcreteQuestionGetter : public d3t12::QuestionGetter { //must be moved to other node as a receiver of std_msgs::String message
	ros::Publisher& questionPublisher;

	inline ConcreteQuestionGetter(ros::Publisher& _questionPublisher):
		questionPublisher(_questionPublisher) {}

	std::string getQuestion() {
		d3t12::CURLGetter getter("https://192.168.0.2");
  		d3t12::AtlasJSONDecoder decoder;
  		std::string atlas_told = getter.performGET();
  		
  		std_msgs::String ansMsg;
  		ansMsg.data = decoder.questionStr(atlas_told);

  		questionPublisher.publish(ansMsg);
  		return ansMsg.data;
	}
};

struct ConcreteQuestionAsker : public d3t12::QuestionAsker {
	d3t12::LEDColorList::Ptr colorList;
	std::vector<d3t12::StringPtr> colors;
	ros::Publisher& answerPublisher;

	inline ConcreteQuestionAsker(d3t12::LEDColorList::Ptr _colorList, ros::Publisher& _answerPublisher):
		colorList(_colorList), answerPublisher(_answerPublisher) {}

	inline void removeEndLine(std::string& str) {
		std::string::iterator it = str.begin();
		std::string ret;
		for(; it != str.end(); ++it) {
			if(*it != '\n' && *it != '\r') {
				ret += *it;
			}
		}
		str = ret;
	}

	std::string ask(std::string question) {
		d3t12::Popener popener;
		std::string answer = popener.popen("python2.7.9 -m naturalLanguagePython '" + question + "'");

		std::string jsonFile = std::string(getenv("HOME")) + "/catkin_ws/src/design3/ros/d3_gui/flags.json";
		d3t12::CountryToColorLister listTranslater(jsonFile);
		
		removeEndLine(answer);

		ROS_ERROR_STREAM("COUNTRY ANSWER ------>>>> " << answer);

		colors = listTranslater.getColorList(answer);

		colorList->setList(colors);

		std_msgs::String ansMsg;
  		ansMsg.data = answer;
		answerPublisher.publish(ansMsg);

		return answer;
	}
};

struct ConcreteConfirmationGetter : public d3t12::ConfirmationGetter {
	bool ok() {
		//implement from topic received from gui button
		return true;
	}
};

struct ConcretePathInformer : public d3t12::PathInformer {
	ros::Publisher pathPublisher;

	inline ConcretePathInformer(ros::NodeHandle& node) {
		pathPublisher = node.advertise<d3t12::tf::robotPoseArray>("/d3_journey/robot_path", 1);
	}

	void informPath(const std::vector<d3t12::PathCommand>& path) {
		d3t12::tf::robotPoseArray poseArray;

		std::vector<d3t12::tf::robotPose> poses;
		for(std::vector<d3t12::PathCommand>::const_iterator it = path.begin(); it != path.end(); ++it) {
			d3t12::tf::robotPose pose;
			pose.x = it->x;
			pose.y = it->y;
			pose.yaw = it->yaw;
			poses.push_back(pose);
		}
		poseArray.poses = poses;

		ROS_ERROR_STREAM("publishing array");
		
		pathPublisher.publish(poseArray);
	}
};

struct ConcreteAngleAdjuster : public d3t12::ImageAngleAdjuster {
    d3t12::CameraPoseHandler::Ptr cameraPose;
    double initPitch;

    inline float rad2deg(double rad) {
        return (rad*180)/M_PI;
    }

    inline double deg2rad(float deg) {
        return (deg*M_PI)/180;
    }

    inline ConcreteAngleAdjuster(d3t12::CameraPoseHandler::Ptr _cameraPose, double _initPitch):
        cameraPose(_cameraPose), initPitch(_initPitch) {}

    void resetAngle() {
    	cameraPose->setPitch(initPitch);
    	cameraPose->setYaw(M_PI/2);
    }

    void adjustY(float degrees) {
        cameraPose->increasePitch(deg2rad(degrees));
    }

    void adjustX(float degrees) {
        cameraPose->increaseYaw(deg2rad(degrees));
    }
};

struct ConcreteMotorAdjuster : public d3t12::ImageAngleAdjuster {
    d3t12::CameraPoseHandler::Ptr cameraPose;
    d3t12::PoseCommander::Ptr poseCommander;

    inline ConcreteMotorAdjuster(d3t12::CameraPoseHandler::Ptr _cameraPose, d3t12::PoseCommander::Ptr _poseCommander):
        cameraPose(_cameraPose), poseCommander(_poseCommander) {}

    void resetAngle() {
    	cameraPose->setPitch(M_PI/4);
    	cameraPose->setYaw(M_PI/2);
    }

    void adjustY(float degrees) {
        poseCommander->commandDirectly(d3t12::RobotPose(0.01*degrees, 0.0, 0.0));
    }

    void adjustX(float degrees) {
        poseCommander->commandDirectly(d3t12::RobotPose(0.0, -0.01*degrees, 0.0));
    }
};

struct ConcreteAngleGetter : public d3t12::ImageAngleGetter {
    d3t12::CameraPoseHandler::Ptr cameraPose;

    inline ConcreteAngleGetter(d3t12::CameraPoseHandler::Ptr _cameraPose):
        cameraPose(_cameraPose) {}

    double getPitch() {
        return cameraPose->getPitch();
    }

    double getYaw() {
        return cameraPose->getYaw();
    }
};

struct ConcreteImageCapturer : public d3t12::ImageCapturer {
    d3t12::CameraCapturer* capturer;
    d3t12::cvMatPtr srcImage;

    inline ConcreteImageCapturer(int camId, d3t12::cvMatPtr _srcImage): 
        capturer(new d3t12::CameraCapturer(camId)), srcImage(_srcImage) {}
    
    ~ConcreteImageCapturer() {
        delete capturer;
    }

    void capture() {
        *capturer >> *srcImage;
    }
};

void runState(d3t12::JourneyStateFactory::Ptr stateFactory, const std::string& stateName) {
	d3t12::JourneyState::Ptr state = stateFactory->createState(stateName);
	state->run();
	std::cout << "done state: " << stateName << std::endl; 
}

void factoryThread(d3t12::JourneyStateFactory::Ptr stateFactory) {
	beginning: runState(stateFactory, "GoToAtlas");
	runState(stateFactory, "HandleQuestion");
	runState(stateFactory, "ShowFlagsOnLEDs");
	nextCube: runState(stateFactory, "GoToDetectionZone"); 
	
	try {
		runState(stateFactory, "AskCube");
	} catch(d3t12::FlagCompletedException& flagDoneError) {
		ROS_ERROR_STREAM(flagDoneError.what());
		goto beginning;
	}
	
	runState(stateFactory, "FindCube");
	runState(stateFactory, "PlanPathToCubeZone");
	runState(stateFactory, "GoToCubeZone");
	runState(stateFactory, "GrabCube");
	runState(stateFactory, "PlanReturnToDetectionZone");
	runState(stateFactory, "ReturnToDetectionZone");
	runState(stateFactory, "DropCube");
	goto nextCube;
}

int main(int argc, char** argv) {
	ros::init(argc, argv, "design3_robot_journey");
	ros::NodeHandle node;
	chdir(getenv("HOME"));

	d3t12::MicroControllerCommandPort::Ptr commandPort(
		new d3t12::MicroControllerCommandPort(
			d3t12::MicroControllerCommandPort::OStreamPtr(
				new std::ofstream("/dev/ttySTM32")
			)
		)
	);

	PoseReceiver* poseReceiver = new PoseReceiver;
	d3t12::PoseGetter::Ptr poseGetter(poseReceiver);
	ros::Subscriber robotPoseSubscriber = node.subscribe<d3t12::tf::robotPose>("robot_positioner/robot_pose", 1, &PoseReceiver::callback, poseReceiver);

	ros::Publisher questionPublisher = node.advertise<std_msgs::String>("/robot_journey/question", 1);
	ros::Publisher answerPublisher = node.advertise<std_msgs::String>("/robot_journey/answer", 1);


	d3t12::PoseCommander::Ptr poseCommander(new ConcretePoseCommander(commandPort));

	d3t12::LEDMatrixController::Ptr leds(new d3t12::LEDMatrixController(commandPort));
	leds->reset();
	d3t12::LEDColorList::Ptr colorList(new d3t12::LEDColorList(leds->getOrderList()));

	d3t12::CubeDropPoseList::Ptr dropList(new d3t12::CubeDropPoseList(leds->getOrderList()));
	std::vector<d3t12::RobotPose> dropListVector;
	dropListVector.push_back(d3t12::RobotPose(0.85, 0.67, M_PI));
	dropListVector.push_back(d3t12::RobotPose(0.85, 0.55, M_PI));
	dropListVector.push_back(d3t12::RobotPose(0.85, 0.43, M_PI));

	dropListVector.push_back(d3t12::RobotPose(0.75, 0.67, M_PI));
	dropListVector.push_back(d3t12::RobotPose(0.75, 0.55, M_PI));
	dropListVector.push_back(d3t12::RobotPose(0.75, 0.44, M_PI));

	dropListVector.push_back(d3t12::RobotPose(0.65, 0.67, M_PI));
	dropListVector.push_back(d3t12::RobotPose(0.65, 0.55, M_PI));
	dropListVector.push_back(d3t12::RobotPose(0.65, 0.43, M_PI));
	dropList->setList(dropListVector);

	d3t12::QuestionGetter::Ptr questionGetter(new ConcreteQuestionGetter(questionPublisher));
	d3t12::QuestionAsker::Ptr questionAsker(new ConcreteQuestionAsker(colorList, answerPublisher));
	d3t12::ConfirmationGetter::Ptr confirmationGetter(new ConcreteConfirmationGetter);
	d3t12::PathInformer::Ptr pathInformer(new ConcretePathInformer(node));

	d3t12::PathPlanner::Ptr pathPlanner(new d3t12::PathPlanner);

	d3t12::cvMatPtr image(new cv::Mat);
	d3t12::ImageCapturer::Ptr imageCapturer(new ConcreteImageCapturer(0, image));

	d3t12::ColorJSONLoader loader;
    loader.setFile(std::string(getenv("HOME")) + "/catkin_ws/src/design3/config/colors.json");
    loader.loadJSON();
    d3t12::ColorPalette::Ptr palette(new d3t12::ColorPalette);
    loader.fillPalette(*palette);

    d3t12::CubeDetectorFactory::Ptr detectorFactory(new d3t12::CubeDetectorFactory(palette));

	d3t12::CameraPoseHandler::Ptr cameraPose(new d3t12::CameraPoseHandler);
	d3t12::ImageAngleGetter::Ptr angleGetter(new ConcreteAngleGetter(cameraPose));

	d3t12::ImageAngleAdjuster::Ptr cameraPoseAdjuster(new ConcreteAngleAdjuster(cameraPose, M_PI/4 + M_PI/12));
    d3t12::CubeCenterTargeter::Ptr cameraTargeter(new d3t12::CubeCenterTargeter(
        imageCapturer,
        cameraPoseAdjuster
    ));

    d3t12::CubeCenterTargeter::Ptr motorTargeter(new d3t12::CubeTopTargeter(
        imageCapturer,
        d3t12::ImageAngleAdjuster::Ptr(new ConcreteAngleAdjuster(cameraPose, M_PI/4)),
        d3t12::CenterTargetParameters(0.25, 0.75, 0.15, cv::Point(320,240))
    ));

    d3t12::CubePositionFinder::Ptr finder(new d3t12::CubePositionFinder(angleGetter, 0.34, 0.03, 0.02));

	d3t12::Prehensor::Ptr prehensor(new d3t12::Prehensor);

	d3t12::JourneyBackPack::Ptr backpack(new d3t12::JourneyBackPack);

	d3t12::JourneyStateFactory::Ptr stateFactory(new d3t12::JourneyStateFactory(
		poseGetter,
		poseCommander,
		questionGetter,
		questionAsker,
		confirmationGetter,
		pathInformer,

		colorList,
		leds,

		pathPlanner,

		detectorFactory,
		image,
		cameraTargeter,
		motorTargeter,
		finder,
	
		cameraPoseAdjuster,
		prehensor,

		dropList,

		backpack
	));

	boost::thread mainThread(factoryThread, stateFactory);

	ros::spin();
	
	return 0;
}