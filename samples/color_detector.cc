#include <math.h>
#include <boost/thread.hpp>
#include <signal.h>
#include <vision/vision.h>

void capture_and_detect(cv::Mat* out, cv::VideoCapture* in, d3t12::ColorFilter* filter, bool* done) {
    while(!*done) {
        cv::Mat in_mat, src;
        *in >> in_mat;
        src = in_mat/*.clone()*/;

        filter->filter(*out, src);
        //cv::Rect rect = cv::boundingRect(*out);
        //cv::rectangle(in_mat, rect, cv::Scalar(0,0,255));
        
        std::vector<cv::Vec4i> hierarchy;
        std::vector<std::vector<cv::Point> > contours;
        cv::findContours( *out, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0, 0) );

        /*for(int i = 0; i < contours.size(); ++i)
            cv::drawContours( src, contours, i, cv::Scalar(0,0,255), 4, 8, hierarchy, 0, cv::Point() );
        */

        for(int i = 0; i < contours.size(); ++i)
            cv::rectangle(src, cv::boundingRect(contours[i]), cv::Scalar(0,0,255));

        cv::imshow("corners", src);
        //cv::imshow("orig", in_mat);
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
    
    d3t12::ColorJSONLoader loader;
    loader.setFile("colors.json");
    loader.loadJSON();
    d3t12::ColorPalette palette;
    loader.fillPalette(palette);
    d3t12::ColorFilter filter(palette.getColor(argv[1]));

    //boost::thread capturer_thread_object(capturer_thread, &src, &capturer, &mutex);
    //boost::thread detector_thread_object(detector_thread, &dst, &src, &mutex);
    signal(SIGINT, sighandle);
    done = false;
    boost::thread capture_and_detect_thread(capture_and_detect, &dst, &capturer, &filter, &done);

    // Showing the result
    //namedWindow( "corners_window", CV_WINDOW_AUTOSIZE );
    pause();
    done = true;
    capture_and_detect_thread.join();
    std::cout << "main bye" << std::endl;

    return(0);
}