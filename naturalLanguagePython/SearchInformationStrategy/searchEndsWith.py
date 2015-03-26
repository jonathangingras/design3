__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
import re

class SearchEndsWith(SearchInformation):

    def createSearchQuery(self, keyword, value, repository):
        listOfPossibleCountryByKeyword = []
        query = {
            "query":
                {
                    "fuzzy": {
                        keyword:{
                            "value": value,
                            }
                    }
                }
        }
        possibleCountry = repository.search(index="", doc_type="", body=query, size= 300, fields= ["_id", "_score"])
        for returnedResult in possibleCountry["hits"]["hits"]:
            listOfPossibleCountryByKeyword.append(returnedResult["_id"])
        return listOfPossibleCountryByKeyword