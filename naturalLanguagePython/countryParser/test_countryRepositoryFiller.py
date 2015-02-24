from unittest import TestCase
__author__ = 'Antoine'
from naturalLanguagePython.countryParser.countryRepositoryFiller import CountryRepositoryDB, CountryRepositoryFiller
#Acceptance  testing is done with this file
class TestCountryRepositoryFiller(TestCase):

    def setUp(self):
        self.countryRepository = CountryRepositoryDB()
        self.countryDBFiller = CountryRepositoryFiller(self.countryRepository)
        self.countryDBFiller.addCountriesToTheRepository()

    def test_findingAParsedCountryByItsCapitalShouldReturnCountryName(self):
        expectedCountryList = [['France']]
        wantedField = {'Capital' : 'Paris'}
        self.assertEqual(self.countryRepository.searchCountries(wantedField), expectedCountryList)

    def test_findingAParsedCountryByItsCapitalWhenNoCountryCorrespondingShouldReturnEmptyList(self):
        expectedCountryList = [[]]
        wantedField = {'Capital' : 'Capitol City'}
        self.assertEqual(self.countryRepository.searchCountries(wantedField), expectedCountryList)

    def test_findingAParsedCountryByItsCapitalWithStartPortionAndEndPortionShouldReturnCountryName(self):
        expectedCountryList = [['Greece']]
        wantedField = {'Capital' : 'Ath', 'Capital' : 'ens'}
        self.assertEqual(self.countryRepository.searchCountries(wantedField), expectedCountryList)
        pass