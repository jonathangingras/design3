__author__ = 'Antoine'
from atlasCountryFlag.flagPersistance.flagRepositroyDB import FlagRepositoryDB
from atlasCountryFlag.flagDomain.flagRepository import FlagRepository
from atlasCountryFlag.flagDomain.flag import Flag
from os import path
import json

class FlagRepositoryFiller(object):

    def __init__(self, flagRepository):
        self.flagRepository = flagRepository

    def setupFlagRepository(self, pathToModule):
        flagJsonData = self.__openingFlagJson(pathToModule)
        flagCountries = flagJsonData['countries']
        nameFieldInJson = 'name'
        colorListFieldInJson = 'color_list'
        for flagCountry in flagCountries:
            flagToAdd = Flag(flagCountry[nameFieldInJson], flagCountry[colorListFieldInJson])
            self.flagRepository.addFlag(flagToAdd)
        self.__closeJsonFile()

    def __openingFlagJson(self, pathToModule):
        pathToFlagDataJson = "/flagData/new_country_json.json"
        pathToFlagJson = pathToModule + pathToFlagDataJson
        pathToFlagJson = path.relpath(pathToFlagJson)
        self.flagJson = open(pathToFlagJson, 'r')
        flagJsonData = json.load(self.flagJson)
        return flagJsonData

    def __closeJsonFile(self):
        self.flagJson.close()
