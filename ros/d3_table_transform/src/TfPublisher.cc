#include <TfPublisher.h>

namespace d3t12 {

void TfPublisher::publishTfInLoop(double rate, d3t12::SignalFunctor::Ptr condition) {
	ros::Rate r(rate);
	while(condition->good()) { publishTf(); r.sleep(); }
}

void TfPublisher::publishTf() {
	tf::Transform tf;
	tf.setOrigin(translation);
	tf.setRotation(rotation);
	broadcaster.sendTransform(tf::StampedTransform(tf, ros::Time::now(), parentTf, childTf));
}

}