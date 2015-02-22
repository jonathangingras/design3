#include <rest/AtlasJSONDecoder.h>

namespace d3t12 {

AtlasJSONDecoder::~AtlasJSONDecoder() {
	json_decref(rootJSON);
  json_decref(question);
}

void AtlasJSONDecoder::resolveRootJSON(const char* output_str) {
	rootJSON = json_loads(output_str, 0, &json_error);
  if(!rootJSON) {
    throw JanssonException(json_error.text);
  }
}

void AtlasJSONDecoder::resolveQuestion() {
	question = json_object_get(rootJSON, "question");
  if(!question) {
    throw JanssonException("\"question\" field was not resolved!");
  }
}

std::string AtlasJSONDecoder::_questionStr(const char* jsonStr) {
	resolveRootJSON(jsonStr);
	resolveQuestion();

  std::string questionStr = json_string_value(question);

  if(questionStr.empty()) {
    throw JanssonException("\"question\" field is empty!");
  }

	return questionStr;
}

}