__author__ = 'Antoine'
from naturalLanguagePython.countryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.questionLanguageAnalyzer.questionInformationAnalyser import QuestionInformationAnalyser
from naturalLanguagePython.countryService.countryServiceException import CountryServiceException
from naturalLanguagePython.countryService.dictionaryInformationKeywordFormatter import DictionaryInformationFormatter
from naturalLanguagePython.countryService.dictionaryValueInformationFormatter import DictionaryValueInformationFormatter
from naturalLanguagePython.countryPersistence.countryRepositoryElasticSearch import CountryRepositoryElasticSearch
from naturalLanguagePython.countryService.searchResultAnalyzer import SearchResultAnalyzer


class CountryService(object):

    def __init__(self, currentWorkspacePath):
        self.countryRepository = CountryRepositoryElasticSearch(currentWorkspacePath)
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()
        self.__dictionaryInformationFormatter = DictionaryInformationFormatter(currentWorkspacePath)
        self.__dictionaryValueFormatter = DictionaryValueInformationFormatter()
        self.questionAnalyzer = QuestionInformationAnalyser()
        self.searchRequestExecutor = SearchResultAnalyzer()

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
            receivedQuestion, dictionary, questionSearchParticularity)

    def formatKeywordFromSemanticAnalysisToWorldFactBook(self, receivedDictionary):
        formattedDictionary = self.__dictionaryInformationFormatter.formatDictionary(receivedDictionary)
        return  formattedDictionary

    def formatValueInformationFromSemanticAnalysisToWorldFactBook(self, receivedDictionary):
        formattedDictionary = self.__dictionaryValueFormatter.formatValueInformation(receivedDictionary)
        return formattedDictionary



    def __verifyNameOfCountryFormat(self, nameOfCountry):
        if type(nameOfCountry) is list:
            nameOfCountry = nameOfCountry[0]
        return nameOfCountry

    def searchCountry(self, searchedInformationDict, wantedSearchStrategy = None):
        wantedSearchStrategy = self.searchStrategyServiceFactory.wantedSearchStrategyValidator(searchedInformationDict,
                                                                                               wantedSearchStrategy)
        listOfPossibleCountryByCategory = self.countryRepository.searchCountries(
            searchedInformationDict, wantedSearchStrategy)
        nameOfCountryList = self.searchRequestExecutor.findPossibleCountryNameInSearchResultByKeyword(listOfPossibleCountryByCategory)
        nameOfCountry = self.__verifyNameOfCountryFormat(nameOfCountryList)
        return nameOfCountry


