#include <gtest/gtest.h>
#include <rest/AtlasJSONDecoder.h>

using namespace d3t12;

TEST(AtlasJSONDecoder, throwsWhenJSONEmpty) {
	AtlasJSONDecoder decoder;

	EXPECT_THROW(decoder.questionStr("{}"), JanssonException);
}

TEST(AtlasJSONDecoder, throwsWhenJSONInvalid) {
	AtlasJSONDecoder decoder;

	EXPECT_THROW(decoder.questionStr("{\"dse: 78}"), JanssonException);
}

TEST(AtlasJSONDecoder, throwsWhenJSONHasNoFieldQuestion) {
	AtlasJSONDecoder decoder;

	EXPECT_THROW(decoder.questionStr("{\"dse\": 78}"), JanssonException);
}

TEST(AtlasJSONDecoder, throwsWhenQuestionEmpty) {
	AtlasJSONDecoder decoder;

	EXPECT_THROW(decoder.questionStr("{\"question\": \"\"}"), JanssonException);
}

TEST(AtlasJSONDecoder, noThrowWhenQuestionPresent) {
	AtlasJSONDecoder decoder;

	EXPECT_NO_THROW(decoder.questionStr("{\"question\": \"Nice shoes, wanna f**k?\"}"));
}

TEST(AtlasJSONDecoder, questionStrIsAccurateWhenQuestionPresent) {
	AtlasJSONDecoder decoder;

	std::string expectedStr = "Nice shoes, wanna f**k?";
	EXPECT_EQ(expectedStr, decoder.questionStr("{\"question\": \"Nice shoes, wanna f**k?\"}"));
}