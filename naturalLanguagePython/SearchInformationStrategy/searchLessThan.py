__author__ = 'Antoine'
from os import path
from decimal import Decimal
import json
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchLessThan(SearchInformation):

    def __openJsonRangeFile(self, pathToWorkingModule):
        nameOfRangeFile = path.realpath(pathToWorkingModule + "/searchInformationStrategy/lessRangeValue.json")
        lesserRangeFile = open(nameOfRangeFile)
        incrementFile = open(path.realpath(pathToWorkingModule+ "/searchInformationStrategy/IncrementByKeyword.json"))
        self.lesserValueJson = json.load(lesserRangeFile)
        self.incrementByKeyword = json.load(incrementFile)
        lesserRangeFile.close()
        incrementFile.close()

    def __init__(self, pathToWorkingModule):
        self.__openJsonRangeFile(pathToWorkingModule)

    def __setMinValueToReach(self, keyword):
        self.minValue = self.lesserValueJson[keyword]

    def __setDecrementValue(self, keyword):
        self.decrement = self.incrementByKeyword[keyword]

    def __decrementValue(self, value):
        if Decimal(value) < Decimal(self.minValue):
            self.searchFinished = True
        else:
            value = str(Decimal(value) - Decimal(self.decrement))
        return value

    def __extractNumericValueFromValue(self, value):
        elementSplit = value.split(" ")
        value = elementSplit[0]
        return value

    def __setQueryBuilderParameters(self, keyword):
        self.__setMinValueToReach(keyword)
        self.__setDecrementValue(keyword)
        self.searchFinished = False

    def __buildingQuery(self, keyword, value):
        formattedValueForQuery = value.replace(".", "\.")
        query = {
            "query":
                {
                    "regexp":
                        {
                            keyword: formattedValueForQuery
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
        self.__setQueryBuilderParameters(keyword)
        value = self.__extractNumericValueFromValue(value)
        while (self.searchFinished is False):
            query = self.__buildingQuery(keyword, value)
            value = self.__decrementValue(value)
            self.__executeSearchQuery(query, repository)
        return self.listOfPossibleCountryByKeyword
