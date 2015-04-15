#include <vision/BlackCubeDetector.h>
#include <opencv2/features2d.hpp>

namespace d3t12 {

static bool comparePointsY(cv::Point point1, cv::Point point2) {
		return ( point1.y < point2.y );
}

static bool compareContoursHeight(std::vector<cv::Point> contour1, std::vector<cv::Point> contour2) {
		std::sort(contour1.begin(), contour1.end(), comparePointsY);
		std::sort(contour2.begin(), contour2.end(), comparePointsY);

		return ( (--contour1.end())->y  <  (--contour2.end())->y );
}

static uint8_t get8bitsAt(cv::Mat& mat, int x, int y) {
	return mat.data[y*640 + x];
}

static cv::Mat getBlackMask(cv::Mat& image) {
	cv::Mat gray, grayNoBlack;
		cv::cvtColor(image, gray, CV_BGR2GRAY);

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

		return grayNoBlackXORED;
}

cv::Rect BlackCubeDetector::detectCube() {
		cv::Mat gray;
		cv::cvtColor(*sourceImage, gray, CV_BGR2GRAY);

		int erosion_size = 2;
		cv::Mat element = cv::getStructuringElement(
			cv::MORPH_RECT,
			cv::Size( 2*erosion_size + 1, 2*erosion_size+1 ),
			cv::Point( erosion_size, erosion_size )
		);
		
		cv::erode(gray, gray, element);

		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);
		cv::dilate(gray, gray, element);

		cv::imshow("gray1", gray);

		cv::Mat graySave;
		gray.copyTo(graySave);

		IncrementalRect incRect;

		// normal case

		cv::Mat elementNormal = cv::getStructuringElement(
			cv::MORPH_CROSS,
			cv::Size( 2*erosion_size + 1, 2*erosion_size+1 ),
			cv::Point( erosion_size, erosion_size )
		);

		cv::dilate(graySave, graySave, elementNormal);
		cv::dilate(graySave, graySave, elementNormal);
		cv::dilate(graySave, graySave, elementNormal);
		cv::dilate(graySave, graySave, elementNormal);
		
		cv::dilate(graySave, graySave, elementNormal);
		cv::dilate(graySave, graySave, elementNormal);
		cv::dilate(graySave, graySave, elementNormal);
		cv::dilate(graySave, graySave, elementNormal);
		cv::dilate(graySave, graySave, elementNormal);
		
		cv::dilate(graySave, graySave, element);
		cv::dilate(graySave, graySave, element);
		cv::dilate(graySave, graySave, element);

		cv::erode(graySave, graySave, element);
		cv::erode(graySave, graySave, element);
		cv::erode(graySave, graySave, element);
		cv::erode(graySave, graySave, element);
		cv::erode(graySave, graySave, element);
		
		cv::erode(graySave, graySave, element);
		cv::erode(graySave, graySave, element);
		cv::erode(graySave, graySave, element);

		cv::imshow("gray2", graySave);
		cv::SimpleBlobDetector::Params params;
		params.maxArea = 1000000;
		cv::SimpleBlobDetector blobber(params);
		
		std::vector<cv::KeyPoint> keypoints;
		blobber.detect( gray, keypoints);
		int i;
		for(i = 0; i < keypoints.size(); ++i) {
			cv::rectangle(*sourceImage, cv::Rect(keypoints[i].pt.x, keypoints[i].pt.y, 4, 4), cv::Scalar(0,0,255));
			incRect += cv::Rect(keypoints[i].pt.x - 50, keypoints[i].pt.y - 50, 100, 100);
		}

		if(i) return incRect.toCvRect();

		//morphology hasard worst case
 
		cv::Mat canny_output;
				std::vector<cv::Vec4i> hierarchy, hierarchy2;
				std::vector<std::vector<cv::Point> > contours, contours2, validContours;
				cv::Canny( gray, canny_output, threshold, threshold*2, 3 );
				cv::findContours( canny_output, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

				cv::Mat element2 = cv::getStructuringElement(
			cv::MORPH_CROSS,
			cv::Size( 7, 7 ),
			cv::Point( 2, 2 )
		);
		cv::Mat element3 = cv::getStructuringElement(
			cv::MORPH_CROSS,
			cv::Size( 3, 3 ),
			cv::Point( 1, 1 )
		);

		cv::dilate(canny_output, canny_output, element2);
		cv::dilate(canny_output, canny_output, element2);
		cv::dilate(canny_output, canny_output, element2);
		cv::dilate(canny_output, canny_output, element2);
		cv::dilate(canny_output, canny_output, element2);

				cv::erode(canny_output, canny_output, element2);
				cv::erode(canny_output, canny_output, element2);
				cv::erode(canny_output, canny_output, element2);
				cv::erode(canny_output, canny_output, element2);

				cv::Mat morphologyHasard, grayMorphologyHasard;
				sourceImage->copyTo(morphologyHasard, canny_output);

				cv::erode(morphologyHasard, morphologyHasard, element2);
				cv::erode(morphologyHasard, morphologyHasard, element2);

				cv::dilate(morphologyHasard, morphologyHasard, element2);
				cv::dilate(morphologyHasard, morphologyHasard, element2);
				cv::dilate(morphologyHasard, morphologyHasard, element2);
				cv::dilate(morphologyHasard, morphologyHasard, element2);
				
				cv::cvtColor(morphologyHasard, grayMorphologyHasard, CV_BGR2GRAY);

				cv::rectangle(grayMorphologyHasard, cv::Point(0,0), cv::Point(15,15), cv::Scalar(0), CV_FILLED);

				cv::findContours( grayMorphologyHasard, contours2, hierarchy2, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

				cv::Mat blackMask = getBlackMask(*sourceImage);

				
				for(int i = 0; i < contours2.size(); ++i) {
					cv::Rect rect = cv::boundingRect(contours2[i]);
					
					cv::Point rectCenter( rect.x + rect.width/2, rect.y + rect.height - 3 );

					if(get8bitsAt(blackMask, rectCenter.x, rectCenter.y) == 255 && rect.y > 20) {
						incRect += rect;

						cv::rectangle(*sourceImage, cv::boundingRect(contours2[i]), cv::Scalar(255,0,0));
					}
				}

		//		std::sort(contours2.begin(), contours2.end(), compareContoursHeight);

		//return ( contours2.end() != contours2.begin() ? cv::boundingRect(*--contours2.end()) : cv::Rect() );

		return incRect.toCvRect();
}

BlackCubeDetector::~BlackCubeDetector() {}

}