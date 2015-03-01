#include <vision/WhiteCubeDetector.h>
#include <vision/SquareFilter.h>

namespace d3t12 {

static uint8_t get8bitsAt(cv::Mat& mat, int x, int y) {
	return mat.data[y*640 + x];
}

cv::Rect WhiteCubeDetector::detectCube() {
	try {	
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

		cv::Mat colorNoBlack;
		sourceImage->copyTo(colorNoBlack, grayNoBlackXORED);

		cv::Mat canny_output;
				std::vector<cv::Vec4i> hierarchy, hierarchy2;
				std::vector<std::vector<cv::Point> > contours;
				cv::Canny( grayNoBlackXORED, canny_output, threshold, threshold*2, 3 );
				cv::findContours( canny_output, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

				std::vector<cv::Point> points;
				for(int i = 0; i < contours.size(); ++i) {
					cv::Rect rect = cv::boundingRect(contours[i]);
					cv::Point rectCenter = cv::Point((rect.x + rect.width/2), (rect.y + rect.height/2));

					if(rect.width > 15 && rect.height > 15 && 
						 rect.width < 200 && rect.height < 200 &&
						 abs(rect.width - rect.height) < 0.60*rect.height &&
						 get8bitsAt(grayNoBlackXORED, rectCenter.x, rectCenter.y) == 0
					) {
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
	} catch (cv::Exception& error) {
		return cv::Rect(0,0,0,0);
	}
}

WhiteCubeDetector::~WhiteCubeDetector() {}

}