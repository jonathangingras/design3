__author__ = 'alex'
import re
import sys


class RegexQuestionAnalyzer(object):

    def __init__(self):
        self.listRegexKeyword = [r"(?<=starts with )(\w+){1}", r"(?<=ends with )(\w+){1}",
                                 r"((((?<=including )|(?<=include )|(?<= are ))(.+) and (((\s?\w+\s?)|(\d?\.\d\%)?)){1,4}))",
                                 r"(?<=between )(\d+)+(\.)?(\d+)((\%)|(\w+)+) and ((\d+[\%\.]?)+)((\ \w+)+)?",
                                 r"((?<=greater than )|(?<=less than ))(((\d+)(\ |\.|\%)?)+(\w+\/\d+)?)+",
                                 r"((\d+\s)?([A-Z][a-z]+\s(\d+)))",
                                 r"((([(\d+\d+)|(\d+)]+\ \d+)|([(\d+\d+)|(\d+)]+\.\d+)) [SENW])",
                                 r"(?<=is the )((\w+\s?){1,2})((?=\.))",
                                 r"(?<=What country has )([A-Z][a-z]+[^d ]\b)",
                                 r"(\.[a-z]+)",
                                 r"((\d+[ /.]?\d+[ %]?)((\w+llion)|(sq km)))",
                                 r"(?<= is )(\d+(\s|\.)\d+\%?)(\s[a-z]{1,2})?(\s[A-Z]{1,})?",
                                 r"((?<=is )([A-Z][a-z]*([\s\,]*))+|(?<= are )([A-Z][a-z]*[\s\,]*([a-z ]+)?)+)",
                                 r"((?<=The )(\w+\s*?){2}(?= is ))",
                                 r"((?<=is )(\d+\s+\w*?){1,})",
                                 r"((?<=[Mm]y )(?<=.)*?((?= is)|(?= was)|(?= are)|(?= is the))(\s+\w))"]
        self.registerOfKeyword = ["starts with", "ends with", "including", "between", "greater than", "contains", "less than"]

        self.subjectRegex = [r"((?<=[Mm]y )(.*?)((?=\sinclude)|(?= was )|(?= is )|(?= are)|(?= is the)))",
                             r"((?<=[Mm]y )(\w+){1}(?= \w*\s?starts))",
                             r"(((?<=has\sa[n\s])\s?(\w+\s?){1,3})((?= of )|(?= between )|(?= greater )|(?= including)|(?= \w+ starts)|(?= and )))",
                             r"(?<=its )(\w+)",
                             r"(?<=What country has )([a-z]{3,}[^d ]\b)(?= including )",
                             r"(?<=What country has a )(.+)(?= of )",
                             r"(?<=is the )(.+)(?= of this country)",
                             r"(?<=The )(\w+\s?){1,3}(?= of this country)"]

        self.listString = []
        self.listSubject = []
        self.listKeyword = []
        self.dictWord = {}

    def __removeSubPartOfSameStringOfAList(self,listStringfromRegex):
        flagRemoveElement = 1
        while (flagRemoveElement == 1):
            flagRemoveElement = 0
            for x in listStringfromRegex:
                for y in listStringfromRegex:
                    searchSub = str.find(x, y)
                    if searchSub != -1:
                        if (len(x) > len(y)):
                            listStringfromRegex.remove(y)
                            flagRemoveElement = 1
        return listStringfromRegex


    def __parseAllRegexWord(self):
        self.listString = self.__removeSubPartOfSameStringOfAList(self.listString)
        for x in self.listString:
            if (self.listString.count(x) > 1):
                self.listString.remove(x)
        self.__splitEnumerationItemInListString()
        return self.listString



    def parseAllRegexKeyWord(self, question):
        indexBegin = 0


        for reg in self.listRegexKeyword:
            regex = re.compile(reg)
            wordReturn = regex.search(question)
            if  wordReturn != None:
                if self.listString.count(wordReturn) == False:
                    listTemp = []
                    listTemp = regex.findall(question)
                    if len(listTemp) > 1:
                        for key in listTemp:
                            listOfKey = []
                            for i in key:
                                listOfKey.append(str(i))

                            listOfKey = self.__removeSubPartOfSameStringOfAList(listOfKey)
                            if self.listString.count(listOfKey[indexBegin]) == False:
                                self.listString.append(listOfKey[indexBegin])
                    else:

                        self.listString.append(regex.search(question).group())
        return self.__parseAllRegexWord()


    def searchSubject(self, question):
        indexBegin = 0
        for reg in self.subjectRegex:
            regex = re.compile(reg)
            wordReturn = regex.search(question)
            if  wordReturn != None:
                if self.listSubject.count(wordReturn) == False:
                    listTemp = []
                    listTemp = regex.findall(question)
                    if len(listTemp) > 1:

                        for key in listTemp:
                            if self.listSubject.count(key[indexBegin]) == 0:
                                self.listSubject.append(key[indexBegin])
                    else:

                        self.listSubject.append(regex.search(question).group())


        for x in self.listSubject:
            for y in self.listSubject:
                searchSub = str.find(x,y)
                if searchSub != -1:
                    if(len(x)> len(y)):
                        self.listSubject.remove(y)

        for x in self.listSubject:
            if(self.listSubject.count(x) > 1):
                self.listSubject.remove(x)
        return self.listSubject

    def searchKeyword(self, question):
        for word in self.registerOfKeyword:
            if question.find(word) != -1:
                self.listKeyword.append(word)
        return self.listKeyword


    def __splitEnumerationItemInListString(self):
        futurList = []
        for item in self.listString:
            listTemp = str(item).replace(' and ', ',').split(',')
            for temp in listTemp:
                temp.strip(' ')
                if (temp != ''):
                    temp.rstrip(' ')
                    futurList.append(temp.lstrip(' '))
        self.listString = futurList

    def associateWord(self, question):
        listTemp =[]
        self.__splitEnumerationItemInListString()

        if(len(self.listSubject) == 1 and len(self.listString) == 1):
            for subject, key in zip(self.listSubject, self.listString):
                self.dictWord[subject] = [key]
        elif len(self.listSubject) < len(self.listString) and len(self.listSubject) == 1:
            self.dictWord[str(self.listSubject[0]).strip(' ')] = self.listString
        elif(len(self.listSubject) >= 2 and len(self.listString) >= 2 and len(self.listString) == len(self.listSubject)):
            for x in self.listSubject:
                nearestValueDistance = sys.maxint
                nearestValuePosition = 0
                for y in self.listString:
                    valueTemp = abs(question.find(x) - question.find(y))
                    if  valueTemp < nearestValueDistance:
                        nearestValueDistance = valueTemp
                        nearestValuePosition = self.listString.index(y)

                self.dictWord[x] = [self.listString[nearestValuePosition]]