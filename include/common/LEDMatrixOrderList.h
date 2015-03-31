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

	inline int next() {
		++currentIndex;
		if(currentIndex == 9) {
			currentIndex = 0;
		}
		return indices[currentIndex];
	}

	inline int cancelCurrent() {
		--currentIndex;
		if(currentIndex < 0) {
			currentIndex = 0;
		}
		return indices[currentIndex];
	}

	inline void increase() {
		++currentIndex;
	}

	inline int current() {
		if(currentIndex < 0) currentIndex = 0;
		return indices[currentIndex];
	}

	inline LEDMatrixOrderList(): currentIndex(-1) {
		indices[0] = 6;
		indices[1] = 7;
		indices[2] = 8;
		indices[3] = 3;
		indices[4] = 4;
		indices[5] = 5;
		indices[6] = 0;
		indices[7] = 1;
		indices[8] = 2;
	}
};

class LEDColorList {
private:
	LEDMatrixOrderList::Ptr orderList;
	std::vector<StringPtr> colors;
	StringPtr nullStr;

public:
	typedef boost::shared_ptr<LEDColorList> Ptr;

	inline LEDColorList(LEDMatrixOrderList::Ptr _orderList): orderList(_orderList), nullStr(new std::string("")) {}

	inline void setColorList(std::vector<StringPtr>& _colors) {
		for(int i = 0; i < _colors.size(); ++i) {
			colors.push_back(_colors[i]);
		}
	}

	inline void increase() {
		orderList->increase();
	}

	inline StringPtr current() const {
		return (colors.size() == 9 ? colors[orderList->current()] : nullStr);
	}

	inline StringPtr next() {
		return (colors.size() == 9 ? colors[orderList->next()] : nullStr);
	}
};

}

#endif