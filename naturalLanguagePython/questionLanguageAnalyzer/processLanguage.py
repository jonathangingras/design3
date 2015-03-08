__author__ = 'alex'

import nltk

class ProcessLanguage(object):

    def __init__(self):
        self.chunkGramAllSentense = r"""KeyWord: {(<JJR>|<VBZ>)<IN>}
                             ChunkNumber: {(<KeyWord>)?<CD>+<NN\w?>*<\w+>?}
                                          }<CC>|<VB\w?>| <IN> | <JJ> | <KeyWord>{

                             ChunkSubject:  {(^<PRP$>|^<DT>|<JJ>|<KeyWord>)?<NN[S]?>?<NN>+}
                                         }<WP>  <PRP$> <DT>  <KeyWord>{
                             ChunkName:  {<KeyWord>?<NNP>+}
                                        }  <KeyWord> {

                             ChunkLessSymbole: {<JJ>}
                                """

        self.chunkGramSubjectOnly = r"""ChunkSubjectOnly:  {((<JJ><NN[S]?>+)|(<NN><IN><NN>))}

                                         """
        self.chunkGramValueOnly = r""" ChunkValue:  {(<KeyWord>?<NNP>+|(<KeyWord>)?<CD>+<NN\w?>*<\w+>?)}
                                        }  <KeyWord> {"""
        self.taggedList = []
        self.tokenizedQuestionList = []
        self.chunkedList = []
        self.keyWordList = []
        self.importantWordList = []
        self.dictionariesWord = {}
        self.dictionariesWordReturn = {}

    def tokenizeQuestion(self, question):
        self.tokenizedQuestionList = nltk.word_tokenize(question)

    def searchKeyWord(self, question):
        myFileKeyWord = open('keyWordList.txt', 'r')
        keyWordList = []
        keyWordList = myFileKeyWord.read()
        keyWordList = keyWordList.splitlines()
        for keyWord in keyWordList:
            if question.find(keyWord) > 0:
                if keyWord.count(" ") > 0:
                    for x in keyWord.split(" "):
                        self.keyWordList.append(x)
                else:
                    self.keyWordList.append(keyWord)
        if(len(self.keyWordList)> 0):
            for word in self.keyWordList:
                indexReplace = self.tokenizedQuestionList.index(word)
                self.tokenizedQuestionList[indexReplace] = " "


    def removeJunkWord(self):
        for junkWord in ['country', 'title']:

            if (junkWord.capitalize() in self.tokenizedQuestionList):
                self.tokenizedQuestionList.insert(self.tokenizedQuestionList.index(junkWord.capitalize()), "that")
            elif junkWord.lower() in self.tokenizedQuestionList:
                self.tokenizedQuestionList.remove(junkWord.lower())

    def taggingQuestion(self):
        self.taggedList = nltk.pos_tag(self.tokenizedQuestionList)
        #print self.taggedList

    def chunkingQuestion(self):
        chunkParser = nltk.RegexpParser(self.chunkGramAllSentense)
        self.chunkedList = chunkParser.parse(self.taggedList)

    def extractOnlyQuestionSubject(self):
        chunkParser = nltk.RegexpParser(self.chunkGramSubjectOnly)
        self.chunkedList = chunkParser.parse(self.taggedList)
        for subTreeQuestion in self.chunkedList.subtrees():
            if subTreeQuestion._label in ['ChunkSubjectOnly']:
                stringToConcat = ""
                listsequenceMot = []
                for leavesChunk in subTreeQuestion.leaves():
                        if stringToConcat == "":
                            stringToConcat = leavesChunk[0]
                        else:
                            stringToConcat = stringToConcat + " " + leavesChunk[0]
                self.importantWordList.append(stringToConcat)

                listsequenceMot.append(stringToConcat)
        return self.importantWordList

    def extractImportantWord(self):
        for subTreeQuestion in self.chunkedList.subtrees():
            if subTreeQuestion._label in ['ChunkNumber', 'ChunkName', 'ChunkLessSymbole', 'ChunkSubject']:
                stringToConcat = ""
                listsequenceMot = []
                for leavesChunk in subTreeQuestion.leaves():
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

        self.tokenizeQuestion()
        self.removeJunkWord()
        self.taggingQuestion()
        self.chunkingQuestion()
        self.extractImportantWord()

        if self.dictionariesWord.has_key('ChunkSubject'):
            list_Item = self.dictionariesWord.items()
            stringSub = ""
            listValue = []
            for item in list_Item:
                if(item[0] == "ChunkSubject"):
                    stringSubject = item [1]
                    stringSub = stringSubject[0]
                else:
                    for i in item[1]:
                        listValue.append(i)

            self.dictionariesWordReturn[stringSub] = listValue