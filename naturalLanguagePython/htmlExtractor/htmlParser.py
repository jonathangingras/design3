__author__ = 'antoine'
from bs4 import BeautifulSoup
from os import path
import json
from htmlInformationFormatter import HtmlInformationFormatter
from htmlExtractor import HtmlExtractor
from htmlInformationValidator import HtmlInformationValidator

class htmlParser(object):

    def __init__(self):
        self.keys = {}
        self.htmlInformationFormatter = HtmlInformationFormatter()
        self.htmlExtractor = HtmlExtractor()
        self.htmlInformationValidator = HtmlInformationValidator()

    def parseCountryHtml(self, fileToParse):
        self.soup = BeautifulSoup(open(fileToParse))
        self.__openFile()
        self.__findCountryInformationKeys()
        self.__findCountryInformationValue()
        self.__writeInformationInOpenedFile()
        self.__closeOpenedFile()

    def __findCountryInformationKeys(self):
        self.informationCategoryList = self.htmlExtractor.extractCountryInformationHtmlTag(self.soup)
        for informationCategory in self.informationCategoryList:
            key = self.htmlExtractor.informationCategoryFinder(informationCategory)
            key = self.htmlInformationFormatter.informationKeyFormatting(key)
            self.__addKeyToKeyList(key)
        self.__deleteUnimportantKeyword()

    def __findCountryInformationValue(self):
        for key in self.keys:
            informationList = []
            extractedInfos = self.htmlExtractor.extractCountryData(key, self.soup)
            informationList = self.htmlInformationValidator.verifyingStringContent(extractedInfos)
            self.keys[key.encode()] = informationList

    def __writeInformationInOpenedFile(self):
        json.dump(self.keys, self.file, indent = 4, separators = (',', ':'))

    def __closeOpenedFile(self):
        self.file.close()

    def __openFile(self):
        writeMode = 'w'
        jsonExtension = ".json"
        pathDirectory = "extractedCountryJson/"
        nameOfCountry = self.htmlExtractor.getNameOfCountry(self.soup)
        nameOfCountry = nameOfCountry.replace(' ', '_')
        nameOfountryFile = pathDirectory + nameOfCountry + jsonExtension
        self.file = open(nameOfCountryFile, writeMode)


    def __addKeyToKeyList(self, key):
        if(key is not None and key != 'None'):
            self.keys[key] = None

    def __deleteUnimportantKeyword(self):
        keyToIgnore = ['Economy - overview', "Executive branch", "Map references","Merchant marine", "Background", "Environment - international agreements",
                       "Legislative branch", "Judicial branch", "Military branches"]
        for key in keyToIgnore:
            self.keys.pop(key, None)


if __name__ == '__main__':
    htmlFilePathDirectory = "htmlFiles/"

    countryNameFilePath = path.realpath(htmlFilePathDirectory + "countryHtmlName.txt")
    countryNameFile = open(countryNameFilePath, 'r')
    for line in countryNameFile.readlines():
            line = line.strip()
            filePath = path.realpath(htmlFilePathDirectory + line + ".html")
            parser = htmlParser()
            parser.parseCountryHtml(filePath)
    countryNameFile.close()