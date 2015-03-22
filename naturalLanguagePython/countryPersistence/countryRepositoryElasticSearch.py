__author__ = 'Antoine'
from elasticsearch import Elasticsearch
from naturalLanguagePython.countryDomain.countryRepository import CountryRepository


class CountryRepositoryElasticSearch(CountryRepository):

    def __init__(self):
        self.countryDB = Elasticsearch(['http://localhost:9200/country'])

    def addCountry(self, country, nameOfCountry):
        return #Script ran before to start and populate elasticsearch

    def __searchPossibleCountryByKeywordAndInformation(self, element, keyword):
        listOfPossibleCountryByKeyword = []
        query = \
            {
                "query":
                    {
                        "match": {keyword: element}
                    }
            }
        possibleCountry = self.countryDB.search(index="", doc_type="", body=query, size= 300)
        for returnedResult in possibleCountry["hits"]["hits"]:
            listOfPossibleCountryByKeyword.append(returnedResult["_id"])
        self.listOfPossibleCountry.append(listOfPossibleCountryByKeyword)

    def searchCountries(self, keywordDictionary, searchStrategyByKeyword):
        self.listOfPossibleCountry = []
        for keyword in keywordDictionary:
            for element in keywordDictionary[keyword]:
                self.__searchPossibleCountryByKeywordAndInformation(element, keyword)
        return self.listOfPossibleCountry
