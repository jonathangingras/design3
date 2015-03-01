__author__ = 'alex'

import nltk
import re
import time
import timex
from nltk.stem.snowball import SnowballStemmer

from nltk.corpus import brown


sentence = "22 September 1960 is the date of independence of this country."
myFile = open('questionsList1.txt', 'r')
sentencesList = myFile.readlines()

tokens = nltk.sent_tokenize(sentence)

stemmer = SnowballStemmer("english")
stemmed_tokens = [stemmer.stem(t) for t in tokens]

 #freqs = nltk.FreqDist([w.lower() for w in brown.words()])
                #wordlist_sorted = sorted(self.importantWordList, key=lambda x: freqs[x.lower()], reverse=True)
                #self.importantWordList = wordlist_sorted (NN[S]?)+


class processLanguage():
    def __init__(self, questionString):
        self.question = questionString
        self.chunkGram = r"""ChunkNumber: {<\w+>?<CD>+<NN>?<\w+>?}
                                          }<CC>|<VB\w?>| <IN> | <JJ>{

                             ChunkSubject:  {<JJ>?<NN[S]?>+}
                                         }<WP>{

                             ChunkName:  {<NNP>+}

                             ChunkLessSymbole: {<JJ>?}
                                """
        self.taggedList = []
        self.tokenizedQuestionList = []
        self.chunkedList = []
        self.importantWordList = []
        self.dictionariesWord = {}

    def tokenizeQuestion(self):
        self.tokenizedQuestionList = nltk.word_tokenize(self.question)



    def removeJunkWord(self):
        for junkWord in ['country', 'What']:

            if (junkWord in self.tokenizedQuestionList):
                self.tokenizedQuestionList.remove(junkWord)

    def taggingQuestion(self):
        self.taggedList = nltk.pos_tag(self.tokenizedQuestionList)
        print self.taggedList


    def chunkingQuestion(self):
        chunkParser = nltk.RegexpParser(self.chunkGram)
        self.chunkedList = chunkParser.parse(self.taggedList)
        print self.chunkedList


    def extractImportantWord(self):




        for subTreeQuestion in self.chunkedList.subtrees():

            if subTreeQuestion._label in ['ChunkNumber', 'ChunkName', 'ChunkLessSymbole', 'ChunkSubject']:
                stringToConcat = ""
                listsequenceMot = []


                for leavesChunk in subTreeQuestion.leaves():
                        #print leavesChunk

                        if stringToConcat == "":
                            stringToConcat = leavesChunk[0]
                        else:
                            stringToConcat = stringToConcat + " " + leavesChunk[0]

                self.importantWordList.append(stringToConcat)

                if self.dictionariesWord.has_key(subTreeQuestion._label):
                    listsequenceMot = self.dictionariesWord.get(subTreeQuestion._label)

                listsequenceMot.append(stringToConcat)

                self.dictionariesWord[subTreeQuestion._label] = listsequenceMot


    def buildDictionaries(self):

        listSubject = []
        a = self.dictionariesWord.get('ChunkSubject')
        countSubject = 0
        dictChunkAndWord = {}




    def normalise(self):

        """Normalises words to lowercase and stems and lemmatizes it."""
        #word = .lower()
        #word = stemmer.stem_word(word)
        #word = lemmatizer.lemmatize(word)
        #return word




# ? = 0 or 1 rep
# * = 0 or more rep
# + = 1 or more rep






if __name__ == '__main__':

    for question in sentencesList:
        print " "
        print "Voici la question:"
        print question
        print "voici la question analyser"
        questionObject = processLanguage(question)

        questionObject.tokenizeQuestion()
        questionObject.removeJunkWord()
        questionObject.taggingQuestion()
        questionObject.chunkingQuestion()
        questionObject.extractImportantWord()
        # essai = questionObject.taggedList
        print questionObject.importantWordList
        print questionObject.dictionariesWord.items()




        # for eachitem in questionObject.chunkedList:
        #print eachitem



