__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
import re


class SearchContains(SearchInformation):

    def createSearchQuery(self, keyword, value):
        query = {
            "query":
                {
                    "match": {keyword: value}
                }
        }
        return query