import os
from unittest import TestCase
from naturalLanguagePython.countryPersistence.countryRepositoryElasticSearch import Elasticsearch
from naturalLanguagePython.searchInformationStrategy.searchKeywordException import SearchKeywordException
from naturalLanguagePython.searchInformationStrategy.searchGreaterThan import SearchGreaterThan
__author__ = 'Antoine'


class TestGreaterThanWith(TestCase):

    def setUp(self):
        pathToModule = os.getcwd()
        self.searchStartsWith = SearchGreaterThan(pathToModule)
        self.repository = Elasticsearch("path")

    def test_createSearchQueryWhenHavingNoneKeywordShouldReturnNone(self):
        keyword = None
        value = "value"
        expectedException = SearchKeywordException
        self.assertRaises(expectedException, self.searchStartsWith.searchPossibleCountryByKeywordValue, keyword, value, self.repository)