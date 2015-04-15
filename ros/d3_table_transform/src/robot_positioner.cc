#include <ros/ros.h>
#include <geometry_msgs/PointStamped.h>
#include <tf/transform_listener.h>
#include <RosExitGuard.h>

#include <d3_table_transform/robotPose.h>

namespace d3t12 {
	namespace tf = d3_table_transform;
} 

int main(int argc, char** argv) {
	ros::init(argc, argv, "robot_positioner");
	ros::NodeHandle node;
	d3t12::SignalFunctor::Ptr exitGuard(new d3t12::RosExitGuard(node));
	d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);

	ros::Publisher posePublisher = node.advertise<d3t12::tf::robotPose>("robot_positioner/robot_pose", 1);

	tf::TransformListener listener(ros::Duration(10));
	
	while(exitGuard->good()) {
		ros::spinOnce();
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

		d3t12::tf::robotPose pose;
		pose.x = robotPoseOnTable.pose.position.x;
		pose.y = robotPoseOnTable.pose.position.y;
		pose.yaw = tf::getYaw(q);
		posePublisher.publish(pose);

		usleep(200000);
	}

	std::cout << "bye" << std::endl;

	return 0;
};