__author__ = 'Antoine'
from naturalLanguagePython.countryService.searchStrategyServiceFactory import SearchStrategyServiceFactory


class RepositorySearch(object):

    def __init__(self):
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()

    def searchPossiblesCountryInRepository(self, countryRepository, searchedInformationDict, wantedSearchStrategy):
        wantedSearchStrategy = self.searchStrategyServiceFactory.wantedSearchStrategyValidator(searchedInformationDict, wantedSearchStrategy)
        print(wantedSearchStrategy)
        searchStrategyNumberInList = 0
        listOfCountry = []
        for key in searchedInformationDict:
            self.searchStrategy = self.searchStrategyServiceFactory.searchStrategyFactory.createSearchStrategy(
                wantedSearchStrategy[searchStrategyNumberInList])
            print(self.searchStrategy)
            listOfCountry.append(countryRepository.searchCountries(searchedInformationDict, self.searchStrategy))
            print(listOfCountry)
            searchStrategyNumberInList += 1
        return listOfCountry