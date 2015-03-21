from unittest import TestCase
from naturalLanguagePython.countryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains

__author__ = 'Antoine'


class TestSearchStrategyServiceFactory(TestCase):

    def setUp(self):
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()

    def test_validateNumbersOfWantedSearchStrategyWhenHavingNoneDefinedStrategyShouldReturnAListOfEqualNumbersOfStrategyToTheDictionary(self):
        expectedReturnedStrategyList = ['Contains']
        dictionary = {"Capital": ["Ottawa"]}
        self.assertEqual(expectedReturnedStrategyList, self.searchStrategyServiceFactory.wantedSearchStrategyValidator(dictionary))

    def test_validateNumbersOfWantedSearchStrategyWhenHavingOneDefinedStrategyShouldReturnTheSameList(self):
        expectedReturnedStrategyList = ['Contains']
        strategyList = ['Contains']
        dictionary = {"Capital": ["Ottawa"]}
        self.assertEqual(expectedReturnedStrategyList, self.searchStrategyServiceFactory.wantedSearchStrategyValidator(dictionary, strategyList))

    def test_createASearchStrategyFromNoneSearchStrategyShouldCreateTheRightStrategy(self):
        self.assertIsInstance(self.searchStrategyServiceFactory.createStrategy(None), SearchContains)

    def test_createASearchStrategyFromContainsSearchStrategyServiceFactoryShouldCreateTheRightStrategy(self):
        self.assertIsInstance(self.searchStrategyServiceFactory.createStrategy('Contains'), SearchContains)