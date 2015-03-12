from unittest import TestCase
from naturalLanguagePython.countryRessource.questionResponder import QuestionResponder
__author__ = 'Antoine'


class TestQuestionResponder(TestCase):

    def setUp(self):
        path = "C:\Users\Antoine\Documents\\design3\\naturalLanguagePython"
        self.questionResponder = QuestionResponder(path)

    def test_askingQuestionWhenSearchingByCountryCapitalShouldReturnTheNameOfCorrespondingCountry(self):
        askedQuestion = "What country has Yaounde as its capital?"
        expectedNameOfCountry = "France"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

