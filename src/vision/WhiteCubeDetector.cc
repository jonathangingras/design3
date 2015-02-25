#include <vision/WhiteCubeDetector.h>
#include <vision/SquareFilter.h>

namespace d3t12 {

static bool comparePointsY(cv::Point point1, cv::Point point2) {
    return ( point1.y < point2.y );
}

static bool compareContoursHeight(std::vector<cv::Point> contour1, std::vector<cv::Point> contour2) {
    std::sort(contour1.begin(), contour1.end(), comparePointsY);
    std::sort(contour2.begin(), contour2.end(), comparePointsY);

    return ( contour1.begin()->y  <  contour2.begin()->y );
}

static uint8_t get8bitsAt(cv::Mat& mat, int x, int y) {
	return mat.data[y*640 + x];
}

static bool scalarIsHigher(cv::Scalar first, cv::Scalar second) {
	return first[0] > second[0]; 
}

cv::Rect WhiteCubeDetector::detectCube() {
		/*cv::Mat gray;
		cv::cvtColor(*sourceImage, gray, CV_BGR2GRAY);

		int erosion_size = 2;
		cv::Mat element = cv::getStructuringElement(
			cv::MORPH_CROSS,
			cv::Size( 2*erosion_size + 1, 2*erosion_size+1 ),
			cv::Point( erosion_size, erosion_size )
		);
		
		cv::erode(gray, gray, element);
		//cv::erode(gray, gray, element);
		//cv::erode(gray, gray, element);
		//cv::erode(gray, gray, element);
		//cv::erode(gray, gray, element);

		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);

		cv::imshow("gray", gray);

		cv::Mat outHexagon;
		cv::inRange(gray, cv::Scalar(170), cv::Scalar(255), outHexagon);

		cv::imshow("hexa", outHexagon);
 
		cv::Mat canny_output;
        std::vector<cv::Vec4i> hierarchy;
        std::vector<std::vector<cv::Point> > contours, validContours;
        cv::Canny( gray, canny_output, threshold, threshold*2, 3 );
        cv::findContours( canny_output, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

        for(int i = 0; i < contours.size(); ++i) {
        	double area = cv::contourArea(contours[i]);
        	cv::drawContours( *sourceImage, contours, i, cv::Scalar(0,0,255), 2, 8, hierarchy, 0, cv::Point() );
        	
        	/*cv::Rect contourRect = cv::boundingRect(contours[i]);
        	cv::Mat contourRectMat( *sourceImage, contourRect ), contourRectMatMask;
        	
        	cv::inRange(contourRectMat, cv::Scalar(0,0,0), cv::Scalar(60,60,60), contourRectMatMask);

        	cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			cv::erode(contourRectMatMask, contourRectMatMask, element);
			
			for(int j = 0; j < 30; ++j) cv::dilate(contourRectMatMask, contourRectMatMask, element);

        	//bool middleIsBlack = 0 != cv::countNonZero(contourRectMatMask);
        	*/
        	/*if(area < 8000 && area > 500) {
        		validContours.push_back(contours[i]);
        	}
        }

        std::sort(validContours.begin(), validContours.end(), compareContoursHeight);

		return ( validContours.end() != validContours.begin() ? cv::boundingRect(*--validContours.end()) : cv::Rect() );
*/
		cv::Mat gray, grayNoBlack;
		cv::cvtColor(*sourceImage, gray, CV_BGR2GRAY);

		int erosion_size = 2;
		cv::Mat element = cv::getStructuringElement(
			cv::MORPH_ELLIPSE,
			cv::Size( 2*erosion_size + 1, 2*erosion_size+1 ),
			cv::Point( erosion_size, erosion_size )
		);
		
		cv::erode(gray, gray, element);
		cv::erode(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);

		cv::inRange(gray, cv::Scalar(100), cv::Scalar(255), grayNoBlack);

		cv::Mat grayNoBlackXORED;
		cv::bitwise_xor(grayNoBlack, cv::Mat(grayNoBlack.size(), CV_8UC1, 255), grayNoBlackXORED);

		//cv::imshow("grayNoBlack", grayNoBlackXORED);

		cv::Mat colorNoBlack;
		sourceImage->copyTo(colorNoBlack, grayNoBlackXORED);

		cv::Mat canny_output;
        std::vector<cv::Vec4i> hierarchy, hierarchy2;
        std::vector<std::vector<cv::Point> > contours;
        cv::Canny( grayNoBlackXORED, canny_output, threshold, threshold*2, 3 );
        cv::findContours( canny_output, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

        std::vector<cv::Point> points;
        for(int i = 0; i < contours.size(); ++i) {
        	//cv::drawContours( *sourceImage, contours, i, cv::Scalar(0,0,255), 2, 8, hierarchy, 0, cv::Point() );

        	cv::Rect rect = cv::boundingRect(contours[i]);
        	cv::Point rectCenter = cv::Point((rect.x + rect.width/2), (rect.y + rect.height/2));

        	if(rect.width > 15 && rect.height > 15 && 
        	   rect.width < 200 && rect.height < 200 &&
        	   abs(rect.width - rect.height) < 0.60*rect.height &&
        	   get8bitsAt(grayNoBlackXORED, rectCenter.x, rectCenter.y) == 0
        	) {
        		//cv::circle(*sourceImage, rectCenter, 2, cv::Scalar(0,255,0), 2);
        		//std::cout << rect << std::endl;
        		if(points.empty()) {
        			points.push_back(cv::Point(rect.x, rect.y));
        			points.push_back(cv::Point(rect.x + rect.width, rect.y + rect.height));
        		}
        		else if(!points.empty() &&
        			abs(rect.x - (--(--points.end() ))->x ) > 2*rect.width &&
        			abs(rect.x - 320) < abs((--(--points.end() ))->x - 320)
        		) {
        			*--(--points.end()) = (cv::Point(rect.x, rect.y));
        			*--points.end() = (cv::Point(rect.x + rect.width, rect.y + rect.height));
        		}
        		else if(!points.empty() &&
        			abs(rect.x - 320) < abs((--(--points.end() ))->x - 320)
        		) {
        			points.push_back(cv::Point(rect.x, rect.y));
        			points.push_back(cv::Point(rect.x + rect.width, rect.y + rect.height));
        		}
        	}
        }

		return cv::boundingRect(points);
}

WhiteCubeDetector::~WhiteCubeDetector() {}

}