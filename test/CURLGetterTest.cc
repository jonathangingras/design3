#include <rest/CURLGetter.h>
#include "testEssentials.h"

using namespace d3t12;

#define INVALID_URL "nosuchurl"
#define VALID_URL1 "google.com"
#define VALID_URL2 "http://echo.jsontest.com/question/hey"
#define VALID_URL_WILL_TIMEOUT "10.255.255.1"

TEST(CURLGetter, throwsWhenURLInvalid) {
	CURLGetter getter(INVALID_URL);

	EXPECT_THROW(getter.performGET(), CURLException);
}

TEST(CURLGetter, requestNotEmptyWhenValid) {
	CURLGetter getter(VALID_URL1);

	std::string gottenString = getter.performGET();

	EXPECT_FALSE(gottenString.empty());
}

TEST(CURLGetter, settingURLIsEffective) {
	CURLGetter getter(VALID_URL1);

	std::string gottenString1 = getter.performGET();
	std::string gottenString2 = getter.performGET();

	EXPECT_NE(gottenString1, gottenString2);
}

//This one takes about 2 mins
TEST(CURLGetter, throwsWhenTimeout) {
	CURLGetter getter(VALID_URL_WILL_TIMEOUT);

	EXPECT_THROW(getter.performGET(), CURLException);
}