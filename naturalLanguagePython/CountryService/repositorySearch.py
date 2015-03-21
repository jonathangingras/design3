__author__ = 'Antoine'
from naturalLanguagePython.countryService.searchStrategyServiceFactory import SearchStrategyServiceFactory


class RepositorySearch(object):

    def __init__(self):
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()

    def searchPossiblesCountryInRepository(self, countryRepository, searchedInformationDict, wantedSearchStrategy):
        wantedSearchStrategy = self.searchStrategyServiceFactory.wantedSearchStrategyValidator(searchedInformationDict, wantedSearchStrategy)
        listOfCountry = []
        for keyword in searchedInformationDict:
            for informationElement in searchedInformationDict[keyword]:
                print(informationElement)
                searchStrategyNumberInList = 0
                self.searchStrategy = self.searchStrategyServiceFactory.searchStrategyFactory.createSearchStrategy(
                wantedSearchStrategy[keyword][searchStrategyNumberInList])
                print(self.searchStrategy)
                listOfCountry.append(countryRepository.searchCountries(searchedInformationDict, self.searchStrategy))
                searchStrategyNumberInList += 1
        return listOfCountry