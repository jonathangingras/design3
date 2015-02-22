#include <ros/ros.h>
#include <geometry_msgs/PointStamped.h>
#include <tf/transform_listener.h>
#include <RosExitGuard.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "robot_positioner");
	ros::NodeHandle node;
	d3t12::SignalFunctor::Ptr exitGuard(new d3t12::RosExitGuard(node));
	d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);

	tf::TransformListener listener(ros::Duration(10));
	
	while(exitGuard->good()) {
		geometry_msgs::PoseStamped robotPoseOnRobot;
		robotPoseOnRobot.header.frame_id = "robot_center";
		robotPoseOnRobot.header.stamp = ros::Time();

		robotPoseOnRobot.pose.position.x = 0;
		robotPoseOnRobot.pose.position.y = 0;
		robotPoseOnRobot.pose.position.z = 0;
		robotPoseOnRobot.pose.orientation = tf::createQuaternionMsgFromYaw(0);
		
		geometry_msgs::PoseStamped robotPoseOnTable;
		try {
			listener.transformPose("d3_table_origin", robotPoseOnRobot, robotPoseOnTable);
		} catch(tf::TransformException& ex) {
			ROS_ERROR_STREAM("could not transform robot position: " << ex.what());
			continue;
		}
		tf::Quaternion q;
		tf::quaternionMsgToTF(robotPoseOnTable.pose.orientation, q);

		ROS_INFO_STREAM("robot position: " << robotPoseOnTable.pose.position.x << ", " << robotPoseOnTable.pose.position.y << ", " << tf::getYaw(q));
	}

	std::cout << "bye" << std::endl;

	return 0;
};