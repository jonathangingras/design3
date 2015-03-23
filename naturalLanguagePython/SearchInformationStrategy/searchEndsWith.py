__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
import re

class SearchEndsWith(SearchInformation):

    def createSearchQuery(self, keyword, value):
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
        return query