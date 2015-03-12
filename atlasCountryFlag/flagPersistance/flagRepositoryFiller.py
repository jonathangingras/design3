__author__ = 'Antoine'
from atlasCountryFlag.flagPersistance.flagRepositroyDB import FlagRepositoryDB
from atlasCountryFlag.flagDomain.flagRepository import FlagRepository
from atlasCountryFlag.flagDomain.flag import Flag
from os import path
import json

class FlagRepositoryFiller(object):

    def __init__(self, flagRepository):
        self.flagRepository = flagRepository

    def __openingFlagJson(self, pathToModule):
        pathToFlagJson = pathToModule + "/flagData/new_country_json.json"
        pathToFlagJson = path.relpath(pathToFlagJson)
        self.flagJson = open(pathToFlagJson, 'r')
        flagJsonData = json.load(self.flagJson)
        return flagJsonData

    def __closeJsonFile(self):
        self.flagJson.close()

    def setupFlagRepository(self, pathToModule):
        flagJsonData = self.__openingFlagJson(pathToModule)
        flagCountries = flagJsonData['countries']
        for flagCountry in flagCountries:
            flafToAdd = Flag(flagCountry['name'], flagCountry['color_list'])
            self.flagRepository.addFlag(flafToAdd)
        self.__closeJsonFile()
