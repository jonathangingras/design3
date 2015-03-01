__author__ = 'Antoine'
from naturalLanguagePython.CountryDomain.countryRepository import CountryRepository
from naturalLanguagePython.CountryDomain.Country import Country


class CountryRepositoryDB(CountryRepository):

    def __init__(self):
        self.countryList = []

    def addCountry(self, country):
        self.countryList.append(country)

    def searchCountries(self, keywordDictionary, searchStrategy = None):
        listOfPossibleCountryByKeyword = []
        for keyword in keywordDictionary:
            listOfPossibleCountry = []
            for country in self.countryList:
                if country.contains(keyword, keywordDictionary[keyword], searchStrategy):
                    listOfPossibleCountry.append(country.name)
            listOfPossibleCountryByKeyword.append(listOfPossibleCountry)
        return listOfPossibleCountryByKeyword

