__author__ = 'alex'
import re
import sys
from naturalLanguagePython.questionLanguageAnalyzer.regexSearchSubject import SearchSubjectInQuestionWithRegex
from naturalLanguagePython.questionLanguageAnalyzer.associateValueToProperKeyWord import AssociateValueToSubject
from naturalLanguagePython.questionLanguageAnalyzer.regexSearchValue import SearchValueWithRegex

class RegexQuestionAnalyzer(object):

    def __init__(self):

        self.registerOfSearchStrategy = ["starts with", "ends with", "including", "between", "greater than", "contains", "less than"]

        self.listString = []
        self.listSubject = []
        self.listKeyword = []
        self.dictWord = {}
        self.associateListOfSubjectWithListOfValue = AssociateValueToSubject()
        self.searchSubjectWithRegex = SearchSubjectInQuestionWithRegex()
        self.searchValueWithRegex = SearchValueWithRegex()



    def __removeDuplicateOfAList(self,listWithRepeatedValue):
        for x in listWithRepeatedValue:
            if (listWithRepeatedValue.count(x) > 1):
                listWithRepeatedValue.remove(x)
        return self.associateListOfSubjectWithListOfValue.splitEnumerationItemInListString(listWithRepeatedValue)

    def __parseAllRegexWord(self):
        self.listString = self.associateListOfSubjectWithListOfValue.removeSubPartOfSameStringOfAList(self.listString)
        self.listString = self.__removeDuplicateOfAList(self.listString)
        return self.listString

    def parseAllRegexValue(self, question):
        self.listString = self.searchValueWithRegex.parseAllRegexValue(question)

        return self.__parseAllRegexWord()

    def searchSubject(self, question):
        self.listSubject = self.searchSubjectWithRegex.searchSubject(question,self.listSubject)

        return self.__removeDuplicateOfAList(self.listSubject)

    def associateWord(self, question,listOfValue, listOfSubject):
        return self.associateListOfSubjectWithListOfValue.associateWordFromTwoListAndReturnIntoDictionary(question,listOfValue,listOfSubject)

    def searchSearchParticularityInQuestion(self, question):
        listKeyWordForSearchParticularity = []
        for word in self.registerOfSearchStrategy:
            if question.find(word) != -1:
                listKeyWordForSearchParticularity.append(word)
        return listKeyWordForSearchParticularity