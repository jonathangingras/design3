#include <vision/WhiteCubeDetector.h>

namespace d3t12 {

static bool comparePointsY(cv::Point point1, cv::Point point2) {
    return ( point1.y < point2.y );
}

static bool compareContoursHeight(std::vector<cv::Point> contour1, std::vector<cv::Point> contour2) {
    std::sort(contour1.begin(), contour1.end(), comparePointsY);
    std::sort(contour2.begin(), contour2.end(), comparePointsY);

    return ( contour1.begin()->y  <  contour2.begin()->y );
}

cv::Rect WhiteCubeDetector::detectCube() {
		cv::Mat gray;
		cv::cvtColor(*sourceImage, gray, CV_BGR2GRAY);

		int erosion_size = 2;
		cv::Mat element = cv::getStructuringElement(
			cv::MORPH_ELLIPSE,
			cv::Size( 2*erosion_size + 1, 2*erosion_size+1 ),
			cv::Point( erosion_size, erosion_size )
		);
		
		cv::erode(gray, gray, element);
		cv::erode(gray, gray, element);
		cv::erode(gray, gray, element);
		cv::erode(gray, gray, element);
		cv::erode(gray, gray, element);

		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
 
		cv::Mat canny_output;
        std::vector<cv::Vec4i> hierarchy;
        std::vector<std::vector<cv::Point> > contours, validContours;
        cv::Canny( gray, canny_output, threshold, threshold*2, 3 );
        cv::findContours( canny_output, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

        for(int i = 0; i < contours.size(); ++i) {
        	double area = cv::contourArea(contours[i]);
        	
        	cv::Rect contourRect = cv::boundingRect(contours[i]);
        	cv::Mat contourRectMat( *sourceImage, contourRect ), contourRectMatMask;
        	
        	cv::inRange(contourRectMat, cv::Scalar(0,0,0), cv::Scalar(60,60,60), contourRectMatMask);

        	cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			
			for(int j = 0; j < 30; ++j) cv::dilate(contourRectMatMask, contourRectMatMask, element);

			//cv::imshow("white", contourRectMatMask);
			//cv::waitKey(800);

        	bool middleWhite = (0 == cv::countNonZero(contourRectMatMask) );
        	
        	if(area < 10000 && area > 500 && middleWhite) {
        		validContours.push_back(contours[i]);
        	}
        }

        std::sort(validContours.begin(), validContours.end(), compareContoursHeight);

		return ( validContours.end() != validContours.begin() ? cv::boundingRect(*--validContours.end()) : cv::Rect() );
}

WhiteCubeDetector::~WhiteCubeDetector() {}

}