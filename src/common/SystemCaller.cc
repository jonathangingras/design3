#include <common/SystemCaller.h>

namespace d3t12 {

void SystemCaller::call(const std::string& command) {
	system(command.c_str());
}

}