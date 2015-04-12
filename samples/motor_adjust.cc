#include <common/common.h>
#include <driver/driver.h>
#include <rest/rest.h>
#include <vision/vision.h>
#include <ai/ai.h>

struct ConcretePoseCommander : public d3t12::PoseCommander {
	d3t12::MicroControllerCommandPort::Ptr commandPort;
	d3t12::MotorController motors;

	inline ConcretePoseCommander(d3t12::MicroControllerCommandPort::Ptr _commandPort): 
		commandPort(_commandPort), motors(_commandPort) {
		*commandPort << "clcmode p";
		//*commandPort << "setecho off";
	}

	void getFlag() {
		d3t12::NonBlockIfStream inPort("/dev/ttySTM32");
		std::string inStr;
		do {
			*commandPort << "getflag";
			d3t12::sleepSecondsNanoSeconds(0, 7000000);
			inPort >> inStr;
		} while(inStr.empty() || *(inStr.end() - 3) != '1');
	}

	void commandDirectly(d3t12::RobotPose pose) {
		*commandPort << "clcmode p";

		if( fabs(pose.yaw) >= 0.01 ) {
			motors.rotate( pose.yaw );
			getFlag();
		}
		if( fabs(pose.x) >= 0.005 || fabs(pose.y) >= 0.005 ) {
			motors.moveTo( (fabs(pose.x) >= 0.005 ? pose.x : 0), (fabs(pose.y) >= 0.005 ? pose.y : 0) );
			getFlag();
		}
	}

	void commandPose(d3t12::RobotPose pose) {}
};

struct ConcreteAngleAdjuster : public d3t12::ImageAngleAdjuster {
    d3t12::CameraPoseHandler::Ptr cameraPose;

    inline float rad2deg(double rad) {
        return (rad*180)/M_PI;
    }

    inline double deg2rad(float deg) {
        return (deg*M_PI)/180;
    }

    inline ConcreteAngleAdjuster(d3t12::CameraPoseHandler::Ptr _cameraPose):
        cameraPose(_cameraPose) {}

    void resetAngle() {
    	cameraPose->setPitch(M_PI/4);
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
    	cameraPose->setPitch(M_PI/4 - M_PI/6);
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

int main(int argc, char** argv) {
	d3t12::SignalFunctor::Ptr exitGuard(new d3t12::ExitGuard);
    d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);

	d3t12::MicroControllerCommandPort::Ptr commandPort(
		new d3t12::MicroControllerCommandPort(
			d3t12::MicroControllerCommandPort::OStreamPtr(
				new std::ofstream("/dev/ttySTM32")
			)
		)
	);

	d3t12::PoseCommander::Ptr poseCommander(new ConcretePoseCommander(commandPort));

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

	d3t12::ImageAngleAdjuster::Ptr cameraPoseAdjuster(new ConcreteAngleAdjuster(cameraPose));
    d3t12::CubeCenterTargeter::Ptr cameraTargeter(new d3t12::CubeCenterTargeter(
        imageCapturer,
        cameraPoseAdjuster,
        d3t12::CenterTargetParameters(1.0, 2.0, 0.125, cv::Point(320,240))
    ));

    //d3t12::ImageAngleAdjuster::Ptr motorAdjuster(new ConcreteMotorAdjuster(cameraPose, poseCommander));
    d3t12::CubeCenterTargeter::Ptr motorTargeter(new d3t12::CubeTopTargeter(
        imageCapturer,
        cameraPoseAdjuster,
        d3t12::CenterTargetParameters(1.0, 2.0, 0.125, cv::Point(320,240))
    ));
    //d3t12::CubeCenterTargeter::Ptr motorTargeter(cameraTargeter);

    d3t12::CubePositionFinder::Ptr finder(new d3t12::CubePositionFinder(angleGetter, 0.34, 0.03, 0.02));

	d3t12::Prehensor::Ptr prehensor(new d3t12::Prehensor);


	//////////////////////////////
	d3t12::CubeDetector::Ptr detector = detectorFactory->createCubeDetector(argv[1], image);
	motorTargeter->setDetector(detector);
	motorTargeter->resetAngle();
	
	bool error = true;
	while(error && exitGuard->good()) {
		try {
			motorTargeter->targetCenter();
		} catch(d3t12::NoCubeFoundException& err) {
			error = true;
			continue;
		}
		cv::imshow("image", *image);
		error = false;
	}
	if(!exitGuard->good()) return 1;


	d3t12::CubeRelativePosition target = finder->findCubePosition();
	poseCommander->commandDirectly(d3t12::RobotPose(target.x - 0.36, target.y - 0.02, 0));


	prehensor->open();
	std::cout << "opened" << std::endl;
	poseCommander->commandDirectly(d3t12::RobotPose(0.20,0,0));
	std::cout << "advanced" << std::endl;
	d3t12::sleepSecondsNanoSeconds(2,0);
	prehensor->close();
	std::cout << "closed" << std::endl;
	d3t12::sleepSecondsNanoSeconds(2,0);
	prehensor->open();
	poseCommander->commandDirectly(d3t12::RobotPose(-0.025,0,0));
	d3t12::sleepSecondsNanoSeconds(1,0);
	poseCommander->commandDirectly(d3t12::RobotPose(0.08,0,0));
	d3t12::sleepSecondsNanoSeconds(1,0);

	prehensor->close();
	//cameraTargeter->targetCenter();
	/*prehensor->rise();
	prehensor->lower();
	prehensor->open();
	poseCommander->commandDirectly(d3t12::RobotPose(-0.15,0,0));
	prehensor->close();
	prehensor->lower();*/
	///////////////////////////////
	
	return 0;
}