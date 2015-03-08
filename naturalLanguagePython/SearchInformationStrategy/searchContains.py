__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
class SearchContains(SearchInformation):

    def __setRegex(self, wantedInformation):
        self.regex = '(\\b' + wantedInformation + 'W\\b)'
