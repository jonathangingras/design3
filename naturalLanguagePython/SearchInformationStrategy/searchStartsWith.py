import re

__author__ = 'Antoine'

from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchStartsWith(SearchInformation):

    def createSearchQuery(self, keyword, value):
        query = {
            "query":{
                "match_phrase_prefix" : {
                    keyword : value
                }
            }
        }
        return query
