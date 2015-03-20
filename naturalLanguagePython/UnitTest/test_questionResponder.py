from unittest import TestCase
from mock import Mock
from naturalLanguagePython.countryRessource.questionResponder import QuestionResponder
__author__ = 'Antoine'


class TestQuestionResponder(TestCase):
    def setUp(self):
        path = "C:\Users\Antoine\Documents\\design3\\naturalLanguagePython"
        self.questionResponder = QuestionResponder(path)

    def test_askingAQuestionWhenHavingAnEmptyQuestionShouldReturnNone(self):
        question = None
        expectedReturn = None
        self.assertEqual(expectedReturn, self.questionResponder.askQuestion(question))

    def test_askingAQuestionWhenHavingAnNonEmptyQuestionShouldReturnTheNameOfTheSearchedCountry(self):
        question = "A question"
        expectedReturn = "A Country"
        self.questionResponder.countryService.analyzeQuestionFromAtlas= Mock()
        self.questionResponder.countryService.searchCountry = Mock(return_value = expectedReturn)
        self.questionResponder.countryService.formatKeywordFromSemanticAnalysisToWorldFactbook = Mock()
        self.questionResponder.countryService.formatValueInformationFromSemanticAnalysisToWorldFactBook = Mock()
        self.assertEqual(expectedReturn, self.questionResponder.askQuestion(question))
