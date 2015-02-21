__author__ = 'Antoine'

from naturalLanguagePython.SearchInformationStrategy.searchInformation import SearchInformation

class SearchStartsWith(SearchInformation):


    def __setRegex(self, wantedInformation):
        self.regex = '(\\b' + wantedInformation + '.*\\b)'
