__author__ = 'alex'
from naturalLanguagePython.questionLanguageAnalyzer.processLanguage import ProcessLanguage
from naturalLanguagePython.questionLanguageAnalyzer.regexQuestionAnalyzer import RegexQuestionAnalyzer
import regexQuestionAnalyzer


class QuestionInformationAnalyser(object):

    def __init__(self):
        self.regexAnalyser = RegexQuestionAnalyzer()
        self.processLanguage = ProcessLanguage()
        self.questionDictionary = {}

    def analyseQuestion(self, question):
        listimportante = self.regexAnalyser.parseAllRegexKeyWord(question)
        self.regexAnalyser.searchKeyword(question)
        wordSubject = self.regexAnalyser.searchSubject(question)
        if len(listimportante) == 0 and len(wordSubject) == 0:
            self.questionDictionary = self.processLanguage.buildDictionaries()
            print "utilisation Complete de NLTK"
        elif len(listimportante) != 0 and len(wordSubject) == 0:
            print "utilisation partielle de nltk pour le sujet"
            self.processLanguage.tokenizeQuestion(question)
            self.processLanguage.taggingQuestion()
            listSubject = self.processLanguage.extractOnlyQuestionSubject()
            if len(listSubject) == 1 and len(listimportante) == 1:
                self.questionDictionary[listSubject.pop()] = listimportante.pop()
            for x in listSubject:
                self.questionDictionary[x] = listimportante
        else:
            self.regexAnalyser.associateWord(question)
            self.questionDictionary = self.regexAnalyser.dictWord

            print "aucune utilisation de nltk"