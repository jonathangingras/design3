import os
from naturalLanguagePython.countryService.countryService import CountryService
from unittest import TestCase

__author__ = 'Antoine'


class AcceptanceTestCountryService(TestCase):

    def setUp(self):
        path = os.getcwd()
        self.countryService = CountryService(path)

    def test_usingServiceToSearchACountryWhenSearchingForACapitalShouldReturnTheNameOfTheCountry(self):
        expectedReturnedCountryName = "Canada"
        dictionaryFromQuestion = {"capital": ["Ottawa"]}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion))

    def test_usingServiceToSearchACountryWhenSearchingForACapitalStartsWithNameShouldReturnTheNameOfTheCountry(self):
        expectedReturnedCountryName = "Afghanistan"
        dictionaryFromQuestion = {"capital": ["Kab"]}
        searchStrategyDictionary = {"capital": ["starts with"]}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion, searchStrategyDictionary))

    def test_analyzingAQuestionWhenTheReceivedStringIsACapitalNameIsInQuestionShouldReturnTheCorrectDictionary(self):
        expectedDictionary = {"capital": ["Paris"]}
        receivedQuestion = "What country has Paris as its capital?"
        self.assertEqual(expectedDictionary, self.countryService.analyzeQuestionFromAtlas(receivedQuestion))

    def test_usingServiceToSearchACountryWhenSearchingForAExportPartnersShouldReturnTheNameOfTheCountry(self):
        dictionaryFromQuestion = {"exports - partners": ["US", "Germany", "UK", "France", "Spain", "Canada", "Italy"]}
        expectedReturnedCountryName = "Bangladesh"
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion))

    def test_usingServiceToSearchACountryWhenSearchingByItsNaturalSymbolShouldReturnTheNameOfTheCountry(self):
        dictionaryFromQuestion = {'national symbol(s)': ['edelweiss']}
        expectedReturnedCountryName = "Austria"
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion))
