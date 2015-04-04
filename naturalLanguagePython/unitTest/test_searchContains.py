from unittest import TestCase
from mock import Mock
from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.countryPersistence.countryRepositoryElasticSearch import Elasticsearch
from naturalLanguagePython.searchInformationStrategy.searchKeywordException import SearchKeywordException
__author__ = 'Antoine'


class TestSearchContains(TestCase):
    def setUp(self):
        self.searchContains = SearchContains()
        self.repository = Elasticsearch("path")

    def test_createSearchQueryWhenHavingNoneKeywordShouldReturnNone(self):
        keyword = None
        value = "value"
        expectedException = SearchKeywordException
        self.assertRaises(expectedException, self.searchContains.searchPossibleCountryByKeywordValue, keyword, value, self.repository)

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
        returnedPossibleCountryList = self.searchContains.searchPossibleCountryByKeywordValue(keyword, value, self.repository)
        self.assertEqual(expectedReturnPossibleCountryList, returnedPossibleCountryList)

    def test_createSearchQueryWhenHavingCapitalKeywordAndValueWashingtonShouldReturnUnitedStatesInsideList(self):
        keyword = "capital"
        value = "Washington"
        expectedReturnPossibleCountryList = ["United_States"]
        self.assertEqual(expectedReturnPossibleCountryList, self.searchContains.searchPossibleCountryByKeywordValue(keyword,
                                                                                                                    value,
                                                                                                                    self.repository))
