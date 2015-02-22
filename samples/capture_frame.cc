#include <common/common.h>
#include <vision/vision.h>
#include <driver/CameraCapturer.h>

int main(int argc, char** argv) {
    d3t12::SignalFunctor::Ptr exitGuard(new d3t12::ExitGuard);
    d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);
    
    d3t12::cvMatPtr src(new cv::Mat);
    d3t12::CameraCapturer capturer(1);

    capturer >> *src;
    cv::imwrite(argv[1], *src);

    cv::imshow("image", *src);
    cv::waitKey(1500);

    return(0);
}