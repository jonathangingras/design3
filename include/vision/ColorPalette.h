#ifndef _D3T12_COLORPALETTE_H_
#define _D3T12_COLORPALETTE_H_

#include <map>

#include <vision/Color.h>
#include <vision/BitmapFormatException.h>
#include <vision/BadColorStringException.h>

namespace d3t12 {

class ColorPalette {
protected:
    typedef std::map<std::string, Color>::const_iterator ConstColorMapIterator;
    typedef std::map<std::string, Color>::iterator ColorMapIterator;

    std::map<std::string, Color> colorMap;

private:
    Color _getColor(const char* p_colorStr);

public:
    inline ColorPalette() {}

    inline Color getColor(const char* p_colorStr) {
        return _getColor(p_colorStr);
    }
    inline Color getColor(const std::string& p_colorStr) {
        return _getColor(p_colorStr.c_str());
    }
    inline void storeColor(const char* colorName, Color color) {
        colorMap[colorName] = color;
    }
};

}

#endif