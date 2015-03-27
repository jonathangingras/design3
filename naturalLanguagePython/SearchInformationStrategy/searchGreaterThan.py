__author__ = 'Antoine'
from os import path
from decimal import Decimal
import json
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
from naturalLanguagePython.searchInformationStrategy.searchKeywordException import SearchKeywordException


class SearchGreaterThan(SearchInformation):

    def __openJsonRangeFile(self, pathToWorkingModule):
        nameOfRangeFile = path.realpath(pathToWorkingModule + "/searchInformationStrategy/greaterRangeValue.json")
        greaterRangeFile = open(nameOfRangeFile)
        greaterIncrementFile = open(path.realpath(pathToWorkingModule+ "/searchInformationStrategy/IncrementByKeyword.json"))
        self.greaterValueJson = json.load(greaterRangeFile)
        self.incrementByKeyword = json.load(greaterIncrementFile)
        greaterRangeFile.close()
        greaterIncrementFile.close()
        self.listOfKeywordForRangeRegex = ["population", "electricity - production"]

    def __init__(self, pathToWorkingModule):
        self.__openJsonRangeFile(pathToWorkingModule)

    def __setMaxValueToReach(self, keyword):
        self.maxValue = self.greaterValueJson[keyword]

    def __setIncrementValue(self, keyword):
        self.increment = self.incrementByKeyword[keyword]

    def __incrementValue(self, value):
        splitValue = value.split(" ")
        if "%" in splitValue[0]:
            splitValue[0] = splitValue[0].replace("%", "")
        if Decimal(splitValue[0]) > Decimal(self.maxValue):
            self.searchFinished = True
        else:
            splitValue[0] = str(Decimal(splitValue[0]) + Decimal(self.increment))
        return splitValue[0]

    def __buildingQuery(self, keyword, value):
        query = {
            "query":
                {
                    "regexp":
                        {
                            keyword: value
                        }
                }
        }
        return query

    def __buildingRangeRegexQuery(self, keyword, value):
        query = {
            "query":
                {
                    "regexp":
                        {
                            keyword:
                                {
                                    "value": "<" + value + "-" + self.maxValue + ">",
                                    "flags": "INTERVAL"
                                }
                        }
                }
        }
        return query
    def __executeSearchQuery(self, query, repository):
        possibleCountry = repository.search(index="", doc_type="", body=query, size=300, fields=["_id", "_score"])
        for returnedResult in possibleCountry["hits"]["hits"]:
            self.listOfPossibleCountryByKeyword.append(returnedResult["_id"])

    def __iterativeSearchQuery(self, keyword, repository, value):
        self.__setIncrementValue(keyword)
        self.searchFinished = False
        while (self.searchFinished is False):
            query = self.__buildingQuery(keyword, value)
            value = self.__incrementValue(value)
            self.__executeSearchQuery(query, repository)

    def __isKeywordRangeRegex(self, keyword):
        regexCondition = False
        if keyword in self.listOfKeywordForRangeRegex:
            regexCondition = True
        return regexCondition

    def __searchByRangeRegexQuery(self, keyword, repository, value):
        query = self.__buildingRangeRegexQuery(keyword, value)
        self.__executeSearchQuery(query, repository)

    def searchPossibleCountryByKeywordValue(self, keyword, value, repository):
        self.listOfPossibleCountryByKeyword = []
        if keyword is None:
            raise SearchKeywordException("The keyword is none")
        self.__setMaxValueToReach(keyword)
        if self.__isKeywordRangeRegex(keyword):
            self.__searchByRangeRegexQuery(keyword, repository, value)
        else:
            self.__iterativeSearchQuery(keyword, repository, value)
        return self.listOfPossibleCountryByKeyword