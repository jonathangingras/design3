__author__ = 'Antoine'
import abc

class CountryRepository(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def searchCountries(self, keywordDictionary):
        return

    @abc.abstractmethod
    def addCountry(self, country):
        return