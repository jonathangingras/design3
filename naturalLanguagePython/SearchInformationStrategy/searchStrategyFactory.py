__author__ = 'Antoine'

from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.searchInformationStrategy.searchStartsWith import SearchStartsWith
from naturalLanguagePython.searchInformationStrategy.searchEndsWith import SearchEndsWith
from naturalLanguagePython.searchInformationStrategy.searchBetween import SearchBetween
from naturalLanguagePython.searchInformationStrategy.searchGreaterThan import SearchGreaterThan
from naturalLanguagePython.searchInformationStrategy.searchLessThan import SearchLessThan

class SearchStrategyFactory(object):

    def __init__(self, pathToModule):
        self.searchStrategy = None
        self.pathToModule = pathToModule

    def createSearchStrategy(self, strategyParticularity = None):
        if strategyParticularity == "Contains":
            self.searchStrategy = SearchContains()
        if strategyParticularity == "including":
            self.searchStrategy = SearchContains()
        elif strategyParticularity == "starts with":
            self.searchStrategy = SearchStartsWith()
        elif strategyParticularity == "ends with":
            self.searchStrategy = SearchEndsWith()
        elif strategyParticularity == "between":
            self.searchStrategy = SearchBetween()
        elif strategyParticularity == "greater than":
            self.searchStrategy = SearchGreaterThan(self.pathToModule)
        elif strategyParticularity == "less than":
            self.searchStrategy = SearchLessThan(self.pathToModule)
        elif strategyParticularity is None:
            self.searchStrategy = SearchContains()
        return self.searchStrategy

