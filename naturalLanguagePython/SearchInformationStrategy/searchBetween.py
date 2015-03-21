__author__ = 'Antoine'
import re
from decimal import Decimal
from math import pow
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchBetween(SearchInformation):

    def __constructDecimalRegexList(self, wantedInformation):
        elementLesser = Decimal(wantedInformation[0])
        elementBigger = Decimal(wantedInformation[1])
        numberOfDigit = len(wantedInformation[0].split(".")[1])
        decimalIncrement = Decimal(str(1 * pow(10, -numberOfDigit)))
        while elementLesser <= elementBigger:
            regex = '(\\b' + str(elementLesser) + '\\b)'
            self.listRegex.append(regex)
            elementLesser += decimalIncrement

    def __setRegex(self, wantedInformation):
        self.listRegex = []
        if len(wantedInformation) > 2:
            return None
        if "." in wantedInformation[0]:
            self.__constructDecimalRegexList(wantedInformation)
        else:
            elementLesser = int(wantedInformation[0])
            elementBigger = int(wantedInformation[1])
            while elementLesser <= elementBigger:
                regex = '(\\b' + str(elementLesser) + '\\b)'
                self.listRegex.append(regex)
                elementLesser += 1


    def __replaceSlash(self, regex):
        return regex.replace(".", "\.")

    def findInformation(self, dictionary, keyword, wantedInformation):
        isContaining = False
        wordRemovedFromWantedInformation = []
        self.__setRegex(wantedInformation)
        for possibleRegex in self.listRegex:
            possibleRegex = self.__replaceSlash(possibleRegex)
            expression = re.compile(possibleRegex)
            if keyword in dictionary:
                for value in dictionary[keyword]:
                    if expression.search(value) is not None:
                        isContaining = True
                        break
        return isContaining