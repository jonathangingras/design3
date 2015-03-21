__author__ = 'alex'
from naturalLanguagePython.questionLanguageAnalyzer.matchKeywordAndSearchStrategy import MatchKeywordAndSearchStrategy
from naturalLanguagePython.questionLanguageAnalyzer.processLanguage import ProcessLanguage
from naturalLanguagePython.questionLanguageAnalyzer.regexQuestionAnalyzer import RegexQuestionAnalyzer


class QuestionInformationAnalyser(object):

    def __init__(self):
        self.regexAnalyser = RegexQuestionAnalyzer()
        self.processLanguage = ProcessLanguage()
        self.matchKeywordAndSearchStrategy = MatchKeywordAndSearchStrategy()
        self.questionDictionary = {}

    def analyseQuestionParticularity(self, question):
        questionParticularity = self.regexAnalyser.searchKeyword(question)
        return questionParticularity

    def linkSearchStrategyToKeywordRelatedToQuestion(self, question, dictionary, questionSearchParticularity):
        return self.matchKeywordAndSearchStrategy.matchSearchStrategyByKeyword(
            question, dictionary, questionSearchParticularity
        )

    def analyseQuestion(self, question):
        keywordList = self.regexAnalyser.parseAllRegexKeyWord(question)
        wordSubject = self.regexAnalyser.searchSubject(question)
        # print keywordList
        # print wordSubject


        if len(keywordList) == 0 and len(wordSubject) == 0:
            self.questionDictionary = self.processLanguage.buildDictionaries()

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
        if len(listSubject) == 1 and len(keywordlist) == 1:
            self.questionDictionary[listSubject.pop()] = keywordlist
        else:
            for x in listSubject:
                self.questionDictionary[x] = keywordlist


    def __analyseQuestionValue(self,question,wordSubject):
        self.__taggingQuestionWithNltk(question)
        listValue = self.processLanguage.extractOnlyQuestionValue()

        if len(wordSubject) == 1 and len(listValue) == 1:
            self.questionDictionary[wordSubject.pop()] = listValue
        else:
            for x in wordSubject:
                self.questionDictionary[x] = listValue


    def __taggingQuestionWithNltk(self, question):
        self.processLanguage.tokenizeQuestion(question)
        self.processLanguage.taggingQuestion()




