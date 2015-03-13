__author__ = 'Antoine'
from atlasCountryFlag.flagDomain.flag import Flag
import abc

class FlagRepository(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def searchFlagColorList(self, nameOfCountry):
        return

    @abc.abstractmethod
    def addFlag(self, flag):
        return

    @abc.abstractmethod
    def searchFlagPictureFilename(self, nameOfCountry):
        return