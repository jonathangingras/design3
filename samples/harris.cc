#include <vision/vision.h>
#include <math.h>
#include <boost/thread.hpp>
#include <signal.h>

int thresh = 100;

std::vector<cv::Point> detect_corners(cv::Mat& out, cv::Mat& src) {
	cv::Mat gray;

    cv::cvtColor( src, gray, CV_BGR2GRAY );
    cv::Mat dst, dst_norm, dst_norm_scaled;
    dst = cv::Mat::zeros( src.size(), CV_32FC1 );



    /*int erosion_size = 3;
    cv::Mat element = cv::getStructuringElement(
            cv::MORPH_RECT,
            cv::Size( 2*erosion_size + 1, 2*erosion_size+1 ),
            cv::Point( erosion_size, erosion_size )
        );
    
    cv::erode(gray, gray, element);
    cv::erode(gray, gray, element);
    //cv::erode(gray, gray, element);

    cv::dilate(gray, gray, element);
    cv::dilate(gray, gray, element);
    cv::dilate(gray, gray, element);*/

    //cv::imshow("gray", gray);
 
    // Detecting corners
    cv::cornerHarris( gray, dst, 7, 15, 0.05, cv::BORDER_DEFAULT );
 
    // Normalizing
    cv::normalize( dst, dst_norm, 0, 255, cv::NORM_MINMAX, CV_32FC1, cv::Mat() );
    cv::convertScaleAbs( dst_norm, dst_norm_scaled );
 
    // Drawing a circle around corners
    std::vector<cv::Point> corners;
    for( int j = 0; j < dst_norm.rows ; j++ ) {
        for( int i = 0; i < dst_norm.cols; i++ ) {
            if( (int) dst_norm.at<float>(j,i) > thresh ) {
                //circle( dst_norm_scaled, Point( i, j ), 5,  Scalar(0), 2, 8, 0 );
                corners.push_back(cv::Point(i,j));
            }
        }
    }

    for(std::vector<cv::Point>::iterator i = corners.begin(); i != corners.end(); ++i) {
        cv::circle( dst_norm_scaled, *i, 5, cv::Scalar(0), 2, 8, 0 );
        /*for(std::vector<cv::Point>::iterator j = corners.begin(); j != corners.end(); ++j) {
            if(i == j) continue;

            std::vector<cv::Point>::iterator higher = (i->y < j->y ? i : j), lower = (higher == i ? j : i);
            int distance_threshold = (int)((higher->y/60)*60.0*0.39);

            float distance = sqrt( abs(pow(higher->x - lower->x, 2)) + abs(pow(higher->y - lower->y, 2)) );
            if((int)distance < distance_threshold) cv::line(dst_norm_scaled, *higher, *lower, cv::Scalar(0,0,255), 1);
        }*/
    }

    out = dst_norm_scaled;
    return corners;
}

void capture_and_detect(cv::Mat* out, cv::VideoCapture* in, bool* done) {
    while(!*done) {
        cv::Mat src;
        *in >> src;
 
        //std::vector<cv::Point> points = detect_corners(*out, src);
        //cv::Rect rect = cv::boundingRect(points);
        //cv::rectangle(*out, rect, cv::Scalar(0,0,255));

        cv::Mat canny_output, gray;
        cv::cvtColor( src, gray, CV_BGR2GRAY );
        std::vector<cv::Vec4i> hierarchy;
        std::vector<std::vector<cv::Point> > contours;
        cv::Canny( gray, canny_output, thresh, thresh*2, 3 );
        cv::findContours( canny_output, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

        cv::RNG rng(12345);
        cv::Mat drawing = cv::Mat::zeros( canny_output.size(), CV_8UC3 );
        for( int i = 0; i < contours.size(); i++ ) {
            cv::Scalar color = cv::Scalar( rng.uniform(0, 255), rng.uniform(0,255), rng.uniform(0,255) );
            cv::drawContours( src, contours, i, color, 2, 8, hierarchy, 0, cv::Point() );
        }

        /*std::vector<std::vector<cv::Point> > squares;
        std::vector<cv::Point> approx;
        for (size_t i = 0; i < contours.size(); i++)
        {
                // approximate contour with accuracy proportional
                // to the contour perimeter
                cv::approxPolyDP(cv::Mat(contours[i]), approx, cv::arcLength(cv::Mat(contours[i]), true)*0.05, true);
                // Note: absolute value of an area is used because
                // area may be positive or negative - in accordance with the
                // contour orientation
                //if (//approx.size() > 3 &&
                //        fabs(cv::contourArea(cv::Mat(approx))) > 100// &&
                //        //cv::isContourConvex(cv::Mat(approx))
                //    )
                //{
                        //double maxCosine = 0;
                        //for (int j = 2; j < 5; j++)
                        //{
                        //        double cosine = fabs(cv::angle(approx[j%4], approx[j-2], approx[j-1]));
                        //        maxCosine = MAX(maxCosine, cosine);
                        //}
                        //if (maxCosine < 0.3)
                                squares.push_back(approx);
                //}
        }*/

        /*for(size_t i = 0; i < squares.size(); i++)
        {
            const cv::Point* p = &squares[i][0];
            int n = (int)squares[i].size();
            cv::polylines(src, &p, &n, 1, true, cv::Scalar(0,0,255), 3, CV_AA);
        }*/

        cv::imshow("corners", src);
        cv::waitKey(30);
    }
    std::cout << "thread bye" << std::endl;
}

bool done;
void sighandle(int signal) {
    done = true;
}

int main(int argc, char** argv)
{
    cv::Mat src, dst;
    // Load source image and convert it to gray
    //src = cv::imread( argv[1], 1 );
    cv::VideoCapture capturer(0);
    capturer >> src;
    boost::mutex mutex;

    //boost::thread capturer_thread_object(capturer_thread, &src, &capturer, &mutex);
    //boost::thread detector_thread_object(detector_thread, &dst, &src, &mutex);
    signal(SIGINT, sighandle);
    done = false;
    boost::thread capture_and_detect_thread(capture_and_detect, &dst, &capturer, &done);

    // Showing the result
    //namedWindow( "corners_window", CV_WINDOW_AUTOSIZE );
    pause();
    done = true;
    capture_and_detect_thread.join();
    std::cout << "main bye" << std::endl;

    return(0);
}