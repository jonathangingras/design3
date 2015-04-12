#include <testEssentials.h>
#include <common/NonBlockIfStream.h>
#include <fstream>

using namespace d3t12;

TEST(NonBlockIfStream, readsGoodBytes) {
	NonBlockIfStream nbifstream("./outputCat");

	std::string outputString, outputString2;

	nbifstream >> outputString;
	std::cout << outputString;

	std::cout << "second shot" << std::endl;

	nbifstream >> outputString2;
	std::cout << outputString2;
}

TEST(NonBlockIfStream, readsGoodBytesWhenStopped) {
	NonBlockIfStream nbifstream("./outputCat");

	std::string outputString1, outputString2;

	nbifstream >> outputString1;
	std::cout << outputString1;

	std::cout << "going to sleep" << std::endl;
	sleep(1);
	
	nbifstream >> outputString2;

	std::cout << outputString2;
}

TEST(NonBlockIfStream, ifstreamEquivalent) {
	std::ifstream ifstream("./outputCat");

	std::string outputString1, outputString2;

	ifstream >> outputString1;
	std::cout << outputString1;

	std::cout << "going to sleep" << std::endl;
	sleep(1);
	
	ifstream >> outputString2;

	std::cout << outputString2;
}