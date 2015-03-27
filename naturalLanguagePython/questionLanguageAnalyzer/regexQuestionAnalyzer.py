__author__ = 'alex'
import re
import sys
from naturalLanguagePython.questionLanguageAnalyzer.associateValueToProperKeyWord import AssociateValueToSubject

class RegexQuestionAnalyzer(object):

    def __init__(self):

        self.listRegexValueWord = [r"(?<=starts with )([A-Z][a-z]+){1}",
                                 r"(?<=ends with )(\w+){1}",
                                 r"((?<=including )|(?<=include )|(?<= are ))((\d+\.\d+\%?)(\s\w+)* and (\d+\.\d+\%?)(\s\w+)*|(\w+\,\s)+(\w+\,?\s)?and (\w+)|(\w+ and \w+\s?))",
                                 r"((\d+\.\d+\%?)(\s\w+)* and (\d+\.\d+\%?)(\s\w+)*|(\w+\,\s)+(\w+\,?\s)?and (\w+))",
                                 r"(?<=between )(\S?\d+)+(\.)?(\d+)((\%)|(\w+)+) and ((\S?\d+[%.]?)+)((\s\w+)+)?",
                                 r"((?<=greater than )|(?<=less than ))(((\d+)(\ |\.|\%)?)+(\w+\/\d+)?)+",
                                 r"((\d+\s)?([A-Z][a-z]{2,}\s(\d+)))",
                                 r"((([(\d+\d+)|(\d+)]+\ \d+)|([(\d+\d+)|(\d+)]+\.\d+)) [SENW])",
                                 r"(?<=is the )((\w+\s?){1,2})((?=\.))",
                                 r"(\d+\.?\d*\s\w+\/\s?\d+)",
                                 r"(?<=[Ww]hat country has )(([A-Z][a-z]+\s?)?(\w*['-]?\w*\-?)?(\s?[A-Z][a-z]+)?){1,3}(?= as)",
                                 r"(\.[a-z]+)",
                                 r"((?<=including a )|(?<=(?<!(including ))ing\b as a ))(\w+\s?)+",
                                 r"(\d*\.?\d+\%)",
                                 r"(?<= contains )(\w+\s?\-?\'?){1,2}",
                                 r"((\d+[ /.]?\d+[ %]?)((\w+llion)|(sq km)))",
                                 r"(?<= is )(\d+(\s|\.)\d+\%?)(\s[a-z]{1,2})?(\s[A-Z]{1,})?",
                                 r"((?<=is )([A-Z][a-z]*([\s\,]*))+|(?<= are )([A-Z][a-z]*[\s\,]*([a-z ]+)?)+)",
                                 r"((?<=The )(\w+\s*?){2}(?= is ))",
                                 r"((?<=is )(\d+\s\w*?){1,})",
                                 r"((?<=[Mm]y )(?<=.)*?((?= is)|(?= was)|(?= are)|(?= is the))(\s+\w))"]

        self.registerOfSearchStrategy = ["starts with", "ends with", "including", "between", "greater than", "contains", "less than"]

        self.subjectRegex = [r"((?<=[Mm]y )(.*?)((?=\sinclude)|(?= was )|(?= is )|(?= are)|(?= is the)|(?= contains)))",
                             r"((?<=[Mm]y )(\w+){1}(?= \w*\s?starts))",
                             r"(((?<=has\sa[n\s])\s?(\w+\s?){1,3})((?= of )|(?= between )|(?= greater )|(?= including)|(?= \w+ starts)|(?= and )))",
                             r"((?<=its )|(?<= our ))(\w+)",
                             r"(?<=[Ww]hat country has )(([a-z]{3,}[^d ]\b)|(\w+\s?){1,3})(?= including )",
                             r"(?<=[Ww]hat country has a )(.+)(?= of )",
                                r"((?<=[Ww]hat country considers )((\w+\s*?){2})(?= \w+ing as a ))",
                             r"(?<=is the )(.+)(?= of this country)",
                             r"(?<=The )(\w+\s?){1,3}(?= of this country)"]

        self.listString = []
        self.listSubject = []
        self.listKeyword = []
        self.dictWord = {}
        self.assosiateListOfSubjectWithListOfValue = AssociateValueToSubject()

    def __removeSubPartOfSameStringOfAList(self,listStringFromRegex):
        flagRemoveElement = True
        while flagRemoveElement is True:
            flagRemoveElement = False
            for x in listStringFromRegex:
                for y in listStringFromRegex:
                    searchSub = str.find(str(x), str(y))
                    if searchSub != -1:
                        if len(x) > len(y):
                            listStringFromRegex.remove(y)
                            flagRemoveElement = True
        return listStringFromRegex


    def __removeDuplicateOfAList(self,listWithDouble):
        for x in listWithDouble:
            if (listWithDouble.count(x) > 1):
                listWithDouble.remove(x)
        return self.assosiateListOfSubjectWithListOfValue.splitEnumerationItemInListString(listWithDouble)

    def __parseAllRegexWord(self):
        self.listString = self.assosiateListOfSubjectWithListOfValue.removeSubPartOfSameStringOfAList(self.listString)
        self.listString = self.__removeDuplicateOfAList(self.listString)
        return self.listString

    def __addElementsFromListTempIntoListOfKey(self, indexBegin, listTemp):
        for key in listTemp:
            listOfKey = []
            for i in key:
                listOfKey.append(str(i))
            listOfKey = self.__removeSubPartOfSameStringOfAList(listOfKey)
            if self.listString.count(listOfKey[indexBegin]) == 0:
                self.listString.append(listOfKey[indexBegin])

    def parseAllRegexValue(self, question):
        indexBegin = 0
        for reg in self.listRegexValueWord:
            regex = re.compile(reg)
            wordReturn = regex.search(question)
            if wordReturn is not None:
                if self.listString.count(wordReturn) == 0:
                    listTemp = []
                    listTemp = regex.findall(question)

                    if len(listTemp) > 1:
                        self.__addElementsFromListTempIntoListOfKey(indexBegin, listTemp)
                    else:
                        self.listString.append(regex.search(question).group())

        return self.__parseAllRegexWord()

    def __removeSmallestElementAlreadyInsideAnOtherItem(self):
        for x in self.listSubject:
            for y in self.listSubject:
                searchSub = str.find(str(x), str(y))
                if searchSub != -1:
                    if len(x) > len(y):
                        self.listSubject.remove(y)

    def __addElementFromListTempInListSubject(self, indexBegin, listTemp):
        for key in listTemp:
            if self.listSubject.count(key[indexBegin]) == 0:
                self.listSubject.append(key[indexBegin])

    def searchSubject(self, question):
        indexBegin = 0
        for reg in self.subjectRegex:
            regex = re.compile(reg)
            wordReturn = regex.search(question)
            if  wordReturn != None:
                if self.listSubject.count(wordReturn) == 0:
                    listTemp = []
                    listTemp = regex.findall(question)
                    if len(listTemp) > 1:
                        self.__addElementFromListTempInListSubject(indexBegin, listTemp)
                    else:
                        self.listSubject.append(regex.search(question).group())

        self.__removeSmallestElementAlreadyInsideAnOtherItem()

        return self.__removeDuplicateOfAList(self.listSubject)

    def associateWord(self, question,listOfValue, listOfSubject):
        return self.assosiateListOfSubjectWithListOfValue.associateWordFromTwoListAndReturnIntoDictionary(question,listOfValue,listOfSubject)

    def searchSearchParticularityInQuestion(self, question):
        listKeyWordForSearchParticularity = []
        for word in self.registerOfSearchStrategy:
            if question.find(word) != -1:
                listKeyWordForSearchParticularity.append(word)
        return listKeyWordForSearchParticularity