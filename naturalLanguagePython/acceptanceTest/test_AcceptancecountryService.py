from naturalLanguagePython.CountryService.countryService import CountryService
from unittest import TestCase

__author__ = 'Antoine'


class AcceptanceTestCountryService(TestCase):

    def test_usingServiceToSearchACountryWhenSearchingForACapitalShouldReturnTheNameOfTheCountry(self):
        countryService = CountryService()
        expectedReturnedCountryName = "Canada"
        dictionaryFromQuestion = {"Capital": "Ottawa"}

        self.assertEqual(expectedReturnedCountryName, countryService.searchCountry(dictionaryFromQuestion))

    def test_usingServiceToSearchACountryWhenSearchingForACapitalStartsWithNameShouldReturnTheNameOfTheCountry(self):
        countryService = CountryService()
        expectedReturnedCountryName = "United_State_Of_America"
        dictionaryFromQuestion = {"Capital": "Wa"}
        self.assertEqual(expectedReturnedCountryName, countryService.searchCountry(dictionaryFromQuestion, ["starts with"]))