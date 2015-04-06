#ifndef _D3T12_CUBECENTERTARGETER_H_
#define _D3T12_CUBECENTERTARGETER_H_

#include <vision/visionEssentials.h>
#include <vision/ImageCapturer.h>
#include <vision/ImageAngleAdjuster.h>
#include <vision/CubeDetector.h>

namespace d3t12 {

class CubeCenterTargeter {
protected:
	CubeDetector::Ptr detector;
	ImageAngleAdjuster::Ptr adjuster;
	ImageCapturer::Ptr capturer;

private:
	void macroAdjust(const cv::Point& center, const cv::Rect& rect);
	void microAdjust(const cv::Point& center, const cv::Rect& rect);
	bool needMicroAdjust(const cv::Point& imageCenter, const cv::Rect& rect);

public:
	typedef boost::shared_ptr<CubeCenterTargeter> Ptr;
	inline CubeCenterTargeter(ImageCapturer::Ptr _capturer, CubeDetector::Ptr _detector, ImageAngleAdjuster::Ptr _adjuster):
		capturer(_capturer), detector(_detector), adjuster(_adjuster) {}

	inline CubeCenterTargeter(ImageCapturer::Ptr _capturer, ImageAngleAdjuster::Ptr _adjuster):
		capturer(_capturer), adjuster(_adjuster) {}

	inline void setDetector(CubeDetector::Ptr _detector) {
		detector = _detector;
	}

	virtual void resetAngle();
	virtual void targetCenter();
};

}

#endif