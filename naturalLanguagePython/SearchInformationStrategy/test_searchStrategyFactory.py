from unittest import TestCase

__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.searchInformationStrategy.searchStartsWith import SearchStartsWith
from naturalLanguagePython.searchInformationStrategy.searchEndsWith import SearchEndsWith

class TestSearchStrategyFactory(TestCase):
    def setUp(self):
        self.searchStrategyFactory = SearchStrategyFactory()

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

