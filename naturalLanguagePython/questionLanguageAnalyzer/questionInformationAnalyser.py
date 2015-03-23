__author__ = 'alex'
from naturalLanguagePython.questionLanguageAnalyzer.processLanguage import ProcessLanguage
from naturalLanguagePython.questionLanguageAnalyzer.regexQuestionAnalyzer import RegexQuestionAnalyzer
import regexQuestionAnalyzer
from sys import maxint


class QuestionInformationAnalyser(object):

    def __init__(self):
        self.regexAnalyser = RegexQuestionAnalyzer()
        self.processLanguage = ProcessLanguage()
        self.questionDictionary = {}

    def analyseQuestionParticularity(self, question):
        questionParticularity = self.regexAnalyser.searchKeyword(question)
        return questionParticularity

    def analyseQuestion(self, question):
        keywordList = self.regexAnalyser.parseAllRegexKeyWord(question)
        wordSubject = self.regexAnalyser.searchSubject(question)
        print "regex keyword"
        print keywordList
        print wordSubject


        if len(keywordList) == 0 and len(wordSubject) == 0:

            self.__taggingQuestionWithNltk(question)
            self.questionDictionary = self.processLanguage.buildDictionaries(question)

        elif len(keywordList) != 0 and len(wordSubject) == 0:
            self.__analyseQuestionSubject(question,keywordList)
        elif len(keywordList) == 0 and len(wordSubject) != 0:
            self.__analyseQuestionValue(question,wordSubject)


        else:

            self.regexAnalyser.associateWord(question)
            self.questionDictionary = self.regexAnalyser.dictWord
        return self.questionDictionary

    def __analyseQuestionSubject(self,question,keywordlist):
        self.__taggingQuestionWithNltk(question)
        listSubject = self.processLanguage.extractOnlyQuestionSubject()
        self.__buildADictionnaryWithProperKeyAndValue(keywordlist, listSubject,question)


    def __splitEnumerationItemInListString(self,listString):
        futurList = []
        for item in listString:
            listTemp = str(item).replace(' and ', ',').split(',')
            for temp in listTemp:
                temp.strip(' ')
                if (temp != ''):
                    temp.rstrip(' ')
                    futurList.append(temp.lstrip(' '))
        return futurList




    def __buildADictionnaryWithProperKeyAndValue(self, listValue, wordSubject, question):
        if len(wordSubject) == 1 and len(listValue) == 1:
            self.questionDictionary[wordSubject.pop()] = listValue
        else:
            for x in wordSubject:
                self.questionDictionary[x] = listValue
        listValue = self.__splitEnumerationItemInListString(listValue)
        print listValue

        if(len(listValue) == 1 and len(listValue) == 1):
            for subject, key in zip(wordSubject, listValue):
                self.questionDictionary[subject] = [key]
        elif len(wordSubject) < len(listValue) and len(wordSubject) == 1:
            self.questionDictionary[str(wordSubject[0]).strip(' ')] = listValue
        elif(len(wordSubject) >= 2 and len(listValue) >= 2 and len(listValue) == len(wordSubject)):
            for x in wordSubject:
                nearestValueDistance = maxint
                nearestValuePosition = 0
                for y in listValue:
                    valueTemp = abs(question.find(x) - question.find(y))
                    if  valueTemp < nearestValueDistance:
                        nearestValueDistance = valueTemp
                        nearestValuePosition = listValue.index(y)

                self.questionDictionary[x] = [listValue.pop(nearestValuePosition)]

    def __analyseQuestionValue(self,question,wordSubject):
        self.__taggingQuestionWithNltk(question)
        listValue = self.processLanguage.extractOnlyQuestionValue()

        self.__buildADictionnaryWithProperKeyAndValue(listValue, wordSubject, question)


    def __taggingQuestionWithNltk(self, question):
        self.processLanguage.tokenizeQuestion(question)
        self.processLanguage.taggingQuestion()




