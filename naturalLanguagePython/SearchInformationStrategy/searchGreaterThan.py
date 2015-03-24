__author__ = 'Antoine'
import sys
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
class SearchGreaterThan(SearchInformation):

    def createSearchQuery(self, keyword, value):
        query = {
            "query":
                {
                    "filtered":{
                        "query":{"match_all":{}},
                        "filter": {
                            "range":{
                                keyword:{
                                    "lte": (value)
                                }
                            }
                    }
                    }

                }
        }
        print(query)
        return query