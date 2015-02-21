__author__ = 'Antoine'
from naturalLanguagePython.SearchInformationStrategy.searchInformation import SearchInformation

class SearchEndsWith(SearchInformation):

    def setRegex(self, wantedInformation):
        self.regex = '(\\b[A-Z].*' + wantedInformation + '\b)'