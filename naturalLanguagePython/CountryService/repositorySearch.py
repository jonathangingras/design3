__author__ = 'Antoine'
from naturalLanguagePython.CountryService.searchStrategyServiceFactory import SearchStrategyServiceFactory


class RepositorySearch(object):

    def __init__(self):
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()

    def searchPossiblesCountryInRepository(self, countryRepository, searchedInformationDict, wantedSearchStrategy):
        wantedSearchStrategy = self.searchStrategyServiceFactory.wantedSearchStrategyValidator(searchedInformationDict, wantedSearchStrategy)
        searchStrategyNumberInList = 0
        listOfCountry = []
        for key in searchedInformationDict:
            self.searchStrategy = self.searchStrategyServiceFactory.searchStrategyFactory.createSearchStrategy(
                wantedSearchStrategy[searchStrategyNumberInList])
            listOfCountry.append(countryRepository.searchCountries(searchedInformationDict, self.searchStrategy))
            searchStrategyNumberInList += 1
        return listOfCountry