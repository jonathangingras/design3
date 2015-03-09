from naturalLanguagePython.countryService.countryService import CountryService
from unittest import TestCase

__author__ = 'Antoine'


class AcceptanceTestCountryService(TestCase):

    def setUp(self):
        self.countryService = CountryService()
    def test_usingServiceToSearchACountryWhenSearchingForACapitalShouldReturnTheNameOfTheCountry(self):
        expectedReturnedCountryName = "Canada"
        dictionaryFromQuestion = {"Capital": "Ottawa"}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion))

    def test_usingServiceToSearchACountryWhenSearchingForACapitalStartsWithNameShouldReturnTheNameOfTheCountry(self):
        expectedReturnedCountryName = "['Nepal', 'Afghanistan', 'Uganda', 'Kazakhstan']"
        expectedReturnedCountryName = "['Afghanistan', 'Kazakhstan', 'Nepal', 'Uganda']"
        dictionaryFromQuestion = {"Capital": "Ka"}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion, ["starts with"]))

    def test_usingServiceToSearchACountryWhenSearchingForACapitalByItsEndsWithNameShouldReturnTheNameOfPossibleCountry(self):
        expectedReturnedCountryName = 'Greece'
        dictionaryFromQuestion = {"Capital": "ens"}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion, ["ends with"]))

    def test_analyzingAQuestionWhenTheReceivedStringIsACapitalNameIsInQuestionShouldReturnTheCorrectDictionary(self):
        expectedDictionary = {"capital":["Paris"]}
        receivedQuestion = "What country has Paris as its capital?"
        self.assertEqual(expectedDictionary, self.countryService.analyzeQuestionFromAtlas(receivedQuestion))