#include <opencv2/opencv.hpp>
#include <boost/regex.hpp>
#include <boost/filesystem/operations.hpp>
#include <boost/filesystem/path.hpp>
#include <decode_gif.h>
#include <jansson.h>

extern "C" typedef struct pixel_t {
	unsigned char b0, b1, b2, b3;
} pixel_t;

uint8_t getAlphaByteAt(cv::Mat& mat, int x, int y) {
	return mat.at<pixel_t>(y, x).b3;
}

cv::Scalar getColorAt(cv::Mat& mat, int x, int y) {
	pixel_t pixel = mat.at<pixel_t>(y, x);
	return cv::Scalar(pixel.b0, pixel.b1, pixel.b2);
}

std::string getColorStringAt(cv::Mat& mat, int x, int y) {
	cv::Scalar color = getColorAt(mat, x, y);

	if(color == cv::Scalar(0,0,0)) {
		return "black";
	}
	if(color == cv::Scalar(0,0,255)) {
		return "red";
	}
	if(color == cv::Scalar(255,0,0)) {
		return "blue";
	}
	if(color == cv::Scalar(0,209,0)) {
		return "green";
	}
	if(color == cv::Scalar(0,255,255)) {
		return "yellow";
	}
	if(color == cv::Scalar(255,255,255)) {
		return "white";
	}

	return "";
}

std::string getPixelColorStr(cv::Mat& mat, int x, int y) {
	if(getAlphaByteAt(mat, x, y)) {
		return getColorStringAt(mat, x, y);
	} else {
		return "(null)";
	}
}

struct FlagCubePixelList {
	int cubes[9][2];

	FlagCubePixelList() {
		cubes[0][0] = 16; cubes[0][1] = 16;
		cubes[1][0] = 49; cubes[1][1] = 16;
		cubes[2][0] = 82; cubes[2][1] = 16;
		
		cubes[3][0] = 16; cubes[3][1] = 49;
		cubes[4][0] = 49; cubes[4][1] = 49;
		cubes[5][0] = 82; cubes[5][1] = 49;
		
		cubes[6][0] = 16; cubes[6][1] = 82;
		cubes[7][0] = 49; cubes[7][1] = 82;
		cubes[8][0] = 82; cubes[8][1] = 82;
	}
};

struct Country {
	std::string filename;
	std::string name;

	inline Country(std::string _filename, std::string _name):
	filename(_filename), name(_name) {}
};

void addCountry(json_t* countryArray, Country country) {
	GIF* gif = gif_new();
	gif_load_file(gif, country.filename.c_str());

	cv::Mat mat(gif->animation.width, gif->animation.height, CV_8UC4);
	
	for(int i = 0; i < gif->animation.frame_count; ++i) {
		mat.data = gif_get_frame(gif, i);
		cv::cvtColor(mat, mat, CV_RGBA2BGRA);
	}

	FlagCubePixelList pixelList;
	json_t* countryObject = json_object();
	json_object_set_new(countryObject, "file", json_string(country.filename.c_str()));
	json_object_set_new(countryObject, "name", json_string(country.name.c_str()));

	json_t* colorArrayObject = json_array();
	for(int i = 0; i < 9; ++i) {
		json_t* colorObject;
		std::string colorStr = getPixelColorStr(mat, pixelList.cubes[i][0], pixelList.cubes[i][1]);

		if(colorStr == "(null)") {
			colorObject = json_null();
		} else {
			colorObject = json_string(colorStr.c_str());
		}

		json_array_append_new(colorArrayObject, colorObject);
	}

	json_object_set_new(countryObject, "color_list", colorArrayObject);
	json_array_append_new(countryArray, countryObject);

	gif_free(gif);
}

namespace fs = boost::filesystem;
void findCountries(const char* directory, std::vector<Country>& countries) {
	if(!fs::is_directory(directory)) return;

	fs::directory_iterator end_iter;

	for(fs::directory_iterator dir_itr(directory); dir_itr != end_iter; ++dir_itr) {		
		boost::regex fileRegEx(".*/(.*)\\.gif");
		boost::smatch what;

		std::string filename = dir_itr->path().string();

		if(boost::regex_search(filename, what, fileRegEx, boost::match_extra)) {
			countries.push_back(
				Country(filename, std::string(what[1].first, what[1].second) )
			);
		}
	}
}

int main(int argc, char** argv) {
	if(argc < 3) {
		std::cout << "Usage: " << argv[0] << " inputDirectoryWhereGIFSAre " << "outputJSONFilename" << std::endl;
		return 1;
	}

	json_t* root = json_object();
	json_object_set_new(root, "countries", json_array());

	std::vector<Country> countries;
	findCountries(argv[1], countries);

	int nbCountries = 0;
	json_t* countryArray = json_object_get(root, "countries");
	for(std::vector<Country>::const_iterator it = countries.begin(); it != countries.end(); ++it) {
		addCountry(countryArray, *it);
		++nbCountries;
	}
	std::cout << "found " << nbCountries << " countries" << std::endl;

	json_dump_file(root, argv[2], JSON_INDENT(2));
}