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

    def test_askingQuestionWhenSearchingByOneOfItsNationalSymbolShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "One national symbol of this country is the edelweiss."
        expectedNameOfCountry = "Switzerland"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsNumberOfInternetUsersShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "What country has 13.694 million internet users?"
        expectedNameOfCountry = "Argentina"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsNationalSymbolShouldReturnCountryName(self):
        askedQuestion = "My national symbol is the elephant."
        expectedNameOfCountry = "Madagascar"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsBirthRateShouldReturnCountryName(self):
        askedQuestion = "What country has a birth rate of 46.12 births/ 1000 population?"
        expectedNameOfCountry = ""
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsTelephoneLinesNumbersShouldReturnNameOfCountry(self):
        askedQuestion = "My telephone lines in use are 1.217 million."
        expectedNameOfCountry = ""
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsNationalAnthemShouldReturnTheNameOfCountry(self):
        askedQuestion = "The title of my national anthem is Advance Australia Fair."
        expectedNameOfCountry = ""
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

