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
        self.chunkGramValueOnly = r""" ChunkValue:  {((<CD>+<NN\w?>*<\w+>?)|(<NNP>,?<IN>?)+)+}
                                        """
        self.taggedList = []
        self.tokenizedQuestionList = []
        self.chunkedList = []
        self.keyWordList = []
        self.importantWordList = []
        self.dictionariesWord = {}
        self.dictionariesWordReturn = {}

    def tokenizeQuestion(self, question):
        self.tokenizedQuestionList = nltk.word_tokenize(question)

    def removeJunkWord(self):
        for junkWord in ['country', 'title']:

            if (junkWord.capitalize() in self.tokenizedQuestionList):
                self.tokenizedQuestionList.insert(self.tokenizedQuestionList.index(junkWord.capitalize()), "that")
            elif junkWord.lower() in self.tokenizedQuestionList:
                self.tokenizedQuestionList.remove(junkWord.lower())

    def taggingQuestion(self):
        self.taggedList = nltk.pos_tag(self.tokenizedQuestionList)
        print self.taggedList

    def chunkingQuestion(self):
        chunkParser = nltk.RegexpParser(self.chunkGramAllSentense)
        self.chunkedList = chunkParser.parse(self.taggedList)

    def extractOnlyQuestionSubject(self):
        chunkParser = nltk.RegexpParser(self.chunkGramSubjectOnly)
        self.chunkedList = chunkParser.parse(self.taggedList)
        for subTreeQuestion in self.chunkedList.subtrees():
            if subTreeQuestion._label in ['ChunkSubjectOnly']:
                stringToConcat = ""

                for leavesChunk in subTreeQuestion.leaves():
                        if stringToConcat == "":
                            stringToConcat = leavesChunk[0]
                        else:
                            stringToConcat = stringToConcat + " " + leavesChunk[0]
                self.importantWordList.append(stringToConcat)


        return self.importantWordList

    def extractOnlyQuestionValue(self):
        chunkParser = nltk.RegexpParser(self.chunkGramValueOnly)
        self.chunkedList = chunkParser.parse(self.taggedList)
        for subTreeQuestion in self.chunkedList.subtrees():
            if subTreeQuestion._label in ['ChunkValue']:
                stringToConcat = ""

                listsequenceMot = []
                for leavesChunk in subTreeQuestion.leaves():
                    print leavesChunk
                    if stringToConcat == "":
                        stringToConcat = leavesChunk[0]
                    else:
                        stringToConcat = stringToConcat + " " + leavesChunk[0]

                self.keyWordList.append(stringToConcat)
        return self.keyWordList


    def extractImportantWord(self):
        for subTreeQuestion in self.chunkedList.subtrees():
            if subTreeQuestion._label in ['ChunkNumber', 'ChunkName', 'ChunkLessSymbole', 'ChunkSubject']:
                stringToConcat = ""
                listsequenceWord = []
                for leavesChunk in subTreeQuestion.leaves():
                        if stringToConcat == "":
                            stringToConcat = leavesChunk[0]
                        else:
                             stringToConcat = stringToConcat + " " + leavesChunk[0]

                self.importantWordList.append(stringToConcat)

                if self.dictionariesWord.has_key(subTreeQuestion._label):
                    listsequenceWord = self.dictionariesWord.get(subTreeQuestion._label)

                listsequenceWord.append(stringToConcat)
                self.dictionariesWord[subTreeQuestion._label] = listsequenceWord

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