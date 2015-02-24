__author__ = 'Antoine'
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
from naturalLanguagePython.countryService.countryServiceException import CountryServiceException

class CountryService(object):

    def __init__(self):
        self.countryRepository = CountryRepositoryDB()
        self.searchStrategyFactory = SearchStrategyFactory()
        self.searchStrategy = None

    def searchCountry(self, searchedInformationDict, wantedSearchStrategy = None):
        nameOfCountry = ""
        listOfCountry = []
        if self.countryRepository.countryList == []:
            return "Repository is empty"
        else:
            if wantedSearchStrategy is None:
                wantedSearchStrategy = []
            if len(searchedInformationDict) < len(wantedSearchStrategy):
                raise CountryServiceException(
                    "The number of wanted information needs to be higher than the number of wanted search strategy")
            while len(wantedSearchStrategy) < len(searchedInformationDict):
                wantedSearchStrategy.append("Contains")
            searchStrategyNumberInList = 0
            for key in searchedInformationDict:
                self.searchStrategy = self.searchStrategyFactory.createSearchStrategy(wantedSearchStrategy[searchStrategyNumberInList])
                listOfCountry.append(self.countryRepository.searchCountries(searchedInformationDict, self.searchStrategy))
                searchStrategyNumberInList += 1
            numberOfCategory = len(listOfCountry)
            for nameOfCountryFistCall in listOfCountry[0]:
                numberOfAppearanceOfNameOfCountry = 0
                for nameOfCountryList in listOfCountry:
                    for namePossible in nameOfCountryList:
                        if namePossible == nameOfCountryFistCall:
                            numberOfAppearanceOfNameOfCountry += 1
                if numberOfAppearanceOfNameOfCountry == numberOfCategory:
                    nameOfCountry = nameOfCountryFistCall
                    break
            return nameOfCountry