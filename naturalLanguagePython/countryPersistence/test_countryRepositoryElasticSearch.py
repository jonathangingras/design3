from unittest import TestCase
import json
from os import path
from naturalLanguagePython.countryPersistence.countryRepositoryElasticSearch import CountryRepositoryElasticSearch
__author__ = 'Antoine'


class TestCountryRepositoryElasticSearch(TestCase):

    def setUp(self):
        self.countryRepository = CountryRepositoryElasticSearch()

    def test_searchCountryWhenSearchingByAParsedCountryShouldReturnTheNameOfTheCountry(self):
        searchInformationDictionary = {"capital": ["Paris"]}
        searchStrategyByKeyword = {"capital":["Contains"]}
        expectedNameOfCountry = [["France"]]
        self.assertEqual(expectedNameOfCountry, self.countryRepository.searchCountries(searchInformationDictionary,
                                                                                       searchStrategyByKeyword))
