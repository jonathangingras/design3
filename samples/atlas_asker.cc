#include <string>
#include <iostream>

#include <rest/CURLGetter.h>
#include <rest/AtlasJSONDecoder.h>

#include <unistd.h>

int main(int argc, char **argv) {
	d3t12::CURLGetter getter("https://132.203.14.228");
  d3t12::AtlasJSONDecoder decoder;

  while(1) {
    sleep(1);
    std::string atlas_told = getter.performGET();
    std::cout << decoder.questionStr(atlas_told) << std::endl;
  }

	return 0;
}