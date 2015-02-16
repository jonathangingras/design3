#include <boost/thread.hpp>
#include <ros/ros.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/image_encodings.h>
#include <cv_bridge/cv_bridge.h>

#include <vision/vision.h>

d3t12::ColorFilter* filter;

void image_cb_ (const sensor_msgs::ImageConstPtr& callback_image) {
	std::vector<cv::Rect> results;
	cv::Mat src = cv_bridge::toCvCopy(callback_image, "bgr8")->image, out;
	
  	filter->filter(out, src);
        //cv::Rect rect = cv::boundingRect(out);
        //cv::rectangle(in_mat, rect, cv::Scalar(0,0,255));
        
        std::vector<cv::Vec4i> hierarchy;
        std::vector<std::vector<cv::Point> > contours;
        cv::findContours( out, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

        /*for(int i = 0; i < contours.size(); ++i)
            cv::drawContours( src, contours, i, cv::Scalar(0,0,255), 4, 8, hierarchy, 0, cv::Point() );
        */

        for(int i = 0; i < contours.size(); ++i)
            cv::rectangle(src, cv::boundingRect(contours[i]), cv::Scalar(0,0,255));

        cv::imshow("corners", src);
        //cv::imshow("orig", in_mat);
        cv::waitKey(30);
}

int main(int argc, char** argv) {
	ros::init (argc, argv, "color_detector");
	ros::NodeHandle nodeHandle;
	ros::Subscriber subscriberImage = nodeHandle.subscribe<sensor_msgs::Image>("/camera/rgb/image_color", 1, image_cb_);

    std::string color_config_path, color_string;
    nodeHandle.getParam("color_detector/color_config_path", color_config_path);
    nodeHandle.getParam("color_detector/color_string", color_string);

	d3t12::ColorJSONLoader loader;
    loader.setFile(color_config_path);
    loader.loadJSON();
    d3t12::ColorPalette palette;
    loader.fillPalette(palette);
    d3t12::ColorFilter filter_(palette.getColor(color_string));
	filter = &filter_;

	ros::spin();
}