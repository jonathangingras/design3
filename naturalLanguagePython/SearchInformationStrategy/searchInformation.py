__author__ = 'Antoine'
import abc
import re
class SearchInformation(object):

    __metaclass__ = abc.ABCMeta
    def __setRegex(self, wantedInformation):
        self.regex = wantedInformation


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