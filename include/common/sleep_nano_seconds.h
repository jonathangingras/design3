#ifndef _D3T12_SLEEP_NANO_SECONDS_H_
#define _D3T12_SLEEP_NANO_SECONDS_H_

#include <errno.h>
#include <time.h>
#include <stdio.h>
#include <string.h>

namespace d3t12 {

inline void sleepSecondsNanoSeconds(time_t secs, long nanoSecs) {
	struct timespec delay = {secs, nanoSecs};
	int done = 1;
	while(done) {
		struct timespec remaining;
		done = nanosleep(&delay, &remaining);
		delay = remaining;

		if(errno != 0 && errno != EINTR) {
			fprintf(stderr, "error when sleeping: %s\n", strerror(errno));
			break;
		}
	}
}

}

#endif