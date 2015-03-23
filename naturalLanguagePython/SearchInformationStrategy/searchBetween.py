__author__ = 'Antoine'
import re
from decimal import Decimal
from math import pow
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation


class SearchBetween(SearchInformation):

    def createSearchQuery(self, keyword, value):
        value = value.replace("%", "")
        value = float(value)
        query = {
            "fuzzy":{
                keyword:{
                "value": value
            }
            }
        }
        return query