__author__ = 'Antoine'
from os import path
from decimal import Decimal
import json
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchGreaterThan(SearchInformation):

    def __openJsonRangeFile(self, pathToWorkingModule):
        nameOfRangeFile = path.realpath(pathToWorkingModule + "/searchInformationStrategy/greaterRangeValue.json")
        greaterRangeFile = open(nameOfRangeFile)
        greaterIncrementFile = open(path.realpath(pathToWorkingModule+ "/searchInformationStrategy/IncrementByKeyword.json"))
        self.greaterValueJson = json.load(greaterRangeFile)
        self.incrementByKeyword = json.load(greaterIncrementFile)
        greaterRangeFile.close()
        greaterIncrementFile.close()

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

    def __executeSearchQuery(self, query, repository):
        possibleCountry = repository.search(index="", doc_type="", body=query, size=300, fields=["_id", "_score"])
        for returnedResult in possibleCountry["hits"]["hits"]:
            self.listOfPossibleCountryByKeyword.append(returnedResult["_id"])

    def createSearchQuery(self, keyword, value, repository):
        self.listOfPossibleCountryByKeyword = []
        self.__setMaxValueToReach(keyword)
        self.__setIncrementValue(keyword)
        self.searchFinished = False
        while (self.searchFinished is False):
            query = self.__buildingQuery(keyword, value)
            value = self.__incrementValue(value)
            self.__executeSearchQuery(query, repository)
        return self.listOfPossibleCountryByKeyword