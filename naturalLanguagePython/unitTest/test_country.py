from unittest import TestCase
import unittest
from mock import Mock
from naturalLanguagePython.countryDomain.country import Country
from naturalLanguagePython.searchInformationStrategy.searchInformation import SearchInformation
__author__ = 'Antoine'


class TestCountry(TestCase):

    def setUp(self):
        self.dictionary = {'Capital': 'Paris'}
        self.nameOfCountry = 'France'
        self.country = Country(self.nameOfCountry, self.dictionary)

        dictionaryCategoryList = {'Capital':['Kiev', 'newKiev']}
        nameOfCountryWithCategoryList = 'Ukraine'
        self.countryWithListInsideCategory = Country(nameOfCountryWithCategoryList, dictionaryCategoryList)

    def test_countryHasNameAttribute(self):
        self.assertIsNotNone(self.country.name)

    def test_countryHasAnInformationDictionary(self):
        self.assertIsNotNone(self.country.informationDict)

    def test_containingWantedInformationReturnTrue(self):
        key = 'Capital'
        value = 'Paris'
        self.assertTrue(self.country.contains(key, value))

    def test_notContainingWantedInformationShouldReturnFalse(self):
        key = 'Capital'
        value = 'Kiew'
        self.assertFalse(self.country.contains(key, value))

    def test_containingWantedInformationShouldReturnTrueWhenHavingHavingMoreThanOneCategory(self):
        key = 'GDP'
        value = 10000
        self.country.informationDict[key] = value
        self.assertTrue(self.country.contains(key, value))

    def test_notContainingCategoryShouldReturnFalse(self):
        key = 'GDP'
        value = 10000
        self.assertFalse(self.country.contains(key, value))

    def test_containingWantedInformationInsideListWhenHavingOneInformationCategoryInsideListShouldReturnTrue(self):
        key = 'Capital'
        value = 'newKiev'
        self.assertTrue(self.countryWithListInsideCategory.contains(key, value))

    def test_notContainingWantedInformationInsideListWhenHavingOneInformationCategoryInsideListShouldReturnFalse(self):
        key = 'Capital'
        value = 'Paris'
        self.assertFalse(self.countryWithListInsideCategory.contains(key, value))


if __name__ == '__main__':
    unittest.main()