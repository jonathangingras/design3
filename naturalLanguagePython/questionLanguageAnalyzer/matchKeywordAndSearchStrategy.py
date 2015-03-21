__author__ = 'Antoine'


class MatchKeywordAndSearchStrategy(object):

    def __init__(self):
        self.capital = "capital"
        self.startsWith = "starts with"
        self.endsWith = "ends with"

    def __createSearchStrategyLinkedKeywordDictionary(self, informationDictionary):
        searchStrategyLinkedToKeyword = {}
        for element in informationDictionary:
            searchStrategyLinkedToKeyword[element] = []
        return searchStrategyLinkedToKeyword

    def __matchCapitalKeywordToPossibleSearchStrategy(self, extractedSearchStrategy, informationDictionary,
                                                      searchStrategyLinkedToKeyword):
        if self.capital in informationDictionary:
            if self.startsWith in extractedSearchStrategy:
                searchStrategyLinkedToKeyword[self.capital].append(self.startsWith)
            if self.endsWith in extractedSearchStrategy:
                searchStrategyLinkedToKeyword[self.capital].append(self.endsWith)

    def matchSearchStrategyByKeyword(self, question, informationDictionary, extractedSearchStrategy):
        searchStrategyLinkedToKeyword = self.__createSearchStrategyLinkedKeywordDictionary(informationDictionary)
        self.__matchCapitalKeywordToPossibleSearchStrategy(extractedSearchStrategy, informationDictionary,
                                                           searchStrategyLinkedToKeyword)

        return searchStrategyLinkedToKeyword