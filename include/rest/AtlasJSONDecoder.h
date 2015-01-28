#ifndef _D3T12_ATLASJSONDECODER_H_
#define _D3T12_ATLASJSONDECODER_H_

#include <string>
#include <jansson.h>
#include <common/JanssonException.h>

namespace d3t12 {

class AtlasJSONDecoder {
  json_t *rootJSON;
  json_t *question;
  json_error_t json_error;

  void resolveRootJSON(const char*);
  void resolveQuestion();

  std::string _questionStr(const char* jsonStr);

public:
	inline AtlasJSONDecoder(): rootJSON(NULL), question(NULL) {}
	~AtlasJSONDecoder();

	inline std::string questionStr(std::string jsonStr) {
		return _questionStr(jsonStr.c_str());
	}
	inline std::string questionStr(const char* jsonStr) {
		return _questionStr(jsonStr);
	}
};

}

#endif