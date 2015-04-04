from unittest import TestCase
from mock import Mock
from naturalLanguagePython.countryDomain.country import Country
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
__author__ = 'Antoine'


class TestCountryRepositoryDB(TestCase):

    def setUp(self):
        self.countryRepository = CountryRepositoryDB()
        self.firstCountryToAdd = Country('Aruba', {'Capital': ['Paris']})
        self.secondCountryToAdd = Country('France', {'Capital': ['Paris']})
        self.countryWithTwoCategory = Country('Canada', {'Capital': ['Ottawa'], 'GDP': [1000000]})
        self.countryWithTwoCategory.contains = Mock(return_value = True)
        self.firstCountryToAdd.contains = Mock(return_value = True)
        self.secondCountryToAdd.contains = Mock(return_value = True)
        self.searchStrategy = SearchInformation()
        self.searchStrategy.findInformation = Mock(return_value = True)

    def test_addCountryToTheDatabase(self):
        self.assertRaises(self.countryRepository.addCountry(self.firstCountryToAdd), None)

    def test_searchCountryToTheDatabase(self):
        keywordSearchedDictionary = {'Capital':['Paris']}
        expectedListOfNameOfTheSearchedCountry = [['Aruba']]
        self.countryRepository.addCountry(self.firstCountryToAdd)
        self.assertEqual(self.countryRepository.searchCountries(keywordSearchedDictionary), expectedListOfNameOfTheSearchedCountry)

    def test_searchCountryToDatabaseWithTwoPossibleCountry(self):
        keywordSearchedDictionary = {'Capital' : ['Paris']}
        expectedListOfNameOfTheSearchedCountry = [['Aruba', 'France']]
        self.countryRepository.addCountry(self.firstCountryToAdd)
        self.countryRepository.addCountry(self.secondCountryToAdd)
        self.assertEqual(self.countryRepository.searchCountries(keywordSearchedDictionary), expectedListOfNameOfTheSearchedCountry)

    def test_searchingCountryWithOneFieldWhenCountryContainsTwoInformationCategoryShouldReturnCountryNameInList(self):
        expectedListOfNameOfTheSearchedCountry = [['Canada']]
        keywordSearchedDictionary = {'GDP': [1000000]}
        self.firstCountryToAdd.contains = Mock(return_value = False)
        self.countryRepository.addCountry(self.firstCountryToAdd)
        self.countryRepository.addCountry(self.countryWithTwoCategory)
        self.assertEqual(self.countryRepository.searchCountries(keywordSearchedDictionary), expectedListOfNameOfTheSearchedCountry)

    def test_searchingCountryWithTwoFieldsWhenCountryContainsTwoInformationCategoryShouldReturnCountryNameInList(self):
        keywordSearchedDictionary = {'GDP': [1000000], 'Capital' : ['Ottawa']}
        expectedListOfNameOfTheSearchedCountry = [['Canada'], ['Canada']]
        self.countryRepository.addCountry(self.countryWithTwoCategory)
        self.assertEqual(self.countryRepository.searchCountries(keywordSearchedDictionary), expectedListOfNameOfTheSearchedCountry)

    def test_searchingCountryWhenUsingASearchStrategyShouldReturnTheNameOfCountry(self):
        keywordSearchedInDictionary = {'Capital' : ['Ottawa']}
        expectedListOfNameOfTheSearchCountry = [['Canada']]
        self.countryRepository.addCountry(self.countryWithTwoCategory)
        self.assertEqual(self.countryRepository.searchCountries(keywordSearchedInDictionary, self.searchStrategy), expectedListOfNameOfTheSearchCountry)
