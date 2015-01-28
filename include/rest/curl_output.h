#ifndef _D3T12_CURLOUTPUT_H_
#define _D3T12_CURLOUTPUT_H_

#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

#ifdef __cplusplus
extern "C" {
#endif

#ifdef __GNUC__
#define restrict __restrict__
#else
#define restrict
#endif

typedef struct {
  char* memory;
  size_t allocation_length;
  size_t size;
} curl_output;

curl_output* curl_output_init();
void curl_output_free(curl_output* output);
size_t curl_output_write_data_overwrite(char* restrict buffer, size_t size, size_t nmemb, void* restrict userp);

#ifdef __cplusplus
}
#endif

#endif