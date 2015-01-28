#ifndef _D3T12_CURLGETTER_H_
#define _D3T12_CURLGETTER_H_

#include <string>
#include <curl/curl.h>
#include "curl_output.h"
#include "CURLException.h"

namespace d3t12 {

class CURLGetter {
	std::string url;
	CURL* handle;
	curl_output* output;

	void initialize();
	void _setURL(const char* p_url);

public:
	CURLGetter(const char* p_url);
	CURLGetter(std::string p_url);

	~CURLGetter();

	inline void setURL(const char* p_url) {
		_setURL(p_url);
	}
	inline void setURL(std::string p_url) {
		_setURL(p_url.c_str());
	}

	std::string performGET();
};

}

#endif