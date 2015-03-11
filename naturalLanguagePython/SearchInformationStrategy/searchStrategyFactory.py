__author__ = 'Antoine'

from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.searchInformationStrategy.searchStartsWith import SearchStartsWith
from naturalLanguagePython.searchInformationStrategy.searchEndsWith import SearchEndsWith
class SearchStrategyFactory(object):

    def __init__(self):
        self.searchStrategy = None

    def createSearchStrategy(self, strategyParticularity = None):
        if strategyParticularity == "Contains":
            self.searchStrategy = SearchContains()
        elif strategyParticularity == "starts with":
            self.searchStrategy = SearchStartsWith()
        elif strategyParticularity == "ends with":
            self.searchStrategy = SearchEndsWith()
        elif strategyParticularity is None:
            self.searchStrategy = SearchContains()
        return self.searchStrategy

