from unittest import TestCase
from mock import Mock
from naturalLanguagePython.countryPersistence.countryRepositoryElasticSearch import Elasticsearch
from naturalLanguagePython.searchInformationStrategy.searchKeywordException import SearchKeywordException
from naturalLanguagePython.searchInformationStrategy.searchStartsWith import SearchStartsWith
__author__ = 'Antoine'


class TestSearchStartsWith(TestCase):

    def setUp(self):
        self.searchStartsWith = SearchStartsWith()
        self.repository = Elasticsearch("path")

    def test_createSearchQueryWhenHavingNoneKeywordShouldReturnNone(self):
        keyword = None
        value = "value"
        expectedException = SearchKeywordException
        self.assertRaises(expectedException, self.searchStartsWith.searchPossibleCountryByKeywordValue, keyword, value, self.repository)

    def test_createSearchQueryWhenHavingValidKeywordShouldReturnListOfCountry(self):
        keyword = "keyword"
        value = "value"
        self.repository.search = Mock(return_value={
            "hits": {
                "hits":
                    [{"_id": "a country"}]
            }
        })
        expectedReturnPossibleCountryList = ["a country"]
        returnedPossibleCountryList = self.searchStartsWith.searchPossibleCountryByKeywordValue(keyword, value, self.repository)
        self.assertEqual(expectedReturnPossibleCountryList, returnedPossibleCountryList)