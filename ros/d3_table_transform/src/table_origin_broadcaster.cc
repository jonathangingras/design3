#include <ros/ros.h>
#include <TfPublisher.h>
#include <RosExitGuard.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "table_origin_broadcaster");
	ros::NodeHandle node;
	d3t12::SignalFunctor::Ptr exitGuard(new d3t12::RosExitGuard(node));
	d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);

	d3t12::TfPublisher publisher(
		"camera_depth_frame", "d3_table_origin", 
		tf::Vector3(0.42, -0.35, 0), d3t12::quaternionFromRPY(0, 0, -0.5235987755982988*0.81)
	);
	
	publisher.publishTfInLoop(100, exitGuard);
	std::cout << "bye" << std::endl;

	return 0;
};