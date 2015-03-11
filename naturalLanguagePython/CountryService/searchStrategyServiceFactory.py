__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
from naturalLanguagePython.countryService.countryServiceException import CountryServiceException
defaultSearchStrategy = "Contains"


class SearchStrategyServiceFactory(object):

    def __init__(self):
        self.searchStrategyFactory = SearchStrategyFactory()

    def wantedSearchStrategyValidator(self, searchedInformationDict, wantedSearchStrategy = None):
        if wantedSearchStrategy is None:
            wantedSearchStrategy = []
        if len(searchedInformationDict) < len(wantedSearchStrategy):
            raise CountryServiceException(
                "The number of wanted information needs to be higher than the number of wanted search strategy")
        while len(wantedSearchStrategy) < len(searchedInformationDict):
            wantedSearchStrategy.append(defaultSearchStrategy)
        return wantedSearchStrategy

    def createStrategy(self, searchStrategy = None):
        return self.searchStrategyFactory.createSearchStrategy(searchStrategy)