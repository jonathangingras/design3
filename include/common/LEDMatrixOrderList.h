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
		if(currentIndex < -1) {
			currentIndex = -1;
		}
	}

	inline void increase() {
		++currentIndex;
		if(currentIndex == 9) {
			currentIndex = 0;
		}
	}

	inline int next() {
		increase();
		return indices[currentIndex];
	}

	inline int current() {
		if(currentIndex < 0) currentIndex = 0;
		if(currentIndex > 8) currentIndex = 8;
		return indices[currentIndex];
	}

	inline LEDMatrixOrderList(): currentIndex(-1) {
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
		return (colors.size() == 9 ? colors[orderList->current() - 1] : nullStr);
	}

	inline StringPtr next() {
		return (colors.size() == 9 ? colors[orderList->next() - 1] : nullStr);
	}
};

}

#endif