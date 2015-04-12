__author__ = 'alex'

import nltk



class ProcessLanguage(object):

    def __init__(self):


        self.chunkGramSubjectOnly = r"""QuestionWordStartsSentence: {<WP><NN>(<VBZ>|<NN\w?>)}
                             ChunkSubjectOnly:  {((<QuestionWordStartsSentence><.*><NN\w?>+)|(<JJ><NN[S]?>+)|(<NN><IN><NN>))?}
                                                }<QuestionWordStartsSentence>{
                                         """
        self.chunkGramValueOnly = r"""QuestionWordStartsSentence: {<WP><NN>(<VBZ>|<NN\w?>)}
                                                AdjectiveHidden: {<QuestionWordStartsSentence><DT><JJ><NN>}
                                                }<QuestionWordStartsSentence>|<NN>|<DT>{

                            ChunkValue:  {((<CD>+(\w+\/\d+)?<NN\w?>*<\w+>?)|(<NNP>,?<IN>?)+)+|<AdjectiveHidden>}
                                                }<QuestionWordStartsSentence><DT>{
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

    def taggingQuestion(self):
        self.taggedList = nltk.pos_tag(self.tokenizedQuestionList)

    def __extractLeavesFromChunkTreeOfSubject(self, stringToConcat, subTreeQuestion):
        for leavesChunk in subTreeQuestion.leaves():
            if stringToConcat == "":
                stringToConcat = leavesChunk[0]
            else:
                stringToConcat = stringToConcat + " " + leavesChunk[0]
        return stringToConcat

    def extractOnlyQuestionSubject(self):
        chunkParser = nltk.RegexpParser(self.chunkGramSubjectOnly)
        self.chunkedList = chunkParser.parse(self.taggedList)
        for subTreeQuestion in self.chunkedList.subtrees():
            if subTreeQuestion._label in ['ChunkSubjectOnly']:
                stringToConcat = ""

                stringToConcat = self.__extractLeavesFromChunkTreeOfSubject(stringToConcat, subTreeQuestion)
                self.importantWordList.append(stringToConcat)


        return self.importantWordList

    def __extractLeavesFromTreeOfValue(self, stringToConcat, subTreeQuestion):
        for leavesChunk in subTreeQuestion.leaves():
            if stringToConcat == "":
                stringToConcat = leavesChunk[0]
            else:
                stringToConcat = stringToConcat + " " + leavesChunk[0]
        return stringToConcat

    def extractOnlyQuestionValue(self):
        chunkParser = nltk.RegexpParser(self.chunkGramValueOnly)
        self.chunkedList = chunkParser.parse(self.taggedList)
        for subTreeQuestion in self.chunkedList.subtrees():
            if subTreeQuestion._label in ['ChunkValue']:
                stringToConcat = ""

                stringToConcat = self.__extractLeavesFromTreeOfValue(stringToConcat, subTreeQuestion)

                self.keyWordList.append(stringToConcat)
        return self.keyWordList


    def buildDictionaries(self,question):
        self.extractOnlyQuestionValue()
        self.extractOnlyQuestionSubject()


        if len(self.keyWordList) == 1 and len(self.importantWordList) == 1:
            self.dictionariesWord[self.importantWordList.pop()] = self.keyWordList
        else:
            for x,y in zip(self.importantWordList,self.keyWordList):
                self.dictionariesWord[str(x)] = str(y)