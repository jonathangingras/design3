#include <common/common.h>
#include <vision/vision.h>
#include <driver/driver.h>
#include <ai/ai.h>

class ConcreteAngleAdjuster : public d3t12::ImageAngleAdjuster {
private:
    d3t12::CameraPoseHandler::Ptr cameraPose;

    inline float rad2deg(double rad) {
        return (rad*180)/M_PI;
    }

    inline double deg2rad(float deg) {
        return (deg*M_PI)/180;
    }

public:
    inline ConcreteAngleAdjuster(d3t12::CameraPoseHandler::Ptr _cameraPose):
        cameraPose(_cameraPose) {}

    void adjustY(float degrees) {
        cameraPose->increasePitch(deg2rad(degrees));
    }

    void adjustX(float degrees) {
        cameraPose->increaseYaw(deg2rad(degrees));
    }
};

class ConcreteAngleGetter : public d3t12::ImageAngleGetter {
private:
    d3t12::CameraPoseHandler::Ptr cameraPose;

public:
    inline ConcreteAngleGetter(d3t12::CameraPoseHandler::Ptr _cameraPose):
        cameraPose(_cameraPose) {}

    double getPitch() {
        return cameraPose->getPitch();
    }

    double getYaw() {
        return cameraPose->getYaw();
    }
};

class CameraImageCapturer : public d3t12::ImageCapturer {
private:
    d3t12::CameraCapturer* capturer;
    d3t12::cvMatPtr srcImage;

public:
    inline CameraImageCapturer(int camId, d3t12::cvMatPtr _srcImage): 
        capturer(new d3t12::CameraCapturer(camId)), srcImage(_srcImage) {}
    
    ~CameraImageCapturer() {
        delete capturer;
    }

    void capture() {
        *capturer >> *srcImage;
    }
};

int main(int argc, char** argv) {
    d3t12::cvMatPtr src(new cv::Mat);
    
    d3t12::ColorJSONLoader loader;
    loader.setFile("colors.json");
    loader.loadJSON();
    d3t12::ColorPalette::Ptr palette(new d3t12::ColorPalette);
    loader.fillPalette(*palette);

    d3t12::CubeDetectorFactory factory(palette);
    d3t12::CubeDetector::Ptr detector = factory.createCubeDetector(argv[1], src);

    d3t12::CameraPoseHandler::Ptr cameraPose(new d3t12::CameraPoseHandler);

    d3t12::ImageAngleAdjuster::Ptr angleAdjuster(new ConcreteAngleAdjuster(cameraPose));
    d3t12::CubeCenterTargeter targeter(
        d3t12::ImageCapturer::Ptr(new CameraImageCapturer(1, src)),
        detector,
        angleAdjuster
    );

    d3t12::ImageAngleGetter::Ptr angleGetter(new ConcreteAngleGetter(cameraPose));
    d3t12::CubePositionFinder finder(angleGetter, 0.30, 0.03, 0.02);

    d3t12::SignalFunctor::Ptr exitGuard(new d3t12::ExitGuard);
    d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);
    while(exitGuard->good()) {
        
        targeter.targetCenter();
        std::cout << std::endl << finder.findCubePosition() << std::endl;

        cv::rectangle(*src, cv::Rect(318,238,4,4), cv::Scalar(0,0,255));

        cv::imshow("image", *src);
        cv::waitKey(30);
    }

    std::cout << "bye" << std::endl;

    return(0);
}
