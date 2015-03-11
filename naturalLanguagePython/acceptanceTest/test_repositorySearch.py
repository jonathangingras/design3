from unittest import TestCase
from mock import Mock
from naturalLanguagePython.countryService.repositorySearch import RepositorySearch
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.countryParser.countryRepositoryFiller import CountryRepositoryFiller
__author__ = 'Antoine'


class TestRepositorySearch(TestCase):

    def setUp(self):
        self.repositorySearch = RepositorySearch()
        self.repository = CountryRepositoryDB()
        self.countryFiller = CountryRepositoryFiller(self.repository)

    def test_searchAPossibleCountryInRepositoryWhenTheSearchStrategyIsNoneShouldReturnAName(self):
        searchedInformationDict = {"capital": "Ottawa"}
        expectedNameOfCountry = ["Canada"]
        self.assertEqual(expectedNameOfCountry, self.repositorySearch.searchPossiblesCountryInRepository(self.repository, searchedInformationDict, ['Contains']))
