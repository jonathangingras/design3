__author__ = 'Antoine'
from naturalLanguagePython.CountryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.CountryDomain.country import Country
from os import path
import os, json

class CountryRepositoryFiller(object):

    def __init__(self, countryRepository):
        self.countryRepository = countryRepository

    def addCountriesToTheRepository(self):
        jsonDirectoryPath = "C://Users//Antoine//Documents//design3//naturalLanguagePython//HtmlExtractor//extractedCountryJson"
        for countryFile in os.listdir(path.abspath(jsonDirectoryPath)):
            nameOfCountryToAdd = countryFile.split('.')
            extractedCountryJson = jsonDirectoryPath + "//" + countryFile
            countryJson = open((extractedCountryJson), 'r')
            countryInformationDict = json.load(countryJson)
            country = Country(nameOfCountryToAdd[0], countryInformationDict)
            self.countryRepository.addCountry(country)