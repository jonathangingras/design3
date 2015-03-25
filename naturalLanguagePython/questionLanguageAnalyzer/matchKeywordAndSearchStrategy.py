__author__ = 'Antoine'
import re


class MatchKeywordAndSearchStrategy(object):

    def __init__(self):
        self.capital = "capital"
        self.startsWith = "starts with"
        self.endsWith = "ends with"
        self.searchStrategyLinkedToKeyword= {}
        self.regex = [r"$ is .", r"$ .", r"$ name .", r"and .", r"$ that ."]

    def __createSearchStrategyLinkedKeywordDictionary(self, informationDictionary):
        for element in informationDictionary:
            self.searchStrategyLinkedToKeyword[element] = []


    def __searchKeywordLinkInQuestionByRegex(self, keyword, question, searchStrategy):
        for possibleRegex in self.regex:
            possibleRegex = possibleRegex.replace("$", keyword)
            possibleRegex = possibleRegex.replace(".", searchStrategy)
            expression = re.compile(possibleRegex)
            result = expression.search(question)
            if result is not None:
                self.searchStrategyLinkedToKeyword[keyword].append(searchStrategy)
                break

    def matchSearchStrategyByKeyword(self, question, informationDictionary, extractedSearchStrategy):
        self.__createSearchStrategyLinkedKeywordDictionary(informationDictionary)
        for keyword in informationDictionary:
            for searchStrategy in extractedSearchStrategy:
                self.__searchKeywordLinkInQuestionByRegex(keyword, question, searchStrategy)
        return self.searchStrategyLinkedToKeyword