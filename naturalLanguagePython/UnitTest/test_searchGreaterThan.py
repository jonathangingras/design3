from unittest import TestCase
from mock import Mock
from naturalLanguagePython.countryPersistence.countryRepositoryElasticSearch import Elasticsearch
from naturalLanguagePython.searchInformationStrategy.searchKeywordException import SearchKeywordException
from naturalLanguagePython.searchInformationStrategy.searchGreaterThan import SearchGreaterThan
__author__ = 'Antoine'


class TestGreaterThanWith(TestCase):

    def setUp(self):
        self.searchStartsWith = SearchGreaterThan("C:\Users\Antoine\Documents\\design3\\naturalLanguagePython")
        self.repository = Elasticsearch("path")

    def test_createSearchQueryWhenHavingNoneKeywordShouldReturnNone(self):
        keyword = None
        value = "value"
        expectedException = SearchKeywordException
        self.assertRaises(expectedException, self.searchStartsWith.searchPossibleCountryByKeywordValue, keyword, value, self.repository)