#include <stdexcept>

#include <common/Popener.h>

#define BUF_LEN 256

namespace d3t12 {

std::string Popener::popen(const std::string& cmd) const {
    FILE* pipe = ::popen(cmd.c_str(), "r");
    if (!pipe) throw std::runtime_error("popen : could not execute command");
    
    std::string result;
    char* buffer = (char*)calloc(BUF_LEN, sizeof(char));

    while(!feof(pipe))
        if(fgets(buffer, BUF_LEN, pipe) != NULL)
            result += buffer;
    pclose(pipe);
    free(buffer);

    return result;
}

}