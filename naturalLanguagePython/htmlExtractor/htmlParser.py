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
        self.__openFile__()
        self.__findCountryInformationKeys__()
        self.__findCountryInformationValue__()
        self.__writeInformationInOpenedFile__()
        self.__closeOpenedFile__()

    def __findCountryInformationKeys__(self):
        self.informationCategoryList = self.htmlExtractor.extractCountryInformationHtmlTag(self.soup)
        for informationCategory in self.informationCategoryList:
            key = self.htmlExtractor.informationCategoryFinder(informationCategory)
            key = self.htmlInformationFormatter.informationKeyFormatting(key)
            self.__addKeyToKeyList__(key)
        self.__deleteUnimportantKeyword__()

    def __findCountryInformationValue__(self):
        for key in self.keys:
            informationList = []
            extractedInfos = self.htmlExtractor.extractCountryData(key, self.soup)
            informationList = self.htmlInformationValidator.verifyingStringContent(extractedInfos)
            self.keys[key] = informationList

    def __writeInformationInOpenedFile__(self):
        json.dump(self.keys, self.file)

    def __closeOpenedFile__(self):
        self.file.close()

    def __openFile__(self):
        writeMode = 'w'
        jsonExtension = ".json"
        nameOfCountry = self.htmlExtractor.getNameOfCountry(self.soup)
        nameOfCountryFile = nameOfCountry + jsonExtension
        self.file = open(nameOfCountryFile, writeMode)

    def __addKeyToKeyList__(self, key):
        if(key is not None and key != 'None'):
            self.keys[key] = None

    def __deleteUnimportantKeyword__(self):
        keyToIgnore = ['Economy - overview']
        for key in keyToIgnore:
            self.keys.pop(key, None)


if __name__ == '__main__':
    file_path = path.normpath("ac.html")
    parser = htmlParser()
    parser.parseCountryHtml(file_path)