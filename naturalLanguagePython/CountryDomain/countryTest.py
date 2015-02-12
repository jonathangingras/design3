from unittest import TestCase
from Country import Country


__author__ = 'Antoine'


class TestCountry(TestCase):

    def setUp(self):
        self.dictionary = {'capital': 'Paris'}
        self.nameOfCountry = 'Aruba'
        self.country = Country(self.nameOfCountry, self.dictionary)

    def test_countryContainsNameAttribute(self):
        self.assertIsNotNone(self.country.name)

    def test_countryNameStartWithAUpperCase(self):
        self.assertEquals(self.country.name, self.nameOfCountry)

    def test_countryContainsAnInformationDictionary(self):
        self.assertIsNotNone(self.country.informationDict)

    def test_countryInformationDictionaryContainsOneInformation(self):
        self.assertEquals(self.country.informationDict, self.dictionary)
