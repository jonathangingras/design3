__author__ = 'Antoine'
from naturalLanguagePython.SearchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
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

    def searchPossiblesCountryInRepository(self, countryRepository, searchedInformationDict, wantedSearchStrategy):
        searchStrategyNumberInList = 0
        listOfCountry = []
        for key in searchedInformationDict:
            self.searchStrategy = self.searchStrategyFactory.createSearchStrategy(
                wantedSearchStrategy[searchStrategyNumberInList])
            listOfCountry.append(countryRepository.searchCountries(searchedInformationDict, self.searchStrategy))
            searchStrategyNumberInList += 1
        return listOfCountry