__author__ = 'Antoine'
import abc
class SearchInformation(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def findInformation(self, dictonary, keyword, wantedInformation):
        return