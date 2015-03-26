from unittest import TestCase

__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.searchInformationStrategy.searchStartsWith import SearchStartsWith
from naturalLanguagePython.searchInformationStrategy.searchEndsWith import SearchEndsWith
from naturalLanguagePython.searchInformationStrategy.searchGreaterThan import SearchGreaterThan
from naturalLanguagePython.searchInformationStrategy.searchLessThan import SearchLessThan
from os import path


class TestSearchStrategyFactory(TestCase):

    def setUp(self):
        self.searchStrategyFactory = SearchStrategyFactory("C:\Users\Antoine\Documents\\design3\\naturalLanguagePython")


    def test_creatingSearchStrategyWhenSearchParticularityIsNoneShouldReturnObjectTypeSearchContains(self):
        searchMethod = self.searchStrategyFactory.createSearchStrategy()
        expectedClassType = SearchContains
        self.assertIsInstance(searchMethod, expectedClassType)

    def test_creatingSearchStrategyWhenSearchParticularityIsStartWithShouldReturnObjectTypeSearchStartsWith(self):
        searchMethod = self.searchStrategyFactory.createSearchStrategy("starts with")
        expectedClassType = SearchStartsWith
        self.assertIsInstance(searchMethod, expectedClassType)

    def test_creatingSearchStrategyWhenSearchParticularityIsEndsWithShouldReturnObjectTypeSearchEndsWith(self):
        searchMethod = self.searchStrategyFactory.createSearchStrategy("ends with")
        expectedClassType = SearchEndsWith
        self.assertIsInstance(searchMethod, expectedClassType)

    def test_creatingSearchStrategyWhenSearchParticularityIsGreaterThanShouldReturnInstanceOfBetween(self):
        searchMethod = self.searchStrategyFactory.createSearchStrategy("greater than")
        expectedClassType = SearchGreaterThan
        self.assertIsInstance(searchMethod, expectedClassType)

    def test_cratingSearchStrategyWhenSearchParticularityIsLesserThanShouldReturnInstanceOfLessThan(self):
        searchMethod = self.searchStrategyFactory.createSearchStrategy("less than")
        expectedClassType = SearchLessThan
        self.assertIsInstance(searchMethod, expectedClassType)
