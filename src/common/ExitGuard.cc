#include <common/ExitGuard.h>

namespace d3t12 {

void ExitGuard::operator()() {
	done = true;
}

bool ExitGuard::good() {
	return !done;
}

}