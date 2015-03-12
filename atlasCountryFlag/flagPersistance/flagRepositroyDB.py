__author__ = 'Antoine'
from atlasCountryFlag.flagDomain.flagRepository import FlagRepository

class FlagRepositoryDB(FlagRepository):

    def __init__(self):
        self.flagList = []


    def searchFlag(self, nameOfCountry):
        colorList = []
        for element in self.flagList:
            if element.isFlagForThisCountry(nameOfCountry):
                colorList = element.colorList
                break
        return colorList

    def addFlag(self, flag):
        self.flagList.append(flag)