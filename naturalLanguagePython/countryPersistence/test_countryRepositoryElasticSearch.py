from unittest import TestCase
import json
from os import path
from elasticsearch import Elasticsearch
from naturalLanguagePython.countryPersistence.countryRepositoryElasticSearch import CountryRepositoryElasticSearch
__author__ = 'Antoine'


class TestCountryRepositoryElasticSearch(TestCase):

    def setUp(self):
        self.countryRepository = CountryRepositoryElasticSearch("path")
        # elastic = Elasticsearch()
        # russie = open("Russia.json")
        # jsonR = json.load(russie)
        # elastic.create(index="country", doc_type="data", id="Russia", body=jsonR)

    def test_searchCountryWhenSearchingByAParsedCountryShouldReturnTheNameOfTheCountry(self):
        searchInformationDictionary = {"capital": ["Paris"]}
        searchStrategyByKeyword = {"capital":["Contains"]}
        expectedNameOfCountry = [["France"]]
        self.assertEqual(expectedNameOfCountry, self.countryRepository.searchCountries(searchInformationDictionary,
                                                                                       searchStrategyByKeyword))
