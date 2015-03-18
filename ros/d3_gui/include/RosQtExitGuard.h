#ifndef _ROSQTEXITGUARD_H_
#define _ROSQTEXITGUARD_H_

#include <ros/ros.h>
#include <common/SIGINTHandler.h>
#include <QtGui/QApplication>

namespace d3t12 {

struct RosQtExitGuard : public d3t12::SignalFunctor {
	::ros::NodeHandle& nodeHandle;
	QApplication* qtApp;
	
	inline RosQtExitGuard(::ros::NodeHandle& _nodeHandle, QApplication* _qtApp):
	nodeHandle(_nodeHandle), qtApp(_qtApp) {}

	virtual void operator()();
	virtual bool good();
};

}

#endif