__author__ = 'Antoine'
from atlasCountryFlag.flagPersistance.flagRepositroyDB import FlagRepositoryDB

class FlagInformationSeeker(object):

    def __init__(self):
        self.flagRepository = FlagRepositoryDB()

    def searchColorFlagByNameOfCountry(self, nameOfCountry):
        flagColorList = self.flagRepository.searchFlagColorList(nameOfCountry)
        return flagColorList

    def searchFlagPictureFilename(self, nameOfCountry):
        flagPictureFilename = self.flagRepository.searchFlagPictureFilename(nameOfCountry)
        return flagPictureFilename