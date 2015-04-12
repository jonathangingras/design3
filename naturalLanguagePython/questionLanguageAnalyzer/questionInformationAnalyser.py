__author__ = 'alex'
from naturalLanguagePython.questionLanguageAnalyzer.matchKeywordAndSearchStrategy import MatchKeywordAndSearchStrategy
from naturalLanguagePython.questionLanguageAnalyzer.processLanguage import ProcessLanguage
from naturalLanguagePython.questionLanguageAnalyzer.regexQuestionAnalyzer import RegexQuestionAnalyzer
from naturalLanguagePython.questionLanguageAnalyzer.associateValueToProperKeyWord import AssociateValueToSubject
import regexQuestionAnalyzer

from sys import maxint


class QuestionInformationAnalyser(object):

    def __init__(self):
        self.regexAnalyser = RegexQuestionAnalyzer()
        self.processLanguage = ProcessLanguage()
        self.matchKeywordAndSearchStrategy = MatchKeywordAndSearchStrategy()
        self.associateListOfSubjectWithListOfValueInDict = AssociateValueToSubject()
        self.questionDictionary = {}

    def analyseQuestionParticularity(self, question):
        questionParticularity = self.regexAnalyser.searchSearchParticularityInQuestion(question)
        return questionParticularity

    def linkSearchStrategyToKeywordRelatedToQuestion(self, question, dictionary, questionSearchParticularity):
        return self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, dictionary, questionSearchParticularity
        )

    def analyseQuestion(self, question):
        keywordList = self.regexAnalyser.parseAllRegexValue(question)
        wordSubject = self.regexAnalyser.searchSubject(question)

        if len(keywordList) == 0 and len(wordSubject) == 0:
            self.__taggingQuestionWithNltk(question)
            self.questionDictionary = self.processLanguage.buildDictionaries(question)

        elif len(keywordList) != 0 and len(wordSubject) == 0:
            self.__analyseQuestionSubject(question,keywordList)

        elif len(keywordList) == 0 and len(wordSubject) != 0:
            self.__analyseQuestionValue(question,wordSubject)

        else:
            self.questionDictionary = self.regexAnalyser.associateWord(question,keywordList,wordSubject)
        return self.questionDictionary

    def __analyseQuestionSubject(self,question,keywordlist):
        self.__taggingQuestionWithNltk(question)
        listSubject = self.processLanguage.extractOnlyQuestionSubject()
        self.__buildADictionaryWithProperKeyAndValue(keywordlist, listSubject,question)

    def __buildADictionaryWithProperKeyAndValue(self, listValue, wordSubject, question):
        self.questionDictionary = self.associateListOfSubjectWithListOfValueInDict.associateWordFromTwoListAndReturnIntoDictionary(
            question,listValue,wordSubject)

    def __analyseQuestionValue(self,question,wordSubject):
        self.__taggingQuestionWithNltk(question)
        listValue = self.processLanguage.extractOnlyQuestionValue()

        self.__buildADictionaryWithProperKeyAndValue(listValue, wordSubject, question)

    def __taggingQuestionWithNltk(self, question):
        self.processLanguage.tokenizeQuestion(question)
        self.processLanguage.taggingQuestion()
