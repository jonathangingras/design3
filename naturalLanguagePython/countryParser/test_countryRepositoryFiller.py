from unittest import TestCase

__author__ = 'Antoine'
from countryRepositoryFiller import CountryRepositoryDB, CountryRepositoryFiller,Country

class TestCountryRepositoryFiller(TestCase):

    def test_findingAParsedCountryByItsCapitalShouldReturnCountryName(self):
        countryRepository = CountryRepositoryDB()
        countryDBFiller = CountryRepositoryFiller(countryRepository)
        countryDBFiller.addCountriesToTheRepository()
        self.assertEqual(countryRepository.searchCountries({'Capital': 'Paris'}), ['France'])