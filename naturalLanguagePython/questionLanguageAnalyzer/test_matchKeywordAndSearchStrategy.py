from unittest import TestCase
from naturalLanguagePython.questionLanguageAnalyzer.matchKeywordAndSearchStrategy import MatchKeywordAndSearchStrategy
__author__ = 'Antoine'


class TestMatchKeywordAndSearchStrategy(TestCase):

    def setUp(self):
        self.matchKeywordAndSearchStrategy = MatchKeywordAndSearchStrategy()

    def test_matchingSearchStrategyAndKeywordWhenHavingStartsWithSearchStrategyShouldReturnStartsWithWithCapitalKeyword(self):
        question = "this question is irrelevant"
        expectedSearchStrategyByKeyword = {"capital": ["starts with"]}
        informationDictionary = {"capital": "a capital"}
        extractedSearchStrategy = ["starts with"]
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy))

    def test_matchingSearchStrategyAndKeywordWhenHavingEndsWithStrategyShouldReturnEndsWithLinkedToCapitalKeyword(self):
        question = "this question is irrelevant"
        expectedSearchStrategyByKeyword = {"capital": ["ends with"]}
        informationDictionary = {"capital": "a capital"}
        extractedSearchStrategy = ["ends with"]
        self.assertEqual(expectedSearchStrategyByKeyword, self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, informationDictionary, extractedSearchStrategy
        ))

    def test_matchingSearchStrategyAndKeywordWhenHavingStartsWithAndEndsWithShouldReturnBothLinkedToCapitalKeyword(self):
        question = "this question is still irrelevant"
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
