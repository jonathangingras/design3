from unittest import TestCase
from naturalLanguagePython.questionLanguageAnalyzer.matchKeywordAndSearchStrategy import MatchKeywordAndSearchStrategy
__author__ = 'Antoine'


class TestMatchKeywordAndSearchStrategy(TestCase):

    def setUp(self):
        self.matchKeywordAndSearchStrategy = MatchKeywordAndSearchStrategy()

    def test_matchingSearchStrategyAndKeywordWhenHavingStartsWithSearchStrategyShouldReturnStartsWithWithCapitalKeyword(self):
        question = "My capital name starts with Moga."
        expectedSearchStrategyByKeyword = {"capital": ["starts with"]}
        informationDictionary = {"capital": "a capital"}
        extractedSearchStrategy = ["starts with"]
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy))

    def test_matchingSearchStrategyAndKeywordWhenHavingEndsWithStrategyShouldReturnEndsWithLinkedToCapitalKeyword(self):
        question = "My capital name ends with Moga."
        expectedSearchStrategyByKeyword = {"capital": ["ends with"]}
        informationDictionary = {"capital": "a capital"}
        extractedSearchStrategy = ["ends with"]
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy
        ))

    def test_matchingSearchStrategyAndKeywordWhenHavingStartsWithAndEndsWithShouldReturnBothLinkedToCapitalKeyword(self):
        question = "My capital name starts with Ath and ends with ens."
        expectedSearchStrategyByKeyword = {"capital": ["starts with", "ends with"]}
        informationDictionary = {"capital": "a capital"}
        extractedSearchStrategy = ["starts with", "ends with"]
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy
        ))

    def test_matchingSearchStrategyAndKeywordWhenCapitalKeywordButNotCorrespondingSearchStrategyShouldReturnCapitalWithEmptyList(self):
        question = "this question is still irrelevant"
        expectedSearchStrategyByKeyword = {"capital": []}
        informationDictionary = {"capital": "A capital"}
        extractedSearchStrategy = []
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy
        ))
    def test_matchingSearchStrategyAndKeywordWhenHavingLessThanKeywordShouldReturnLessThanLinkedToTheCorrespondingKeyword(self):
        question = "What country has a population less than 1 300 692 576?"
        expectedSearchStrategyByKeyword = {"population": ["less than"]}
        informationDictionary = {"population": ["1 300 692 576"]}
        extractedSearchStrategy = ["less than"]
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy
        ))

    def test_matchingSearchStrategyAndKeywordWhenHavingGreaterThanShouldReturnGreaterThanLinkedToTheCorrespondingKeyword(self):
        question = "My death rate is greater than 15 death/1000"
        expectedSearchStrategyByKeyword = {"death rate" : ["greater than"]}
        informationDictionary = {"death rate": ["15 death/1000"]}
        extractedSearchStrategy = ["greater than"]
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy
        ))

    def test_matchingSearchStrategyAndKeywordWhenHavingTwoStrategyLinkedToTheSameKeywordShouldReturnBothOfThemInKeywordList(self):
        question = "The death rate of this country is greater than 10.37 deaths/1000 population and less than 10.40 deaths/1000 population."
        expectedSearchStrategyByKeyword = {"death rate": ["greater than", "less than"]}
        informationDictionary = {"death rate": ["10.37 deaths/1000", "10.40 deaths/1000"]}
        extractedSearchStrategy = ["greater than", "less than"]
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy
        ))