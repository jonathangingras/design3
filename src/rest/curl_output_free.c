#include <rest/curl_output.h>

void curl_output_free(curl_output* output) {
  free(output->memory);
  free(output);
}