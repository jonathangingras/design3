from unittest import TestCase
from countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.CountryDomain.Country import Country
__author__ = 'Antoine'


class TestCountryRepositoryDB(TestCase):

    def setUp(self):
        self.countryRepository = CountryRepositoryDB()
        self.firstCountryToAdd = Country('Aruba', {'Capital':'Paris'})
        self.secondCountryToAdd = Country('France', {'Capital':'Paris'})

    def test_addCountryToTheDatabase(self):
        countryToAdd = Country('Aruba', {'Capital':'Paris'})
        self.assertRaises(self.countryRepository.addCountry(countryToAdd), None)

    def test_searchCountryToTheDatabase(self):
        dictionaryOfKeyword = {'Capital':'Paris'}
        listOfNameOfTheSearchedCountry = ['Aruba']
        self.countryRepository.addCountry(self.firstCountryToAdd)
        self.assertEquals(self.countryRepository.searchCountries(dictionaryOfKeyword), listOfNameOfTheSearchedCountry)

    def test_searchCountryToDatabaseWithTwoPossibleCountry(self):
        self.countryRepository.addCountry(self.firstCountryToAdd)
        self.countryRepository.addCountry(self.secondCountryToAdd)
        listOfNameOfTheSearchedCountry = ['Aruba', 'France']
        dictionaryOfKeyword = {'Capital' : 'Paris'}
        self.assertEquals(self.countryRepository.searchCountries(dictionaryOfKeyword), listOfNameOfTheSearchedCountry)