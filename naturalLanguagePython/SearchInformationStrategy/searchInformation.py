__author__ = 'Antoine'
import abc
import re


class SearchInformation(object):

    @abc.abstractmethod
    def createSearchQuery(self, keyword, value):
        return
