__author__ = 'alex'
import re
import sys


class RegexQuestionAnalyzer(object):

    def __init__(self):
        self.listRegexKeyword = [r"(?<=starts with )(\w+){1}", r"(?<=ends with )(\w+){1}",
                                 r"((((?<=including )|(?<=include )|(?<= are ))(.+) and (((\s?\w+\s?)|(\d?\.\d\%)?)){1,4}))",
                                 r"(?<=between )(\d+)+(\.)?(\d+)((\%)|(\w+)+) and ([\S+]+)((\ \w+)+)?",
                                 r"(?<=greater than )(((\d+)(\ )?)+(\w+\/\d+)?)+",
                                 r"((\d+\s)?([A-Z][a-z]+\s(\d+)))",
                                 r"((([(\d+\d+)|(\d+)]+\ \d+)|([(\d+\d+)|(\d+)]+\.\d+)) [SENO])",
                                 r"(?<=is the )((\w+\s?){1,2})((?=\.))",
                                 r"(?<=What country has )([A-Z][a-z]+[^d ]\b)",
                                 r"(\.[a-z]+)",
                                 r"((\d+[ /.]?\d+[ %]?)((\w+llion)|(sq km)))",
                                 r"(?<= is )(\d+[\s\.]\d+\%?)(?=\.)",
                                 r"((?<=is )([A-Z][a-z]*([\s\,]*))+|(?<= are )([A-Z][a-z]*[\s\,]*([a-z ]+)?)+)",
                                 r"((?<=The )(\w+\s*?){2}(?= is ))",
                                 r"((?<=is )(\d+\s+\w*?){1,})",
                                 r"((?<=[Mm]y )(?<=.)*?((?= is)|(?= was)|(?= are)|(?= is the))(\s+\w))"]
        self.registerOfKeyword = ["starts with", "ends with", "including", "between", "greater than", "contains", "less than"]

        self.subjectRegex = [r"((?<=[Mm]y )(.)*?((?= is)|(?= was)|(?= are)))",
                             r"((?<=[Mm]y )(\w+\s?){1,2}(?= starts))",
                             r"((?<=has\sa\s)(\w+))",
                             r"(?<=its )(\w+)",
                             r"(?<=What country has )([a-z]+[^d ]\b)",
                             r"(?<=What country has a )(.+)(?= of )",
                             r"(?<=is the )(.+)(?= of this country)"]

        self.listString = []
        self.listSubject = []
        self.listKeyword = []
        self.dictWord = {}

    def __parseAllRegexWord(self):
        print self.listString
        for x in self.listString:
            for y in self.listString:
                searchSub = str.find(x, y)
                if searchSub != -1:
                    if (len(x) > len(y)):
                        self.listString.remove(y)
        for x in self.listString:
            if (self.listString.count(x) > 1):
                self.listString.remove(x)

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
                            if self.listString.count(key[indexBegin]) == False:
                                self.listString.append(key[indexBegin])
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


 # def __splitString(self):
    #     listTemp =[]
    #     futurList = []
    #     for item in self.listString:
    #         listTemp = str(item).replace('and ','').split(',')
    #         for temp in listTemp:
    #             futurList.append(temp)
    #     self.listString = futurList
    #     print futurList

    def associateWord(self, question):
        listTemp =[]
        futurList = []
        for item in self.listString:
            listTemp = str(item).replace(' and ',',').split(',')
            for temp in listTemp:
                temp.strip(' ')
                if(temp != ''):
                    futurList.append(temp)
        self.listString = futurList
        if(len(self.listSubject) == 1 and len(self.listString) == 1):
            for subject, key in zip(self.listSubject, self.listString):
                self.dictWord[subject] = [key]
        elif len(self.listSubject) < len(self.listString) and len(self.listSubject) == 1:
            self.dictWord[self.listSubject[0]] = self.listString
        elif(len(self.listSubject) >= 2 and len(self.listString) >= 2 and len(self.listString) == len(self.listSubject)):
            for x in self.listSubject:
                nearestValueDistance = sys.maxint
                nearestValuePosition = 0
                for y in self.listString:
                    valueTemp = abs(question.find(x) - question.find(y))
                    if  valueTemp < nearestValueDistance:
                        nearestValueDistance = valueTemp
                        nearestValuePosition = self.listString.index(y)

                self.dictWord[x] = self.listString[nearestValuePosition]