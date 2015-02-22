#ifndef _D3T12_CUBEDETECTORTESTER_H_
#define _D3T12_CUBEDETECTORTESTER_H_

namespace d3t12 {

class CubeDetectorTester {
private:
	ColorPalette::Ptr palette;
	cvMatPtr image;
	std::string colorString;

	ColorPalette::Ptr setupPalette() {
		ColorPalette::Ptr palette(new ColorPalette);
		ColorJSONLoader loader;
		loader.setFile("../config/colors.json");
		loader.loadJSON();
		loader.fillPalette(*palette);
		return palette;
	}

public:
	inline CubeDetectorTester() : palette(setupPalette()) {}

	void setImageFromFile(std::string imageFile) {
		image = cvMatPtr(new cv::Mat(cv::imread(imageFile)));
	}

	cv::Rect detectColor(std::string _colorString) {
		colorString = _colorString;
		CubeDetector::Ptr detector = CubeDetectorFactory(palette).createCubeDetector(colorString, image);
		return detector->detectCube();
	}
	
	void showImage(cv::Rect rect) {
		cv::rectangle(*image, rect, cv::Scalar(0,0,255));
		cv::imshow(colorString, *image);
		cv::waitKey(1000);
	}
};

}

#endif