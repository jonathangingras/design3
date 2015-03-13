__author__ = 'Antoine'
from atlasCountryFlag.flagService.flagInformationSeeker import FlagInformationSeeker

class FlagInformationProvider(object):

    def __init__(self, pathToAtlasCountryFlagModule):
        self.flagInformationSeeker = FlagInformationSeeker(pathToAtlasCountryFlagModule)

    def obtainFlagPictureFilename(self, nameOfCountry):
        return self.flagInformationSeeker.searchFlagPictureFilename(nameOfCountry)

    def obtainFlagColorList(self, nameOfCountry):
        return self.flagInformationSeeker.searchColorFlagByNameOfCountry(nameOfCountry)