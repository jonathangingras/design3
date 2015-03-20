__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
import re


class SearchContains(SearchInformation):

    def __verifyBeginningOfWantedInformation(self, wantedInformation):
        beginningInformation = ""
        if wantedInformation[0].isalnum():
            beginningInformation = "(\\b"
        else:
            beginningInformation = "(\\B"
        return beginningInformation

    def __verifyEndingOfWantedInformation(self, wantedInformation):
        endingInformation = ""
        if wantedInformation[len(wantedInformation)-1].isalnum():
            endingInformation = "\\b)"
        else:
            endingInformation = "\\B)"
        return endingInformation

    def __setRegex(self, wantedInformation):
        wantedInformation = wantedInformation.replace(".", "\.")
        beginningInformation = self.__verifyBeginningOfWantedInformation(wantedInformation)
        endingInformation = self.__verifyEndingOfWantedInformation(wantedInformation)
        self.regex = beginningInformation + wantedInformation + endingInformation

    def findInformation(self, dictionary, keyword, wantedInformation):
        isContaining = False
        self.__setRegex(wantedInformation)
        expression = re.compile(self.regex)
        if dictionary.has_key(keyword):
            for value in dictionary[keyword]:
                if expression.search(value) is not None:
                    isContaining = True
                    break
        return isContaining