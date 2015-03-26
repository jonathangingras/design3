__author__ = 'Antoine'
from elasticsearch import Elasticsearch
from naturalLanguagePython.countryDomain.countryRepository import CountryRepository
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory


class CountryRepositoryElasticSearch(CountryRepository):

    def __init__(self, pathToModule):
        self.countryDB = Elasticsearch(['http://localhost:9200/country'])
        self.selfStrategyFactory = SearchStrategyFactory(pathToModule)
        self.pathToModule = pathToModule

    def addCountry(self, country, nameOfCountry):
        return #Script ran before to start and populate elasticsearch

    def __createStrategy(self, strategy):
        return self.selfStrategyFactory.createSearchStrategy(strategy)

    def __searchPossibleCountryByKeywordAndInformation(self, keyword, value, strategy):
        searchStrategy = self.__createStrategy(strategy)
        possibleCountry = searchStrategy.createSearchQuery(keyword, value, self.countryDB)
        self.listOfPossibleCountry.append(possibleCountry)

    def searchCountries(self, keywordDictionary, searchStrategyByKeyword):
        self.listOfPossibleCountry = []
        for keyword in keywordDictionary:
            keywordListKeyword = keywordDictionary[keyword]
            strategyListKeyword = searchStrategyByKeyword[keyword]
            numberOfElementForKeyword = len(keywordDictionary[keyword])
            i = 0
            while i < numberOfElementForKeyword:
                self.__searchPossibleCountryByKeywordAndInformation(keyword,
                                                                    keywordListKeyword[i],
                                                                    strategyListKeyword[i])
                i += 1

        return self.listOfPossibleCountry
