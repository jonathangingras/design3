__author__ = 'Antoine'

from naturalLanguagePython.SearchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.SearchInformationStrategy.searchStartsWith import SearchStartsWith
from naturalLanguagePython.SearchInformationStrategy.searchEndsWith import SearchEndsWith
class SearchStrategyFactory(object):

    def __init__(self):
        self.searchStrategy = None

    def createSearchStrategy(self, strategyParticularity = None):
        if strategyParticularity is "starts with":
            self.searchStrategy = SearchStartsWith()
        elif strategyParticularity is "ends with":
            self.searchStrategy = SearchEndsWith()
        elif strategyParticularity is None:
            self.searchStrategy = SearchContains()
        return self.searchStrategy

