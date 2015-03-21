__author__ = 'Antoine'
import re
from math import pow

from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchBetween(SearchInformation):

    def __setRegex(self, wantedInformation):
        self.listRegex = []
        if len(wantedInformation) > 2:
            return None
        if "." in wantedInformation[0]:
            elementLesser = float(wantedInformation[0])
            elementBigger = float(wantedInformation[1])
            numberOfDigit = len(wantedInformation[0].split(".")[1])
            floatIncrement = 1 * pow(10, -numberOfDigit)
            while elementLesser <= elementBigger:
                regex = '(\\b' + str(elementLesser) + '\\b)'
                self.listRegex.append(regex)
                elementLesser += floatIncrement
                print(elementLesser)
                elementLesser = float("{0:.2f}".format(elementLesser))

        else:
            elementLesser = int(wantedInformation[0])
            elementBigger = int(wantedInformation[1])
            while elementLesser <= elementBigger:
                regex = '(\\b' + str(elementLesser) + '\\b)'
                self.listRegex.append(regex)
                elementLesser += 1



    def findInformation(self, dictionary, keyword, wantedInformation):
        isContaining = False
        self.__setRegex(wantedInformation)
        print(self.listRegex)
        for possibleRegex in self.listRegex:
            expression = re.compile(possibleRegex)
            if keyword in dictionary:
                for value in dictionary[keyword]:
                    if expression.search(value) is not None:
                        isContaining = True
                        break
        return isContaining