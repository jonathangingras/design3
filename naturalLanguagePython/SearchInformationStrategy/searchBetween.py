__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchBetween(SearchInformation):

    def __setRegex(self, wantedInformation):
        self.listRegex = []
        for element in wantedInformation:
            print(element)

    def findInformation(self, dictionary, keyword, wantedInformation):
        isContaining = False

        return isContaining