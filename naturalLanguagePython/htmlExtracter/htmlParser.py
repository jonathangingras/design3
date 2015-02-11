__author__ = 'antoine'
from bs4 import BeautifulSoup
from os import path
import json
from htmlInformationFormatter import HtmlInformationFormatter
from htmlExtractor import HtmlExtractor
from htmlInformationValidator import HtmlInformationValidator

class htmlParser(object):

    def __init__(self, fileToParse):
        self.keys = {}
        self.htmlInformationFormatter = HtmlInformationFormatter()
        self.htmlExtractor = HtmlExtractor()
        self.htmlInformationValidator = HtmlInformationValidator()
        self.soup = BeautifulSoup(open(fileToParse))
        self.__openFile__()

    def findCountryInformationKeys(self):
        self.informationCategoryList = self.htmlExtractor.extractCountryInformationHtmlTag(self.soup)
        for informationCategory in self.informationCategoryList:
            key = self.htmlExtractor.informationCategoryFinder(informationCategory)
            key = self.htmlInformationFormatter.informationKeyFormatting(key)
            self.__addKeyToKeyList__(key)
        self.__deleteUnimportantKeyword__()

    def findCountryInformationValue(self):
        for key in self.keys:
            informationList = []
            extractedInfos = self.htmlExtractor.extractCountryData(key, self.soup)
            informationList = self.htmlInformationValidator.verifyingStringContent(extractedInfos)
            self.keys[key] = informationList

    def __writeInformationInOpenedFile__(self):
        json.dump(self.keys, self.file)

    def closeOpenedFiles(self):
        self.__writeInformationInOpenedFile__()
        self.file.close()

    def __openFile__(self):
        appendMode = 'a'
        jsonExtension = ".json"
        nameOfCountry = self.htmlExtractor.getNameOfCountry(self.soup)
        nameOfCountryFile = nameOfCountry + jsonExtension
        self.file = open(nameOfCountryFile, appendMode)
        self.__writeNameOfCountry__(nameOfCountry)

    def __writeNameOfCountry__(self, nameOfCountry):
        json.dump(nameOfCountry, self.file)

    def __addKeyToKeyList__(self, key):
        if(key is not None and key != 'None'):
            self.keys[key] = None

    def __deleteUnimportantKeyword__(self):
        keyToIgnore = ['Economy - overview']
        for key in keyToIgnore:
            self.keys.pop(key, None)


if __name__ == '__main__':
    file_path = path.normpath("aa.html")
    parser = htmlParser(file_path)
    parser.findCountryInformationKeys()
    parser.findCountryInformationValue()
    parser.closeOpenedFiles()