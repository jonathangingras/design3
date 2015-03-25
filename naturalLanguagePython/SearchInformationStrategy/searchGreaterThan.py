__author__ = 'Antoine'
import sys
import json
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchGreaterThan(SearchInformation):

    def createSearchQuery(self, keyword, value):
        query = {
            "query":
                {
                    "bool":
                        {
                            "must":{
                                "range":
                                {
                                keyword:
                                    {
                                        "from": value,
                                        "to": str(sys.maxint),
                                        "include_upper": False,
                                        "boost": 2.0
                                    }
                                },
                        }
                    }
                }
        }

        query = keyword+":["+value+" TO "+str(sys.maxint)+"]"
        print(query)
        return query