from unittest import TestCase
from naturalLanguagePython.questionLanguageAnalyzer.regexQuestionAnalyzer import RegexQuestionAnalyzer
__author__ = 'Antoine'


class TestRegexQuestionAnalyser(TestCase):
    def setUp(self):
        self.regexQuestionAnalyzer = RegexQuestionAnalyzer()
    def test_extractStrategyWhenHavingNoSpecifiedStrategyInQuestionShouldReturnEmptyList(self):
        question = "My unemployment rate is 40.6%."
        expectedStrategyList = []
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchKeyword(question))

    def test_extractStrategyWhenHavingStartsWithKeywordMentionedShouldReturnListWithStartsWith(self):
        question = "My capital name starts with Moga."
        expectedStrategyList = ['starts with']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchKeyword(question))

    def test_extractStrategyWhenHavingEndsWithKeywordMentionedShouldReturnListWithEndsWith(self):
        question = "My capital name ends with ens."
        expectedStrategyList = ['ends with']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchKeyword(question))

    def test_extractStrategyWhenHavingContainsStrategyMentionedShouldReturnListContains(self):
        question = "The major urban areas of this country contains Santiago, Valparaiso and Concepcion."
        expectedStrategyList = ['contains']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchKeyword(question))

    def test_extractStrategyWhenHavingGreaterThanStrategyMentionedShouldReturnListWithGreaterThan(self):
        question = "What country has a population growth rate of greater than 1.46%?"
        expectedStrategyList = ['greater than']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchKeyword(question))

    def test_extractStrategyWhenHavingLessThanStrategyMentionedShouldReturnListWithLessThan(self):
        question = "What country has a population growth rate of less than 1.46%?"
        expectedStrategyList = ['less than']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchKeyword(question))

