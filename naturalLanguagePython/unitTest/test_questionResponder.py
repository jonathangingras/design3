from unittest import TestCase
import os
from mock import Mock
from naturalLanguagePython.countryRessource.questionResponder import QuestionResponder
__author__ = 'Antoine'


class TestQuestionResponder(TestCase):
    def setUp(self):
        path = os.getcwd()
        self.questionResponder = QuestionResponder(path)

    def test_askingAQuestionWhenHavingAnEmptyQuestionShouldReturnNone(self):
        question = None
        expectedReturn = ""
        self.assertEqual(expectedReturn, self.questionResponder.askQuestion(question))

    def test_askingAQuestionWhenHavingAnNonEmptyQuestionShouldReturnTheNameOfTheSearchedCountry(self):
        question = "A question"
        expectedReturn = "A Country"
        self.questionResponder.countryService.analyzeQuestionFromAtlas= Mock()
        self.questionResponder.countryService.searchCountry = Mock(return_value = expectedReturn)
        self.questionResponder.countryService.formatKeywordFromSemanticAnalysisToWorldFactBook = Mock()
        self.questionResponder.countryService.formatValueInformationFromSemanticAnalysisToWorldFactBook = Mock()
        self.questionResponder.countryService.linkSearchStrategyToKeyword = Mock()
        self.assertEqual(expectedReturn, self.questionResponder.askQuestion(question))
