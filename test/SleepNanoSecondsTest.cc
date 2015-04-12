#include <testEssentials.h>
#include <common/common.h>

TEST(SleepNanoSecconds, waitsGoodAmountOfTime) {
	d3t12::sleepSecondsNanoSeconds(5, 999999999);
}

TEST(SleepNanoSecconds, waitsGoodAmountOfTime2) {
	d3t12::sleepSecondsNanoSeconds(5, 0);
}