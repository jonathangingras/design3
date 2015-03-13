__author__ = 'Antoine'
from atlasCountryFlag.flagPersistance.flagRepositroyDB import FlagRepositoryDB
from atlasCountryFlag.flagPersistance.flagRepositoryFiller import FlagRepositoryFiller


class FlagInformationSeeker(object):

    def __init__(self, pathToAtlasCountryFlagModule = None):
        self.flagRepository = FlagRepositoryDB()
        if pathToAtlasCountryFlagModule is not None:
            self.__fillFlagRepository(pathToAtlasCountryFlagModule)

    def searchColorFlagByNameOfCountry(self, nameOfCountry):
        flagColorList = self.flagRepository.searchFlagColorList(nameOfCountry)
        return flagColorList

    def searchFlagPictureFilename(self, nameOfCountry):
        flagPictureFilename = self.flagRepository.searchFlagPictureFilename(nameOfCountry)
        return flagPictureFilename

    def __fillFlagRepository(self, pathToAtlasCountryFlagModule):
        self.flagRepositoryFiller = FlagRepositoryFiller(self.flagRepository)
        self.flagRepositoryFiller.setupFlagRepository(pathToAtlasCountryFlagModule)