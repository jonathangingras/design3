#include <rest/curl_output.h>

size_t curl_output_write_data_overwrite(char* restrict buffer, size_t size, size_t nmemb, void* restrict userp) {
	size_t input_size = size * nmemb;

	curl_output* output = (curl_output*)userp;
	
	if(input_size + 1 > output->allocation_length){
    output->memory = (char*)realloc(output->memory, input_size + 1);
    if(!output->memory) {
      return 0;
    }
    output->allocation_length = input_size + 1;
  }
	
  output->size = input_size;

  memset(output->memory, 0, output->allocation_length);
  memcpy(output->memory, buffer, input_size);

  return input_size;
}