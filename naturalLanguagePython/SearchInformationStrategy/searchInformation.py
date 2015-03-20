__author__ = 'Antoine'
import abc
import re


class SearchInformation(object):

    def __setRegex(self, wantedInformation):
        self.regex = wantedInformation

    @abc.abstractmethod
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

    @abc.abstractmethod
    def findInformationList(self, dictionary, keyword, wantedListInformation):
        isContaining = False
        numberOfInformationFound = 0
        for wantedInformation in wantedListInformation:
            isContainingInformation = self.findInformation(dictionary, keyword, wantedInformation)
            if isContainingInformation is True:
                numberOfInformationFound += 1
        if numberOfInformationFound == len(wantedListInformation):
            isContaining = True
        return isContaining
