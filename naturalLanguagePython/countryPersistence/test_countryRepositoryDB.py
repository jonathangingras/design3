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
        expectedListOfNameOfTheSearchedCountry = ['Aruba']
        self.countryRepository.addCountry(self.firstCountryToAdd)
        self.assertEqual(self.countryRepository.searchCountries(dictionaryOfKeyword), expectedListOfNameOfTheSearchedCountry)

    def test_searchCountryToDatabaseWithTwoPossibleCountry(self):
        self.countryRepository.addCountry(self.firstCountryToAdd)
        self.countryRepository.addCountry(self.secondCountryToAdd)
        expectedListOfNameOfTheSearchedCountry = ['Aruba', 'France']
        keywordSearchedDictionary = {'Capital' : 'Paris'}
        self.assertEqual(self.countryRepository.searchCountries(keywordSearchedDictionary), expectedListOfNameOfTheSearchedCountry)

    def test_searchingCountryWithOneFieldWhenCountryContainsTwoInformationCategoryShouldReturnCountryNameInList(self):
        countryWithTwoCategory = Country('Canada', {'Capital': 'Ottawa', 'GDP':1000000})
        self.countryRepository.addCountry(self.firstCountryToAdd)
        self.countryRepository.addCountry(countryWithTwoCategory)
        expectedListOfNameOfTheSearchedCountry = ['Canada']
        keywordSearchedDictionary = {'GDP': 1000000}
        self.assertEqual(self.countryRepository.searchCountries(keywordSearchedDictionary), expectedListOfNameOfTheSearchedCountry)
