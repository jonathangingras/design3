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
        self.informationCategoryList = self.soup.find_all('div', 'category')
        self.informationList = self.soup.find_all('div', 'category_data')



    def extractInformation(self, nameOfTheInformation):
        tag = self.soup
        print(self.soup.tagStack)


    def closeOpenFiles(self):
        pass

if __name__ == '__main__':
    file_path = path.relpath("/home/antoine/workspace/design3/naturalLanguagePython/aa.html")
    parser = htmlParser(file_path,"/home/antoine/workspace/design3/naturalLanguagePython/extractedCountryInfo/aruba.txt")
    parser.extractCountryInformationHtmlTag()