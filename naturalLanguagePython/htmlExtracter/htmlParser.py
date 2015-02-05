__author__ = 'antoine'

from bs4 import BeautifulSoup
from os import path

class htmlParser(object):

    def __init__(self, fileToParse, nameOfCountry):

        self.soup = BeautifulSoup(open(fileToParse))
        try:
            self.file = open(nameOfCountry, 'w')

        except:
            print("file does not exist")

    def extractCountryInformationHtmlTag(self):
        tag = 'div'
        classType  = 'category'
        self.informationCategoryList = self.soup.find_all(tag, classType)

    def findCountryInformationKeys(self):
        self.extractCountryInformationHtmlTag()
        self.keys = []
        numberOfContryFacts = len(self.informationCategoryList)
        for i in range(numberOfContryFacts):
            tag = self.informationCategoryList[i]
            print(tag.contents)



    def closeOpenFiles(self):
        pass

if __name__ == '__main__':
    file_path = path.relpath("/home/antoine/workspace/design3/naturalLanguagePython/aa.html")
    parser = htmlParser(file_path,"/home/antoine/workspace/design3/naturalLanguagePython/extractedCountryInfo/aruba.txt")
    parser.findCountryInformationKeys()
