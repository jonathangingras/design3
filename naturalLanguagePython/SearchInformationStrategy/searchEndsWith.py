__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation

class SearchEndsWith(SearchInformation):

    def __setRegex(self, wantedInformation):
        self.regex = '(\\b[A-Z].*' + wantedInformation + '\b)'