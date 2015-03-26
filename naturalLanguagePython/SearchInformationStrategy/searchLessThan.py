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
        splitValue = value.split(" ")
        if Decimal(splitValue[0]) < Decimal(self.minValue):
            self.searchFinished = True
        else:
            splitValue[0] = str(Decimal(splitValue[0]) - Decimal(self.decrement))
        return splitValue[0]

    def createSearchQuery(self, keyword, value, repository):
        self.listOfPossibleCountryByKeyword = []
        self.__setMinValueToReach(keyword)
        self.__setDecrementValue(keyword)
        self.searchFinished = False
        while (self.searchFinished is False):
            query = {
                "query":
                    {
                        "regexp":
                            {
                                keyword: "("+value+")"
                            }
                    }
            }
            value = self.__decrementValue(value)
            print(value)
            possibleCountry = repository.search(index="", doc_type="", body=query, size= 300, fields= ["_id", "_score"])
            print(possibleCountry)
            for returnedResult in possibleCountry["hits"]["hits"]:
                self.listOfPossibleCountryByKeyword.append(returnedResult["_id"])

        return self.listOfPossibleCountryByKeyword
