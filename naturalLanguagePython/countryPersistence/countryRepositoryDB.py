__author__ = 'Antoine'
from naturalLanguagePython.CountryDomain.CountryRepository import CountryRepository
from naturalLanguagePython.CountryDomain.Country import Country


class CountryRepositoryDB(CountryRepository):

    def __init__(self):
        self.countryList = []

    def addCountry(self, country):
        self.countryList.append(country)

    def searchCountries(self, keywordDictionary):
        listOfPossibleCountry = []
        for country in self.countryList:
            for keyInfo in country.informationDict:
                for keyword in keywordDictionary:
                    if keyword is keyInfo:
                        if country.informationDict.get(keyInfo) is keywordDictionary.get(keyword):
                            listOfPossibleCountry.append(country.name)
        return listOfPossibleCountry


