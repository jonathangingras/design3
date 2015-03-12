__author__ = 'Antoine'
from atlasCountryFlag.flagDomain.flag import Flag
import abc

class FlagRepository(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def searchFlag(self, nameOfCountry):
        return

    @abc.abstractmethod
    def addFlag(self, flag):
        return