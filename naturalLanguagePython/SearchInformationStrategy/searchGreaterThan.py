__author__ = 'Antoine'
import sys
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
class SearchGreaterThan(SearchInformation):

    def createSearchQuery(self, keyword, value):
        query = {
            "query":
                {
                    "range":
                        {
                            keyword:
                                {
                                    "from": value,
                                    "to": "*",
                                    "boost": 2.0
                                }
                        }
                }
        }


        print(query)
        return query