#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

#include <vision/vision.h>
#include <driver/CameraCapturer.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "d3_robot_cam_broadcaster");
	ros::NodeHandle node;

	image_transport::ImageTransport it(node);
	image_transport::Publisher publisher = it.advertise("robot_camera/image", 1);

	d3t12::CameraCapturer capturer(0);
	cv::Mat image;

	ros::Rate rate(10);
	while(node.ok()) {
		capturer >> image;
		sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();
		publisher.publish(msg);
		ros::spinOnce();
		rate.sleep();
	}

	std::cout << "bye" << std::endl;
}