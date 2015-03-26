from unittest import TestCase
from naturalLanguagePython.countryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains

__author__ = 'Antoine'


class TestSearchStrategyServiceFactory(TestCase):

    def setUp(self):
        self.searchStrategyServiceFactory = SearchStrategyServiceFactory()

    def test_validateNumbersOfWantedSearchStrategyWhenHavingNoneDefinedStrategyShouldReturnAListOfEqualNumbersOfStrategyToTheDictionary(self):
        expectedSearchStrategyDictionary = {"Capital": ["Contains"]}
        dictionary = {"Capital": ["Ottawa"]}
        self.assertEqual(expectedSearchStrategyDictionary,
                         self.searchStrategyServiceFactory.wantedSearchStrategyValidator(dictionary))

    def test_validateNumbersOfWantedSearchStrategyWhenHavingOneDefinedStrategyShouldReturnTheSameList(self):
        expectedSearchStrategyDictionary = {"Capital": ["Contains"]}
        searchStrategyDictionary = {"Capital": ['Contains']}
        dictionary = {"Capital": ["Ottawa"]}
        self.assertEqual(expectedSearchStrategyDictionary,
                         self.searchStrategyServiceFactory.wantedSearchStrategyValidator(dictionary, searchStrategyDictionary))
