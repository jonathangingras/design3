__author__ = 'antoine'
from bs4 import BeautifulSoup
from os import path
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

    def findCountryInformationValue(self):
        self.__extractCountryInformtionData__()
        ### faire une recherche dans le html par les key pour ajouter
        nomberOfContryFacts = len(self.informationDataList)
        for key in self.keys:
            print(key)
            informationKeyTag = self.soup.find('a', title = "Notes and Definitions: "+key)
            #print(informationKeyTag)
            parent = ((informationKeyTag.parent).parent).parent
            print((parent.next_sibling).next_element)



    def closeOpenedFiles(self):
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
            keyStringFormattedFromHtml = str(tagToExtractTheKey.string)
            strippedKeyString = keyStringFormattedFromHtml.strip(' :')
            key = strippedKeyString

        return key

    def __addKeyToKeyList__(self, key):
        if(key is not None and key != 'None'):
            self.keys[key] = None
if __name__ == '__main__':
    file_path = path.normpath("aa.html")
    parser = htmlParser(file_path)
    parser.findCountryInformationKeys()
    parser.findCountryInformationValue()
    parser.closeOpenedFiles()
