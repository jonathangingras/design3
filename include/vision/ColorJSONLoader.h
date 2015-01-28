#ifndef _D3T12_COLORJSONLOADER_H_
#define _D3T12_COLORJSONLOADER_H_

#include <jansson.h>
#include <common/JanssonException.h>
#include <vision/Color.h>
#include <vision/ColorPalette.h>

namespace d3t12 {

class ColorJSONLoader {
protected:
    std::string filename;
    json_t *rootJSON;

private:
    void cleanLastRoot();
    Color createColor(json_t *colorRange);

public:
    inline ColorJSONLoader(): rootJSON(NULL) {}
    virtual ~ColorJSONLoader() {
        cleanLastRoot();
    }

    inline void setFile(std::string p_filename) {
        filename = p_filename;
    }

    void loadJSON();
    void fillPalette(ColorPalette& palette);
};

}

#endif