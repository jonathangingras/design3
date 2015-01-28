#include <rest/curl_output.h>

curl_output* curl_output_init() {
  curl_output* output = (curl_output*)malloc(sizeof(curl_output));
  output->memory = (char*)malloc(256*sizeof(char));
  output->allocation_length = 256;
  output->size = 0;
  return output;
}