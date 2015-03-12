__author__ = 'Antoine'
from atlasCountryFlag.flagDomain.flag import Flag
import abc

class flagRepository(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def searchFlag(self, nameOfCountry):
        pass