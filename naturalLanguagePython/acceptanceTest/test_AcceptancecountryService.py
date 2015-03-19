from naturalLanguagePython.countryService.countryService import CountryService
from unittest import TestCase

__author__ = 'Antoine'


class AcceptanceTestCountryService(TestCase):

    def setUp(self):
        path = "C:\Users\Antoine\Documents\\design3\\naturalLanguagePython"
        self.countryService = CountryService(path)

    def test_usingServiceToSearchACountryWhenSearchingForACapitalShouldReturnTheNameOfTheCountry(self):
        expectedReturnedCountryName = "Canada"
        dictionaryFromQuestion = {"capital": ["Ottawa"]}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion))

    def test_usingServiceToSearchACountryWhenSearchingForACapitalStartsWithNameShouldReturnTheNameOfTheCountry(self):
        expectedReturnedCountryName = "['Nepal', 'Afghanistan', 'Uganda', 'Kazakhstan']"
        expectedReturnedCountryName = "['Afghanistan', 'Kazakhstan', 'Nepal', 'Uganda']"
        dictionaryFromQuestion = {"capital": ["Ka"]}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion, ["starts with"]))

    def test_usingServiceToSearchACountryWhenSearchingForACapitalByItsEndsWithNameShouldReturnTheNameOfPossibleCountry(self):
        expectedReturnedCountryName = 'Greece'
        dictionaryFromQuestion = {"capital": ["ens"]}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion, ["ends with"]))

    def test_analyzingAQuestionWhenTheReceivedStringIsACapitalNameIsInQuestionShouldReturnTheCorrectDictionary(self):
        expectedDictionary = {"capital": ["Paris"]}
        receivedQuestion = "What country has Paris as its capital?"
        self.assertEqual(expectedDictionary, self.countryService.analyzeQuestionFromAtlas(receivedQuestion))

    def test_usingServiceToSearchACountryWhenSearchingForAExportPartnersShouldReturnTheNameOfTheCountry(self):
        dictionaryFromQuestion = {"exports - partners": ["US", "Germany", "UK", "France", "Spain", "Canada", "Italy"]}
        expectedReturnedCountryName = "Bangladesh"
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion))

    def test_usingServiceToSearchACountryWhenSearchingByItsNaturalSymbolShouldReturnTheNameOfTheCountry(self):
        dictionaryFromQuestion = {'national symbol(s)': ['polar bear']}
        expectedReturnedCountryName = "Greenland"
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion))

    #def test_usingServiceToSearchACountryWhenSearchingByItsDeathRateShouldReturnTheNameOfTheCountry(self):
    #    dictionaryFromQuestion = {"death rate": "15 death/1,000",
    #                              "capital": "Mos"}
    #    expectedReturnedCountryName = ""
    #    self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion))