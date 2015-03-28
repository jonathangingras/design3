from naturalLanguagePython.searchInformationStrategy.searchKeywordException import SearchKeywordException

__author__ = 'Antoine'

from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchStartsWith(SearchInformation):

    def searchPossibleCountryByKeywordValue(self, keyword, value, repository):
        listOfPossibleCountryByKeyword = []
        if keyword is None:
            raise SearchKeywordException("The keyword is none")
        query = {
            "query":{
                "match_phrase_prefix" : {
                    keyword : value
                }
            }
        }
        possibleCountry = repository.search(index="", doc_type="", body=query, size= 300, fields= ["_id", "_score"])
        for returnedResult in possibleCountry["hits"]["hits"]:
            listOfPossibleCountryByKeyword.append(returnedResult["_id"])
        return listOfPossibleCountryByKeyword
