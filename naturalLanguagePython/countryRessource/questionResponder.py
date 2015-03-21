__author__ = 'Antoine'
from naturalLanguagePython.countryService.countryService import CountryService

class QuestionResponder(object):

    def __init__(self, currentProjectPath):
        self.countryService = CountryService(currentProjectPath)

    def askQuestion(self, question):
        nameOfCountry = None
        if question is not None:
            dictionary = self.countryService.analyzeQuestionFromAtlas(question)
            questionSearchParticularity = self.countryService.searchQuestionSearchStrategyParticularity(question)
            formattedDictionary = self.countryService.formatKeywordFromSemanticAnalysisToWorldFactbook(dictionary)
            formattedDictionary = self.countryService.formatValueInformationFromSemanticAnalysisToWorldFactBook(formattedDictionary)
            # print(formattedDictionary)
            nameOfCountry = self.countryService.searchCountry(formattedDictionary, questionSearchParticularity)
        return nameOfCountry