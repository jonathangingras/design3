#ifndef _D3T12_LEDMATRIXORDERLIST_H_
#define _D3T12_LEDMATRIXORDERLIST_H_

#include <vector>
#include "common.h"

namespace d3t12 {

class LEDMatrixOrderList {
private:
	int indices[9];
	int currentIndex;

public:
	typedef boost::shared_ptr<LEDMatrixOrderList> Ptr;

	inline void cancelCurrent() {
		--currentIndex;
		if(currentIndex < 0) {
			currentIndex = 8;
		}
	}

	inline void increase() {
		++currentIndex;
		if(currentIndex > 8) {
			currentIndex = 0;
		}
	}

	inline int current() {
		if(currentIndex < 0) currentIndex = 0;
		if(currentIndex > 8) currentIndex = 8;
		return indices[currentIndex];
	}

	inline LEDMatrixOrderList(): currentIndex(0) {
		indices[0] = 7;
		indices[1] = 8;
		indices[2] = 9;
		indices[3] = 4;
		indices[4] = 5;
		indices[5] = 6;
		indices[6] = 1;
		indices[7] = 2;
		indices[8] = 3;
	}
};

template <typename Type>
class CubeList {
private:
	LEDMatrixOrderList::Ptr orderList;
	std::vector<Type> elements;
	Type nullElement;

public:
	typedef boost::shared_ptr<CubeList> Ptr;

	inline CubeList(LEDMatrixOrderList::Ptr _orderList): orderList(_orderList) {}

	inline void setColorList(std::vector<Type>& _elements) {
		for(int i = 0; i < _elements.size(); ++i) {
			elements.push_back(_elements[i]);
		}
	}

	inline void increase() {
		orderList->increase();
	}

	inline Type current() const {
		return (elements.size() == 9 ? elements[orderList->current() - 1] : nullElement);
	}
};

typedef CubeList<StringPtr> LEDColorList;

}

#endif