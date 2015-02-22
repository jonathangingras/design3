#include <common/SIGINTHandler.h>

namespace d3t12 {

SIGINTHandler* SIGINTHandler::self = NULL;
SignalFunctor::Ptr SIGINTHandler::handler;

void SIGINTHandler::handleSignal(int signal) {
	(*handler)();
}
void SIGINTHandler::catchSignal() {
	signal(SIGINT, handleSignal);
}
SIGINTHandler& SIGINTHandler::getInstance() {
	return ( self ? *self : *((self = new SIGINTHandler)) );
}
SIGINTHandler::~SIGINTHandler() {
	delete self;
}
void SIGINTHandler::setSignalHandler(SignalFunctor::Ptr _handler) {
	handler = _handler;
	catchSignal();
}

}