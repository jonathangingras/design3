#include <common/common.h>
#include <vision/vision.h>
#include <driver/CameraCapturer.h>

int main(int argc, char** argv) {
    d3t12::cvMatPtr src(new cv::Mat);
    d3t12::CameraCapturer capturer(1);
    
    d3t12::ColorJSONLoader loader;
    loader.setFile("colors.json");
    loader.loadJSON();
    d3t12::ColorPalette::Ptr palette(new d3t12::ColorPalette);
    loader.fillPalette(*palette);

    d3t12::CubeDetectorFactory factory(palette);
    d3t12::CubeDetector::Ptr detector = factory.createCubeDetector(argv[1], src);

    d3t12::SignalFunctor::Ptr exitGuard(new d3t12::ExitGuard);
    d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);
    while(exitGuard->good()) {
        capturer >> *src;
        //*src = cv::imread(argv[2]);

        cv::Rect cubeRect = detector->detectCube();
        cv::rectangle(*src, cubeRect, cv::Scalar(0,255,0));

        cv::imshow("image", *src);
        cv::waitKey(30);
        //pause();
    }

    std::cout << "bye" << std::endl;

    return(0);
}
