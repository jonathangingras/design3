#include <vision/ColorJSONLoader.h>

namespace d3t12 {

void ColorJSONLoader::cleanLastRoot() {
    if(rootJSON) {
        json_decref(rootJSON);
    }
}

Color ColorJSONLoader::createColor(json_t *colorRange) {
    int ints[6];
    size_t i;
    json_t* range;

    json_array_foreach(colorRange, i, range) {
        ints[i] = (int)json_integer_value(range);
    }
    
    return Color((Color::Range){cv::Scalar(ints[0],ints[1],ints[2]), cv::Scalar(ints[3], ints[4], ints[5])});
}

void ColorJSONLoader::loadJSON() {
    cleanLastRoot();
    json_error_t json_error;
    rootJSON = json_load_file(filename.c_str(), JSON_DECODE_ANY, &json_error);
    if(!rootJSON) {
        json_decref(rootJSON);
        rootJSON = NULL;
        throw JanssonException(json_error.text);
    }

    if(!json_is_array(json_object_get(rootJSON, "colors"))) {
        throw JanssonException("no \"colors\" field in JSON, or value not an array!");
    }
}

void ColorJSONLoader::fillPalette(ColorPalette& palette) {
    json_t *colorSet;
    colorSet = json_object_get(rootJSON, "colors");

    size_t colorIndex;
    json_t *color;
    json_array_foreach(colorSet, colorIndex, color) {
        json_t *colorName = json_object_get(color, "name");
        json_t *colorRange = json_object_get(color, "range");

        if(!colorRange || !colorName) {
            throw JanssonException("Color needs \"name\" and \"range\"");
        }

        palette.storeColor(json_string_value(colorName), createColor(colorRange));
    }
}

}