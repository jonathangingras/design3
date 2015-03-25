#include <ros/ros.h>
#include <TfPublisher.h>
#include <RosExitGuard.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "robot_center_broadcaster");
	ros::NodeHandle node;
	d3t12::SignalFunctor::Ptr exitGuard(new d3t12::RosExitGuard(node));
	d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);

	d3t12::TfPublisher publisher(
		"ar_marker_0", "robot_center",
		tf::Vector3(0, -0.0525, -0.125), d3t12::quaternionFromRPY(M_PI/2, 3*M_PI/2, M_PI/2)
	);
	
	publisher.publishTfInLoop(100, exitGuard);
	std::cout << "bye" << std::endl;

	return 0;
};