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
            for keyword in keywordDictionary:
                if country.contains(keyword, keywordDictionary[keyword]):
                    listOfPossibleCountry.append(country.name)
        return listOfPossibleCountry
