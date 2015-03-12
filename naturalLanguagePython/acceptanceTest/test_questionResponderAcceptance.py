from unittest import TestCase
from naturalLanguagePython.countryRessource.questionResponder import QuestionResponder
__author__ = 'Antoine'


class TestQuestionResponder(TestCase):

    def setUp(self):
        path = "C:\Users\Antoine\Documents\\design3\\naturalLanguagePython"
        self.questionResponder = QuestionResponder(path)

    def test_askingQuestionWhenSearchingByCountryCapitalShouldReturnTheNameOfCorrespondingCountry(self):
        askedQuestion = "What country has Yaounde as its capital?"
        expectedNameOfCountry = "Cameroon"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsUnemploymentRateShouldReturnTheNameOfCorrespondingCountry(self):
        askedQuestion = "My unemployment rate is 40.6%."
        expectedNameOfCountry = "Haiti"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsInternetCodeShouldReturnTheNameOfCorrespondingCountry(self):
        askedQuestion = "My internet country code is .br."
        expectedNameOfCountry = "Brazil"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsYearAndMonthOfIndependenceShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "My independence was declared in August 1971."
        expectedNameOfCountry = "Bahrain"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsNationalSymbolShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "One national symbol of this country is the edelweiss."
        expectedNameOfCountry = "Switzerland"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))