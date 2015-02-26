__author__ = 'Antoine'
from naturalLanguagePython.CountryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.CountryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.CountryParser.countryRepositoryFiller import CountryRepositoryFiller
from naturalLanguagePython.CountryService.countryServiceException import CountryServiceException
from naturalLanguagePython.QuestionLanguageAnalyzer.questionAnalyzer import QuestionAnalyzer


class CountryService(object):

    def __init__(self):
        self.countryRepository = CountryRepositoryDB()
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()
        self.searchStrategy = None
        self.questionAnalyzer = QuestionAnalyzer()
        self.__setupTheCountryRepository()

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
        listOfPossibleCountryByCategory = self.searchStrategyServiceFactory.searchPossiblesCountryInRepository(self.countryRepository,
                                                                                                               searchedInformationDict, wantedSearchStrategy)
        for nameOfCountryFistCall in listOfPossibleCountryByCategory[0]:
            numberOfAppearanceOfNameOfCountry = self.__findCountryAppearingInListOfPossibleCountry(listOfPossibleCountryByCategory,
                                                                                                   nameOfCountryFistCall)
            if numberOfAppearanceOfNameOfCountry == len(listOfPossibleCountryByCategory):
                nameOfCountry = nameOfCountryFistCall
                break
        if type(nameOfCountry) is list:
            print(nameOfCountry)
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