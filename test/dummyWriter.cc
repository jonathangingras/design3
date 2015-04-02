#include <fstream>
#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
	//std::ofstream out("./outputCat");
	int out = open("./outputCat", O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);

	for(int i = 0; i < 100; ++i) {
		dprintf(out, "hello %i\n", i);
		//out << "hello " << i << '\n';
		//out.flush();
		usleep(100000);
	}

	close(out);
}