#include <iostream>
#include <vision/Color.h>

namespace d3t12 {

std::ostream& operator<<(std::ostream& os, Color color) {
    os << "color [ min: " << color.range.min << ", max: " << color.range.max << " ]";
    return os;
}

}