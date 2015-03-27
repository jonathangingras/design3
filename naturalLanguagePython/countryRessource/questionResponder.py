__author__ = 'Antoine'
from naturalLanguagePython.countryService.countryService import CountryService

class QuestionResponder(object):

    def __init__(self, currentProjectPath):
        self.countryService = CountryService(currentProjectPath)

    def __formatInformationDictionary(self, dictionary):
        formattedDictionary = self.countryService.formatKeywordFromSemanticAnalysisToWorldFactBook(dictionary)
        formattedDictionary = self.countryService.formatValueInformationFromSemanticAnalysisToWorldFactBook(
            formattedDictionary)
        return formattedDictionary

    def __getSearchStrategyByKeywordDictionary(self, dictionary, question):
        questionSearchParticularity = self.countryService.searchQuestionSearchStrategyParticularity(question)
        searchStrategyByKeywordDictionary = self.countryService.linkSearchStrategyToKeyword(
            question, dictionary, questionSearchParticularity
        )
        formattedSearchStrategyByKeywordDictionary = self.countryService.formatKeywordFromSemanticAnalysisToWorldFactBook(
            searchStrategyByKeywordDictionary)
        return formattedSearchStrategyByKeywordDictionary

    def askQuestion(self, question):
        nameOfCountry = ""
        if question is not None and question != "":
            dictionary = self.countryService.analyzeQuestionFromAtlas(question)
            formattedDictionary = self.__formatInformationDictionary(dictionary)
            formattedSearchStrategyByKeywordDictionary = self.__getSearchStrategyByKeywordDictionary(dictionary,
                                                                                                     question)
            nameOfCountry = self.countryService.searchCountry(formattedDictionary, formattedSearchStrategyByKeywordDictionary)
        return nameOfCountry