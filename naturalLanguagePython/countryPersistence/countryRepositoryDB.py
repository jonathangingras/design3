__author__ = 'Antoine'
from naturalLanguagePython.CountryDomain.CountryRepository import CountryRepository
from naturalLanguagePython.CountryDomain.Country import Country


class CountryRepositoryDB(CountryRepository):

    def __init__(self):
        self.countryList = []

    def addCountry(self, country):
        self.countryList.append(country)

    def searchCountries(self, keywordDictionary):
        listOfPossibleCountryByKeyword = []
        for keyword in keywordDictionary:
            listOfPossibleCountry = []
            for country in self.countryList:
                if country.contains(keyword, keywordDictionary[keyword]):
                    listOfPossibleCountry.append(country.name)
            listOfPossibleCountryByKeyword.append(listOfPossibleCountry)
        return listOfPossibleCountryByKeyword
