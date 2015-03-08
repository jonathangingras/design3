__author__ = 'alex'
import re
import sys


class RegexQuestionAnalyser(object):

    def __init__(self):
        self.listRegexKeyWord = [r"(?<=starts with )(\w+){1}", r"(?<=ends with )(\w+){1}",#begin with key word
                                 r"(?<=including )(.+)+ (and) (\w+){1}", #begin with key word
                                 r"(?<=between )(\d+)+(\.)?(\d+)((\%)|(\w+)+) and ([\S+]+)((\ \w+)+)?", #begin with key word
                                 r"(?<=greater than )(((\d+)(\ )?)+(\w+\/\d+)?)+", #begin with key word
                                 r"((\d+\s)?([A-Z][a-z]+\s(\d+)))", #date
                                 r"((([(\d+\d+)|(\d+)]+\ \d+)|([(\d+\d+)|(\d+)]+\.\d+)) [SENO])", #coord
                                 r"(?<=is the )((\w+\s?){1,2})((?=\.))",
                                 r"(?<=What country has )([A-Z][a-z]+[^d ]\b)",
                                 r"(\.[a-z]+)",#code
                                 r"((\d+[ /.]?\d+[ %]?)((\w+llion)|(sq km)))",
                                 r"(?<= is )(\d+[\s\.]\d+\%?)(?=\.)",
                                 r"((?<=is )([A-Z][a-z]*([\s\,]*))+|(?<= are )([A-Z][a-z]*[\s\,]*([a-z ]+)?)+)", #enum
                                 r"((?<=The )(\w+\s*?){2}(?= is ))"]

        self.registerOfKeyWord = ["starts with", "ends with", "including", "between", "greater than"]

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

    def parseAllRegexKeyWord(self, question):
        indexBegin = 0

        for reg in self.listRegexKeyWord:
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
        for x in self.listString:
            for y in self.listString:
                searchSub = str.find(x,y)
                if searchSub != -1:
                    if(len(x)> len(y)):
                        self.listString.remove(y)
                    #elif (len(x) < len(y)):
                        #self.listString.remove(x)

        for x in self.listString:
            if(self.listString.count(x) > 1):
                self.listString.remove(x)


        print self.listString
        return self.listString


    def searchKeyWord(self, question):
        listkeyWordImportant = []
        for word in self.registerOfKeyWord:
            if question.find(word) != -1:
                listkeyWordImportant.append(word)
        #print listkeyWordImportant
        self.listKeyword = listkeyWordImportant
        return listkeyWordImportant

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

        #print self.listSubject

        return self.listSubject

    def associateWord(self, question):

        if(len(self.listSubject) == 1 and len(self.listString) == 1):
            for subject, key in zip(self.listSubject, self.listString):
                self.dictWord[subject] = key
            #print self.dictWord
            return
        elif len(self.listSubject) < len(self.listString) and len(self.listSubject) == 1:
            self.dictWord[self.listSubject[0]] = self.listString
            #print self.dictWord
            return
        elif(len(self.listSubject) == 2 and len(self.listString) == 2):
            for x in self.listSubject:
                nearestValueDistance = sys.maxint
                nearestValuePosition = 0
                for y in self.listString:
                    valueTemp = abs(question.find(x) - question.find(y))
                    if  valueTemp < nearestValueDistance:
                        nearestValueDistance = valueTemp
                        nearestValuePosition = self.listString.index(y)

                self.dictWord[x] = self.listString[nearestValuePosition]



            print self.dictWord
            return