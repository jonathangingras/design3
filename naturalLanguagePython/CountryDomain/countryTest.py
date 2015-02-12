from unittest import TestCase
from Country import Country
__author__ = 'Antoine'


class TestCountry(TestCase):

    def test_countryContainsAName(self):
        country = Country()
        self.assertEqual(country.name, 'a')
    pass