__author__ = 'Antoine'
import abc
import re


class SearchInformation(object):

    @abc.abstractmethod
    def searchPossibleCountryByKeywordValue(self, keyword, value, repository):
        return
