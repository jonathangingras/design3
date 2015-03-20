__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
import re


class SearchContains(SearchInformation):

    def __setRegex(self, wantedInformation):
        self.regex = '(\\b' + wantedInformation + '\\b)'

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