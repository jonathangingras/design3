#include <ros/ros.h>

#include <common/common.h>
#include <driver/driver.h>
#include <rest/rest.h>
#include <vision/vision.h>
#include <ai/ai.h>

#include <d3_table_transform/robotPose.h>
namespace d3t12 {
	namespace tf = d3_table_transform;
}

struct PoseReceiver : public d3t12::PoseGetter {
	d3t12::RobotPose robotPose;
	boost::mutex mutex;

	inline PoseReceiver(): robotPose(0,0,0) {}

	void callback(const d3t12::tf::robotPose::ConstPtr& inputPose) {
		mutex.lock();
		robotPose = d3t12::RobotPose(inputPose->x, inputPose->y, inputPose->yaw);
		mutex.unlock();
	}

	d3t12::RobotPose getPose() {
		mutex.lock();
		d3t12::RobotPose pose = robotPose;
		mutex.unlock();
		return pose;
	}
};

struct ConcretePoseCommander : public d3t12::PoseCommander {
	d3t12::MicroControllerCommandPort::Ptr commandPort;
	d3t12::MotorController motors;
	std::ifstream inPort;

	inline ConcretePoseCommander(d3t12::MicroControllerCommandPort::Ptr _commandPort): 
		inPort("/dev/ttySTM32"), commandPort(_commandPort), motors(_commandPort) {
		*commandPort << "clcmode p";
	}

	bool getFlag() {
		int ret;
		*commandPort << "getflag";
		inPort >> ret;
		return ret;
	}

	void commandPose(d3t12::RobotPose pose) {
		if(pose.yaw) {
			motors.rotate(pose.yaw);
			while(!getFlag());
		}
		if(pose.x || pose.y) {
			motors.moveTo(pose.x, pose.y);
			while(!getFlag());
		}
	}
};

struct ConcreteQuestionGetter : public d3t12::QuestionGetter { //must be moved to other node as a receiver of std_msgs::String message
	std::string getQuestion() {
		/*d3t12::CURLGetter getter("https://132.203.14.228");
  		d3t12::AtlasJSONDecoder decoder;
  		std::string atlas_told = getter.performGET();
    	return decoder.questionStr(atlas_told);*/
    	return "Who likes Sausage?";
	}
};

struct ConcreteQuestionAsker : public d3t12::QuestionAsker {
	std::string ask(std::string question) {
		// AntoineCode with Popener
		return "Germany";
	}
};

struct ConcreteConfirmationGetter : public d3t12::ConfirmationGetter {
	bool ok() {
		//implement from topic received from gui button
		return true;
	}
};

struct ConcretePathInformer : public d3t12::PathInformer {
	void informPath(const std::vector<d3t12::PathCommand>& path) {
		//implement as path publisher to gui
	}
};

struct ConcreteAngleAdjuster : public d3t12::ImageAngleAdjuster {
private:
    d3t12::CameraPoseHandler::Ptr cameraPose;

    inline float rad2deg(double rad) {
        return (rad*180)/M_PI;
    }

    inline double deg2rad(float deg) {
        return (deg*M_PI)/180;
    }

public:
    inline ConcreteAngleAdjuster(d3t12::CameraPoseHandler::Ptr _cameraPose):
        cameraPose(_cameraPose) {}

    void adjustY(float degrees) {
        cameraPose->increasePitch(deg2rad(degrees));
    }

    void adjustX(float degrees) {
        cameraPose->increaseYaw(deg2rad(degrees));
    }
};

struct ConcreteAngleGetter : public d3t12::ImageAngleGetter {
private:
    d3t12::CameraPoseHandler::Ptr cameraPose;

public:
    inline ConcreteAngleGetter(d3t12::CameraPoseHandler::Ptr _cameraPose):
        cameraPose(_cameraPose) {}

    double getPitch() {
        return cameraPose->getPitch();
    }

    double getYaw() {
        return cameraPose->getYaw();
    }
};

struct CameraImageCapturer : public d3t12::ImageCapturer {
private:
    d3t12::CameraCapturer* capturer;
    d3t12::cvMatPtr srcImage;

public:
    inline CameraImageCapturer(int camId, d3t12::cvMatPtr _srcImage): 
        capturer(new d3t12::CameraCapturer(camId)), srcImage(_srcImage) {}
    
    ~CameraImageCapturer() {
        delete capturer;
    }

    void capture() {
        *capturer >> *srcImage;
    }
};

int main(int argc, char** argv) {
	ros::init(argc, argv, "design3_robot_journey");
	ros::NodeHandle node;

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

	d3t12::PoseCommander::Ptr poseCommander(new ConcretePoseCommander(commandPort));

	d3t12::LEDMatrixController::Ptr leds(new d3t12::LEDMatrixController(commandPort));
	d3t12::Prehensor::Ptr prehensor(new d3t12::Prehensor);
	d3t12::CameraPoseHandler::Ptr cameraPose(new d3t12::CameraPoseHandler);

	d3t12::QuestionGetter::Ptr questionGetter(new ConcreteQuestionGetter);
	d3t12::QuestionAsker::Ptr questionAsker(new ConcreteQuestionAsker);
	d3t12::ConfirmationGetter::Ptr confirmationGetter(new ConcreteConfirmationGetter);
	d3t12::PathInformer::Ptr pathInformer(new ConcretePathInformer);

	d3t12::PathPlanner::Ptr pathPlanner(new d3t12::PathPlanner);

	d3t12::cvMatPtr image(new cv::Mat);
	d3t12::ImageCaturer::Ptr imageCapturer();

	d3t12::ImageAngleAdjuster()

	ros::spin();
	return 0;
}