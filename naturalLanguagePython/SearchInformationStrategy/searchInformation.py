__author__ = 'Antoine'
import abc
import re


class SearchInformation(object):

    def __setRegex(self, wantedInformation):
        self.regex = wantedInformation

    @abc.abstractmethod
    def createQuery(self, keyword, value):
        return
