#ifndef _D3T12_COUNTRYTOCOLORLISTER_H_
#define _D3T12_COUNTRYTOCOLORLISTER_H_

#include "common.h"
#include <jansson.h>

namespace d3t12 {

class CountryToColorLister {
private:
	std::string flagsJSON;
public:
	CountryToColorLister(std::string _flagsJSON): flagsJSON(_flagsJSON) {}

	inline std::vector<StringPtr> getColorList(std::string countryName) {
		json_error_t error;
		json_t* root = json_load_file(flagsJSON.c_str(), 0, &error);
		json_t* countries = json_object_get(root, "countries");
		std::vector<StringPtr> colors;
		size_t countryIndex;
		json_t* countryValue;
		json_array_foreach(countries, countryIndex, countryValue) {
			if(json_string_value(json_object_get(countryValue, "name")) == countryName) {
				size_t colorIndex;
				json_t* colorValue;
				json_t* colorArray = json_object_get(countryValue, "color_list");
				json_array_foreach(colorArray, colorIndex, colorValue) {
					if(json_is_null(colorValue)) {
						colors.push_back(StringPtr(new std::string("")));
					} else {
						colors.push_back( StringPtr(new std::string(json_string_value(colorValue))) );
					}
				}
			}
		}
		json_decref(root);
		return colors;
	}
};

} //d3t12

#endif