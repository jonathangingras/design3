#include <rest/CURLGetter.h>

namespace d3t12 {

CURLGetter::CURLGetter(const char* p_url) : url(p_url)  {
	initialize();
}

CURLGetter::CURLGetter(std::string p_url) : url(p_url)  {
	initialize();
}

CURLGetter::~CURLGetter() {
	curl_output_free(output);
  curl_free(handle);
}

void CURLGetter::initialize() {
	//curl handle
	handle = curl_easy_init();
	//curl output structure (DTO)
  output = curl_output_init();

  curl_easy_setopt(handle, CURLOPT_URL, url.c_str());
	//set fuction to call at perform time
  curl_easy_setopt(handle, CURLOPT_WRITEFUNCTION, &curl_output_write_data_overwrite);
	//set pointer for string output
  curl_easy_setopt(handle, CURLOPT_WRITEDATA, (void *)output);
  //set options because server has its own certificate
  curl_easy_setopt(handle, CURLOPT_SSL_VERIFYPEER, 0);
  curl_easy_setopt(handle, CURLOPT_SSL_VERIFYHOST, 0);
}

void CURLGetter::_setURL(const char* p_url) {
	url = p_url;
	curl_easy_setopt(handle, CURLOPT_URL, url.c_str());
}

std::string CURLGetter::performGET() {
	CURLcode code;
  if((code = curl_easy_perform(handle)) != CURLE_OK) {
    throw CURLException(std::string(curl_easy_strerror(code)));
  }

  return std::string(output->memory);
}

}