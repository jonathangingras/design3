#include <vision/ColorPalette.h>

namespace d3t12 {

Color ColorPalette::_getColor(const char* p_colorStr) {
    ConstColorMapIterator iterator = colorMap.find(p_colorStr);

    if(iterator == colorMap.end()) {
        throw BadColorStringException("ColorPalette::getColor: Unknown Color String");
    }

    return iterator->second;
}

}