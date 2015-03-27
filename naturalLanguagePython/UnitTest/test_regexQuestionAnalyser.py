import unittest
from naturalLanguagePython.questionLanguageAnalyzer.regexQuestionAnalyzer import RegexQuestionAnalyzer


__author__ = 'Antoine'




class TestRegexQuestionAnalyser(unittest.TestCase):
    def setUp(self):
        self.regexQuestionAnalyzer = RegexQuestionAnalyzer()


    def test_extractStrategyWhenHavingNoSpecifiedStrategyInQuestionShouldReturnEmptyList(self):
        question = "My unemployment rate is 40.6%."
        expectedStrategyList = []
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchSearchParticularityInQuestion(question))

    def test_extractStrategyWhenHavingStartsWithKeywordMentionedShouldReturnListWithStartsWith(self):
        question = "My capital name starts with Moga."
        expectedStrategyList = ['starts with']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchSearchParticularityInQuestion(question))

    def test_extractStrategyWhenHavingEndsWithKeywordMentionedShouldReturnListWithEndsWith(self):
        question = "My capital name ends with ens."
        expectedStrategyList = ['ends with']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchSearchParticularityInQuestion(question))

    def test_extractStrategyWhenHavingContainsStrategyMentionedShouldReturnListContains(self):
        question = "The major urban areas of this country contains Santiago, Valparaiso and Concepcion."
        expectedStrategyList = ['contains']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchSearchParticularityInQuestion(question))

    def test_extractStrategyWhenHavingGreaterThanStrategyMentionedShouldReturnListWithGreaterThan(self):
        question = "What country has a population growth rate of greater than 1.46%?"
        expectedStrategyList = ['greater than']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchSearchParticularityInQuestion(question))

    def test_extractStrategyWhenHavingLessThanStrategyMentionedShouldReturnListWithLessThan(self):
        question = "What country has a population growth rate of less than 1.46%?"
        expectedStrategyList = ['less than']
        self.assertEqual(expectedStrategyList, self.regexQuestionAnalyzer.searchSearchParticularityInQuestion(question))

    def test_parseAllRegexKeywordWhenHavingAnEmptyQuestionShouldReturnAnEmptyList(self):
        question = ""
        expectedRegexKeywordList = []
        self.assertEqual(expectedRegexKeywordList, self.regexQuestionAnalyzer.parseAllRegexValue(question))

    def test_parseAllRegexKeywordWhenHavingOnlyOneInformationInQuestionShouldReturnCorrectList(self):
        question = "My capital name starts with Moga."
        expectedRegexKeywordList = ["Moga"]
        self.assertEqual(expectedRegexKeywordList, self.regexQuestionAnalyzer.parseAllRegexValue(question))

    def test_parseAllRegexKeywordWhenHavingTwoInformationInQuestionShouldReturnCorrectList(self):
        question = "My capital name starts with Ath and ends with ens."
        expectedRegexKeywordList = ["Ath", "ens"]
        self.assertEqual(expectedRegexKeywordList, self.regexQuestionAnalyzer.parseAllRegexValue(question))

    def test_parseAllRegexKeywordWhenHavingThreeInformationInQuestionShouldReturnCorrectList(self):
        question = "The lotus blossom is the national symbol of this country , my internet code is .br and, my capital is Bruxelle"
        expectedRegexKeywordList =[".br", "Bruxelle", "lotus blossom"]
        self.assertEqual(expectedRegexKeywordList, self.regexQuestionAnalyzer.parseAllRegexValue(question))

    def test_removeDoubleInformationFetchedBySubjectRegexList(self):
        question = "My capital name starts with Ath."
        self.regexQuestionAnalyzer.listString = ["Ath"]
        self.regexQuestionAnalyzer.listSubject = ["capital name", "capital"]
        expectedDict = {}
        expectedDict["capital name"] = ["Ath"]
        dictAssociateWordDone = self.regexQuestionAnalyzer.associateWord(question,self.regexQuestionAnalyzer.listString,self.regexQuestionAnalyzer.listSubject)
        self.assertEqual(dictAssociateWordDone,expectedDict)

    def test_assignAllValueToOneSubject(self):
        question = "My latitude is 16 00 S and my longitude is 167 00 E and my export partners are US, Germany, UK, France, Spain, Canada and Italy."
        self.regexQuestionAnalyzer.parseAllRegexValue(question)
        self.regexQuestionAnalyzer.searchSubject(question)
        # self.regexQuestionAnalyzer.associateWord(question)
        expectedDict = {}
        expectedDict["latitude"] = ["16 00 S"]
        expectedDict["longitude"] = ["167 00 E"]
        expectedDict["export partners"] = ["US", "Germany", "UK", "France", "Spain", "Canada", "Italy"]

        dictAssociateWordDone = self.regexQuestionAnalyzer.associateWord(question,self.regexQuestionAnalyzer.listString,self.regexQuestionAnalyzer.listSubject)
        self.assertEqual(dictAssociateWordDone,expectedDict)

