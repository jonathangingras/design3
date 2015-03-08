__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
from naturalLanguagePython.CountryService.countryServiceException import CountryServiceException
defaultSearchStrategy = "Contains"


class SearchStrategyServiceFactory(object):

    def __init__(self):
        self.searchStrategyFactory = SearchStrategyFactory()

    def wantedSearchStrategyValidator(self, searchedInformationDict, wantedSearchStrategy):
        if wantedSearchStrategy is None:
            wantedSearchStrategy = []
        if len(searchedInformationDict) < len(wantedSearchStrategy):
            raise CountryServiceException(
                "The number of wanted information needs to be higher than the number of wanted search strategy")
        while len(wantedSearchStrategy) < len(searchedInformationDict):
            wantedSearchStrategy.append(defaultSearchStrategy)
        return wantedSearchStrategy
