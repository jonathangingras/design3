from unittest import TestCase
from mock import Mock
from naturalLanguagePython.countryPersistence.countryRepositoryElasticSearch import Elasticsearch
from naturalLanguagePython.searchInformationStrategy.searchKeywordException import SearchKeywordException
from naturalLanguagePython.searchInformationStrategy.searchEndsWith import SearchEndsWith
__author__ = 'Antoine'


class TestSearchEndsWith(TestCase):
    def setUp(self):
        self.searchEndsWith = SearchEndsWith()
        self.repository = Elasticsearch("path")

    def test_createSearchQueryWhenHavingNoneKeywordShouldReturnNone(self):
        keyword = None
        value = "value"
        expectedException = SearchKeywordException
        self.assertRaises(expectedException, self.searchEndsWith.searchPossibleCountryByKeywordValue, keyword, value, self.repository)

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
        returnedPossibleCountryList = self.searchEndsWith.searchPossibleCountryByKeywordValue(keyword, value, self.repository)
        self.assertEqual(expectedReturnPossibleCountryList, returnedPossibleCountryList)
