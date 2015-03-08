__author__ = 'Antoine'
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.CountryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.countryParser.countryRepositoryFiller import CountryRepositoryFiller
from naturalLanguagePython.CountryService.countryServiceException import CountryServiceException
from naturalLanguagePython.questionLanguageAnalyzer.questionAnalyzer import QuestionAnalyzer
from naturalLanguagePython.CountryService.repositorySearch import RepositorySearch


class CountryService(object):

    def __init__(self):
        self.countryRepository = CountryRepositoryDB()
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()
        self.questionAnalyzer = QuestionAnalyzer()
        self.__setupTheCountryRepository()
        self.repositorySearch = RepositorySearch()

    def analyzeQuestionFromAtlas(self, receivedQuestion):
        if receivedQuestion is None:
            raise CountryServiceException("The received question from Atlas is empty")
        if receivedQuestion is "":
            raise CountryServiceException("The received question from Atlas is empty")
        dictionaryOfImportantInformation = self.questionAnalyzer.extractedImportantInformationsFromQuestion(receivedQuestion)
        return dictionaryOfImportantInformation

    def searchCountry(self, searchedInformationDict, wantedSearchStrategy = None):
        nameOfCountry = ""
        wantedSearchStrategy = self.searchStrategyServiceFactory.wantedSearchStrategyValidator(searchedInformationDict, wantedSearchStrategy)
        listOfPossibleCountryByCategory = self.repositorySearch.searchPossiblesCountryInRepository(self.countryRepository,
                                                                                                               searchedInformationDict, wantedSearchStrategy)
        for nameOfCountryFistCall in listOfPossibleCountryByCategory[0]:
            numberOfAppearanceOfNameOfCountry = self.__findCountryAppearingInListOfPossibleCountry(listOfPossibleCountryByCategory,
                                                                                                   nameOfCountryFistCall)
            if numberOfAppearanceOfNameOfCountry == len(listOfPossibleCountryByCategory):
                nameOfCountry = nameOfCountryFistCall
                break
        if type(nameOfCountry) is list:
            if len(nameOfCountry) > 1:
                return str(nameOfCountry)
            nameOfCountry = nameOfCountry[0]
        return nameOfCountry

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
