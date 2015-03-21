__author__ = 'Antoine'
from naturalLanguagePython.countryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.countryParser.countryRepositoryFiller import CountryRepositoryFiller
from naturalLanguagePython.questionLanguageAnalyzer.questionInformationAnalyser import QuestionInformationAnalyser
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.countryService.repositorySearch import RepositorySearch
from naturalLanguagePython.countryService.countryServiceException import CountryServiceException
from naturalLanguagePython.countryService.dictionaryInformationKeywordFormatter import DictionaryInformationFormatter
from naturalLanguagePython.countryService.dictionaryValueInformationFormatter import DictionaryValueInformationFormatter


class CountryService(object):

    def __init__(self, currentWorkspacePath):
        self.countryRepository = CountryRepositoryDB()
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()
        self.__dictionaryInformationFormatter = DictionaryInformationFormatter(currentWorkspacePath)
        self.__dictionaryValueFormatter = DictionaryValueInformationFormatter()
        self.questionAnalyzer = QuestionInformationAnalyser()
        self.__setupTheCountryRepository(currentWorkspacePath)
        self.__repositorySearch = RepositorySearch()

    def analyzeQuestionFromAtlas(self, receivedQuestion):
        if receivedQuestion is None:
            raise CountryServiceException("The received question from Atlas is empty")
        if receivedQuestion is "":
            raise CountryServiceException("The received question from Atlas is empty")
        dictionaryOfImportantInformation = self.questionAnalyzer.analyseQuestion(receivedQuestion)
        return dictionaryOfImportantInformation

    def searchQuestionSearchStrategyParticularity(self, receivedQuestion):
        return self.questionAnalyzer.analyseQuestionParticularity(receivedQuestion)

    def linkSearchStrategyToKeyword(self, receivedQuestion, dictionary, questionSearchParticularity):
        return self.questionAnalyzer.linkSearchStrategyToKeywordRelatedToQuestion(
            receivedQuestion, dictionary, questionSearchParticularity
        )

    def formatKeywordFromSemanticAnalysisToWorldFactbook(self, receivedDictionary):
        formattedDictionary = self.__dictionaryInformationFormatter.formatDictionary(receivedDictionary)
        return  formattedDictionary

    def formatValueInformationFromSemanticAnalysisToWorldFactBook(self, receivedDictionary):
        formattedDictionary = self.__dictionaryValueFormatter.formatValueInformation(receivedDictionary)
        return formattedDictionary

    def searchCountry(self, searchedInformationDict, wantedSearchStrategy = None):
        nameOfCountry = ""
        listOfPossibleCountryByCategory = self.__repositorySearch.searchPossiblesCountryInRepository(self.countryRepository,
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
