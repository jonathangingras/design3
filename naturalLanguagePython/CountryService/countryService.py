__author__ = 'Antoine'
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.countryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.countryParser.countryRepositoryFiller import CountryRepositoryFiller

class CountryService(object):

    def __init__(self):
        self.countryRepository = CountryRepositoryDB()
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()
        self.searchStrategy = None
        #self.__setupTheCountryRepository()

    def __setupTheCountryRepository(self):
        self.countryRepositoryFiller = CountryRepositoryFiller(self.countryRepository)
        self.countryRepositoryFiller.addCountriesToTheRepository()

    def __findCountryAppearingInListOfPossibleCountry(self, listOfCountry, nameOfCountryFistCall):
        numberOfAppearanceOfNameOfCountry = 0
        for nameOfCountryList in listOfCountry:
            for namePossible in nameOfCountryList:
                if namePossible == nameOfCountryFistCall:
                    numberOfAppearanceOfNameOfCountry += 1
        return numberOfAppearanceOfNameOfCountry

    def searchCountry(self, searchedInformationDict, wantedSearchStrategy = None):
        nameOfCountry = ""
        wantedSearchStrategy = self.searchStrategyServiceFactory.wantedSearchStrategyValidator(searchedInformationDict, wantedSearchStrategy)
        listOfPossibleCountryByCategory = self.searchStrategyServiceFactory.searchPossiblesCountryInRepository(self.countryRepository,
                                                                                                               searchedInformationDict, wantedSearchStrategy)
        for nameOfCountryFistCall in listOfPossibleCountryByCategory[0]:
            numberOfAppearanceOfNameOfCountry = self.__findCountryAppearingInListOfPossibleCountry(listOfPossibleCountryByCategory,
                                                                                                   nameOfCountryFistCall)
            if numberOfAppearanceOfNameOfCountry == len(listOfPossibleCountryByCategory):
                nameOfCountry = nameOfCountryFistCall
                break
        return nameOfCountry