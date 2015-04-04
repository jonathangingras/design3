#ifndef _D3T12_AI_POSEGETTER_H_
#define _D3T12_AI_POSEGETTER_H_

#include <common/commonEssentials.h>
#include "RobotPose.h"
#include "PathPlanner.h"

namespace d3t12 {

struct PoseGetter {
	typedef boost::shared_ptr<PoseGetter> Ptr;
	virtual ~PoseGetter() {}
	virtual RobotPose getPose() = 0;
};

struct PoseCommander {
	typedef boost::shared_ptr<PoseCommander> Ptr;
	virtual ~PoseCommander() {}
	virtual void commandDirectly(RobotPose pose) = 0;
	virtual void commandPose(RobotPose pose) = 0;
};

struct QuestionGetter {
	typedef boost::shared_ptr<QuestionGetter> Ptr;
	virtual ~QuestionGetter() {}
	virtual std::string getQuestion() = 0;
};

struct QuestionAsker {
	typedef boost::shared_ptr<QuestionAsker> Ptr;
	virtual ~QuestionAsker() {}
	virtual std::string ask(std::string question) = 0;
};

struct ConfirmationGetter {
	typedef boost::shared_ptr<ConfirmationGetter> Ptr;
	virtual ~ConfirmationGetter() {}
	virtual bool ok() = 0;
};

struct PathInformer {
	typedef boost::shared_ptr<PathInformer> Ptr;
	virtual ~PathInformer() {}
	virtual void informPath(const std::vector<PathCommand>& path) = 0;
};

} //d3t12

#endif