#ifndef _D3T12_TFPUBLISHER_H_
#define _D3T12_TFPUBLISHER_H_

#include <string>
#include <common/common.h>
#include <tf/transform_broadcaster.h>

namespace d3t12 {

class TfPublisher {
protected:
	std::string parentTf;
	std::string childTf;
	tf::Vector3 translation;
	tf::Quaternion rotation;
	tf::TransformBroadcaster broadcaster;

public:
	inline TfPublisher(std::string _parentTf, std::string _childTf, tf::Vector3 _translation, tf::Quaternion _rotation):
	parentTf(_parentTf), childTf(_childTf), translation(_translation), rotation(_rotation) {}

	inline void setRotation(tf::Quaternion _rotation) {
		rotation = _rotation;
	}

	inline void setTranslation(tf::Vector3 _translation) {
		translation = _translation;
	}

	void publishTf();

	void publishTfInLoop(double rate, d3t12::SignalFunctor::Ptr condition);
};

inline tf::Quaternion quaternionFromRPY(double r, double p, double y) {
	tf::Quaternion q;
	q.setRPY(r, p, y);
	return q;
}

}

#endif