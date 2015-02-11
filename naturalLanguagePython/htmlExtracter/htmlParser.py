__author__ = 'antoine'
from bs4 import BeautifulSoup
from os import path
import json
endOfLine = "\n"

class htmlParser(object):

    def __init__(self, fileToParse):
        self.keys = {}
        self.value = []
        self.soup = BeautifulSoup(open(fileToParse))
        self.__openFile__()

    def findCountryInformationKeys(self):
        self.__extractCountryInformationHtmlTag__()
        numberOfContryFacts = len(self.informationCategoryList)
        for i in range(numberOfContryFacts):
            tag = self.informationCategoryList[i]
            tagChild = tag.find('a')
            key = self.__informationKeyFormatting__(tagChild)
            self.__addKeyToKeyList__(key)
        self.__deleteNonImportantKeyword__()

    def findCountryInformationValue(self):
        for key in self.keys:
            informationList = []
            extractedInfos = self.__extractCountryData__(key)
            for extractedInfo in extractedInfos:
                self.__verifyingStringContent__(extractedInfo, informationList)
            self.keys[key] = informationList


    def __extractCountryData__(self, key):
        informationKeyTag = self.soup.find('a', title="Notes and Definitions: " + key)
        parent = ((informationKeyTag.parent).parent).parent
        parentNextElement = (parent.next_sibling).next_element
        extractedInfos = parentNextElement.find_all(['div', 'span'], ['category', 'category_data'])
        return extractedInfos

    def __verifyingStringContent__(self, extractedInfo, informationList):
        if extractedInfo.string is not None:
            formattedInformationString = self.__informationKeyFormatting__(extractedInfo.string)
            if formattedInformationString is not None:
                informationList.append(formattedInformationString)

    def writeInformationInOpenedFile(self):
        for key in self.keys:
            print(self.keys.get(key))

    def closeOpenedFiles(self):
        json.dump(self.keys, self.file)
        self.file.close()

    def __openFile__(self):
        appendMode = 'a'
        txtExtension = ".txt"

        nameOfCountry = self.__getNameOfCountry__()
        nameOfCountryFile = nameOfCountry+ txtExtension
        self.file = open(nameOfCountryFile, appendMode)
        self.__writeNameOfCountry__(nameOfCountry)

    def __getNameOfCountry__(self):
        nameOfCountryTag = self.soup.find('span', 'region')
        return nameOfCountryTag.string

    def __writeNameOfCountry__(self, nameOfCountry):
        nameOfCountry = nameOfCountry + endOfLine
        self.file.write(nameOfCountry)

    def __extractCountryInformationHtmlTag__(self):
        tag = 'div'
        classType  = "category"
        self.informationCategoryList = self.soup.find_all(tag, classType)

    def __extractCountryInformtionData__(self):
        tag = 'td'
        wantedId = 'data'
        self.informationDataList = self.soup.find_all(tag, id = wantedId)

    def __informationKeyFormatting__(self, tagToExtractTheKey):
        key = None
        if (tagToExtractTheKey is not None):
            string = tagToExtractTheKey.string
            keyStringFormattedFromHtml = str(string)
            strippedKeyString = keyStringFormattedFromHtml.strip(' :')
            key = strippedKeyString
        if key == 'country comparison to the world':
            key = None
        return key

    def __addKeyToKeyList__(self, key):
        if(key is not None and key != 'None'):
            self.keys[key] = None

    def __deleteNonImportantKeyword__(self):
        keyToIgnore = ['Economy - overview']
        for key in keyToIgnore:
            self.keys.pop(key, None)


if __name__ == '__main__':
    file_path = path.normpath("aa.html")
    parser = htmlParser(file_path)
    parser.findCountryInformationKeys()
    parser.findCountryInformationValue()
    parser.closeOpenedFiles()