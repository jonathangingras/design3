#include <string.h>
#include <ros/ros.h>
#include <d3_table_transform/robotPose.h>

#include <driver/driver.h>

namespace d3t12 {
	namespace tf = d3_table_transform;
}

struct RobotPositioner {
	boost::mutex mutex;
	d3t12::MotorController& motors;

	float x, y, yaw;
	int counter;

	inline RobotPositioner(d3t12::MotorController& _motors):
		motors(_motors), counter(0), x(0), y(0), yaw(0) {}

	void callback(const d3t12::tf::robotPose::ConstPtr& pose) {
		mutex.lock();
		if(++counter < 5000) {
			x += pose->x; y += pose->y; yaw += pose->yaw;
			mutex.unlock();
			return;
		}
		else {
			x /= counter; y /= counter; yaw /= counter;
			counter = 0;
		}
		
		motors.informPosition(x, y, yaw);

		mutex.unlock();
	}

	void goTo(float _x, float _y, float _yaw) {
		mutex.lock();
		float comX = _x - x, comY = _y - y, comYaw = _yaw - yaw;
		motors.commandPosition(comX, comY, comYaw);
		mutex.unlock();
	}
};

struct RemoteConsole {
	ros::NodeHandle* node;
	RobotPositioner* position; 
	d3t12::LEDMatrixController* leds;
	d3t12::Prehensor* prehensor;
	d3t12::CameraPoseHandler* cameraPose;

	inline RemoteConsole(
		ros::NodeHandle* _node,
		RobotPositioner* _position, 
		d3t12::LEDMatrixController* _leds,
		d3t12::Prehensor* _prehensor,
		d3t12::CameraPoseHandler* _cameraPose
	): node(_node), position(_position), leds(_leds), prehensor(_prehensor), cameraPose(_cameraPose) {}

	void printLine(const std::string& line) {
		std::cout << line << std::endl;
	}

	void prompt() { //ugly sorry, but not to be maintained, just for tests on table
		std::cout << " > ";
		std::string command;
		std::getline(std::cin, command);
		
		if(command == "pr up") {
			printLine("rising prehensor");
			prehensor->rise();
		} else if(command == "pr down") {
			printLine("lowering prehensor");
			prehensor->lower();
		} else if(command == "pr open") {
			printLine("opening prehensor");
			prehensor->open();
		} else if(command == "pr close") {
			printLine("closing prehensor");
			prehensor->close();
		} else if(command[0] == 'g' && command[1] == 'o') {
			double xyyaw[3] = {0,0,0};
			char commandCharArray[command.length() + 1];
			commandCharArray[0] = '\0';
			strcpy(commandCharArray, command.c_str());
			char* token;
			token = strtok(commandCharArray, " ,");
			for(int i = 0; i < 3; ++i) {
				token = strtok(NULL, " ,");
				xyyaw[i] = atof(token);
			}
			position->goTo(xyyaw[0], xyyaw[1], xyyaw[2]);
		} else if(command[0] == 'c' && command[1] == 'a' && command[2] == 'm') {
			double angles[2] = {0,0};
			char commandCharArray[command.length() + 1];
			commandCharArray[0] = '\0';
			strcpy(commandCharArray, command.c_str());
			char* token;
			token = strtok(commandCharArray, " ,");
			for(int i = 0; i < 2; ++i) {
				token = strtok(NULL, " ,");
				angles[i] = atof(token);
			}
			if(angles[0] && angles[1]) {
				printLine("setting cam pitch/yaw");
				cameraPose->setPitch(angles[0]);
				cameraPose->setYaw(angles[1]);
			} else {
				printLine("bad cam instruction!");
			}
		} else if(command[0] == 'l' && command[1] == 'e' && command[2] == 'd') {
			char commandCharArray[command.length() + 1];
			commandCharArray[0] = '\0';
			strcpy(commandCharArray, command.c_str());
			char* token;
			token = strtok(commandCharArray, " ,");
			token = strtok(NULL, " ,");
			printLine(token);
			if(!strcmp(token, "add")) {
				token = strtok(NULL, " ,");
				if(token) leds->addNew(token);
				else leds->addBlank();
			} else if(!strcmp(token, "alloff")) {
				printLine("turning all LEDs off");
				leds->turnAllOff();
			} else if(!strcmp(token, "master")) {
				token = strtok(NULL, " ,");
				if(token) {
					if(!strcmp(token, "on")) {
						printLine("turning master LED on");
						leds->turnMasterOn();
					} else if(!strcmp(token, "off")) {
						printLine("turning master LED off");
						leds->turnMasterOff();
					}
				}
				else {
					printLine("bad led command!");
				}
			}
		} else if(command == "exit") {
			node->shutdown();
		} else {
			printLine("no such command!");
		}
	}

	void operator()() {
		while(node->ok()) {
			prompt();
		}
	}
};

int main(int argc, char** argv) {
	ros::init(argc, argv, "robot_remote");
	ros::NodeHandle node;

	d3t12::MicroControllerCommandPort::OStreamPtr stream(
				new std::ofstream("/dev/ttySTM32")
			);

	//Micro-controller command port
	d3t12::MicroControllerCommandPort::Ptr commandPort(
		new d3t12::MicroControllerCommandPort(
			stream
		)
	);
	 
	d3t12::MotorController motors(commandPort);
	d3t12::LEDMatrixController leds(commandPort);
	d3t12::Prehensor prehensor;
	d3t12::CameraPoseHandler cameraPose;

	RobotPositioner positioner(motors);
	ros::Subscriber robotPoseReceiver = node.subscribe<d3t12::tf::robotPose>("robot_positioner/robot_pose", 1, &RobotPositioner::callback, &positioner);

	RemoteConsole remoteConsole(&node, &positioner, &leds, &prehensor, &cameraPose);
	boost::thread remoteConsoleThread(remoteConsole);

	ros::spin();
	remoteConsoleThread.join();

	return 0;
}