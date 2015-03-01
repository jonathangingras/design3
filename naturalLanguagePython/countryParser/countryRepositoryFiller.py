__author__ = 'Antoine'
from naturalLanguagePython.CountryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.CountryDomain.Country import Country
from os import path
import os, json

class CountryRepositoryFiller(object):

    def __init__(self, countryRepository):
        self.countryRepository = countryRepository

    def addCountriesToTheRepository(self):
        jsonDirectoryPath = path.abspath('./naturalLanguagePython/HtmlExtractor/extractedCountryJson')
        for countryFile in os.listdir(jsonDirectoryPath):
            nameOfCountryToAdd = countryFile.split('.')
            extractedCountryJson = jsonDirectoryPath + "//" + countryFile
            countryJson = open((extractedCountryJson), 'r')
            countryInformationDict = json.load(countryJson)
            country = Country(nameOfCountryToAdd[0], countryInformationDict)
            self.countryRepository.addCountry(country)