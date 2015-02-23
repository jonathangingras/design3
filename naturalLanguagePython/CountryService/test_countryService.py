from unittest import TestCase
from naturalLanguagePython.CountryService.countryService import CountryService
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.SearchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
__author__ = 'Antoine'


class TestCountryService(TestCase):

    def setUp(self):
        self.countryService = CountryService()

    def test_creatingACountryServiceShouldCreateAnInstanceOfCountryRepositoryDB(self):
        expectedInstance = CountryRepositoryDB
        self.assertIsInstance(self.countryService.countryRepository, expectedInstance)

    def test_creatingACountryServiceShouldCreateAnInstanceOfSearchStrategyFactory(self):
        expectedInstance = SearchStrategyFactory
        self.assertIsInstance(self.countryService.searchStrategyFactory, expectedInstance)

    def test_searchingForACountryWhenHavingNoCountryInDatabaseShouldReturnNone(self):
        searchedInformation = {
            "Capital" : ["Paris"]
        }


