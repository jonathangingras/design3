__author__ = 'Antoine'
from naturalLanguagePython.countryService.countryService import CountryService

class QuestionResponder(object):

    def __init__(self, currentProjectPath):
        self.countryService = CountryService(currentProjectPath)

    def askQuestion(self, question):
        nameOfCountry = None
        if question is not None:
            dictionary = self.countryService.analyzeQuestionFromAtlas(question)
            formattedDictionary = self.countryService.formatKeywordFromSemanticAnalysisToWorldFactbook(dictionary)
            formattedDictionary = self.countryService.formatValueInformationFromSemanticAnalysisToWorldFactBook(formattedDictionary)
            questionSearchParticularity = self.countryService.searchQuestionSearchStrategyParticularity(question)
            searchStrategyByKeywordDictionary = self.countryService.linkSearchStrategyToKeyword(
                question, dictionary, questionSearchParticularity
            )
            formattedSearchStrategyByKeywordDictionary = self.countryService.formatKeywordFromSemanticAnalysisToWorldFactbook(searchStrategyByKeywordDictionary)
            print(formattedDictionary)
            nameOfCountry = self.countryService.searchCountry(formattedDictionary, formattedSearchStrategyByKeywordDictionary)
        return nameOfCountry