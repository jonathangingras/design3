#include <common/common.h>
#include <vision/vision.h>
#include <driver/driver.h>

class AngleAdjuster : public d3t12::ImageAngleAdjuster {
private:
    d3t12::CameraPoseHandler cameraPose;

    inline int rad2deg(double rad) {
        return (rad*180)/M_PI;
    }

    inline double deg2rad(int deg) {
        return (deg*M_PI)/180;
    }

public:
    inline AngleAdjuster() {}

    void adjustY(int degrees) {
        cameraPose.increasePitch(deg2rad(degrees));
    }

    void adjustX(int degrees) {
        cameraPose.increaseYaw(deg2rad(degrees));
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

    d3t12::CubeCenterTargeter targeter(
        d3t12::ImageCapturer::Ptr(new CameraImageCapturer(1, src)),
        detector,
        d3t12::ImageAngleAdjuster::Ptr(new AngleAdjuster)
    );

    d3t12::SignalFunctor::Ptr exitGuard(new d3t12::ExitGuard);
    d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);
    while(exitGuard->good()) {
        
        targeter.targetCenter();

        cv::imshow("image", *src);
        cv::waitKey(30);
    }

    std::cout << "bye" << std::endl;

    return(0);
}
