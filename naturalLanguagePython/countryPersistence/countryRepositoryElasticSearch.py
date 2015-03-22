__author__ = 'Antoine'
from elasticsearch import Elasticsearch
from naturalLanguagePython.countryDomain.countryRepository import CountryRepository
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory


class CountryRepositoryElasticSearch(CountryRepository):

    def __init__(self):
        self.countryDB = Elasticsearch(['http://localhost:9200/country'])
        self.selfStrategyFactory = SearchStrategyFactory()

    def addCountry(self, country, nameOfCountry):
        return #Script ran before to start and populate elasticsearch

    def __createStrategy(self, strategy):
        return self.selfStrategyFactory.createSearchStrategy(strategy)

    def __searchPossibleCountryByKeywordAndInformation(self, keyword, value, strategy):
        listOfPossibleCountryByKeyword = []
        searchStrategy = self.__createStrategy(strategy)
        query = searchStrategy.createSearchQuery(keyword, value)
        possibleCountry = self.countryDB.search(index="", doc_type="", body=query, size= 300)
        for returnedResult in possibleCountry["hits"]["hits"]:
            listOfPossibleCountryByKeyword.append(returnedResult["_id"])
        self.listOfPossibleCountry.append(listOfPossibleCountryByKeyword)

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
