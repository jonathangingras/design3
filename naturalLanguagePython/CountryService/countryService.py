__author__ = 'Antoine'
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.countryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.countryParser.countryRepositoryFiller import CountryRepositoryFiller
from naturalLanguagePython.countryService.countryServiceException import CountryServiceException
from naturalLanguagePython.questionLanguageAnalyzer.questionInformationAnalyser import QuestionInformationAnalyser
from naturalLanguagePython.countryService.repositorySearch import RepositorySearch



class CountryService(object):

    def __init__(self, currentWorkspacePath):
        self.countryRepository = CountryRepositoryDB()
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()
        self.questionAnalyzer = QuestionInformationAnalyser()
        self.__setupTheCountryRepository(currentWorkspacePath)
        self.repositorySearch = RepositorySearch()

    def analyzeQuestionFromAtlas(self, receivedQuestion):
        dictionaryOfImportantInformation = {}
        if receivedQuestion is None:
            raise CountryServiceException("The received question from Atlas is empty")
        if receivedQuestion is "":
            raise CountryServiceException("The received question from Atlas is empty")
        dictionaryOfImportantInformation = self.questionAnalyzer.analyseQuestion(receivedQuestion)
        return dictionaryOfImportantInformation

    def searchCountry(self, searchedInformationDict, wantedSearchStrategy = None):
        nameOfCountry = ""
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

    def __setupTheCountryRepository(self, currentWorkspacePath):
        self.countryRepositoryFiller = CountryRepositoryFiller(self.countryRepository)
        self.countryRepositoryFiller.addCountriesToTheRepository(currentWorkspacePath)

    def __findCountryAppearingInListOfPossibleCountry(self, listOfCountry, nameOfCountryFistCall):
        numberOfAppearanceOfNameOfCountry = 0
        for nameOfCountryList in listOfCountry:
            for namePossible in nameOfCountryList:
                if namePossible == nameOfCountryFistCall:
                    numberOfAppearanceOfNameOfCountry += 1
        return numberOfAppearanceOfNameOfCountry
