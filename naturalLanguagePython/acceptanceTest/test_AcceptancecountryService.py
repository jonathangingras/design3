from naturalLanguagePython.CountryService.countryService import CountryService
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
        expectedReturnedCountryName = "Unable to return only one Country. Here's the list of possible ones : " \
                                      "['Nepal', 'Afghanistan', 'Uganda', 'Kazakhstan']"
        dictionaryFromQuestion = {"Capital": "Ka"}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion, ["starts with"]))

    def test_usingServiceToSearchACountryWhenSearchingForACapitalByItsEndsWithNameShouldReturnTheNameOfPossibleCountry(self):
        expectedReturnedCountryName = 'Greece'
        dictionaryFromQuestion = {"Capital": "ens"}
        self.assertEqual(expectedReturnedCountryName, self.countryService.searchCountry(dictionaryFromQuestion, ["ends with"]))
