#ifndef _D3T12_COLORPALETTEMOCK_H_
#define _D3T12_COLORPALETTEMOCK_H_

class ColorPaletteMock : public d3t12::ColorPalette {
public:
  MOCK_METHOD2(storeColor, void(const char* colorName, d3t12::Color color));
};

#endif