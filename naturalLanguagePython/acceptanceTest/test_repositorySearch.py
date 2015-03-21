from unittest import TestCase

from mock import Mock

from naturalLanguagePython.countryService.repositorySearch import RepositorySearch
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB

__author__ = 'Antoine'


class TestRepositorySearch(TestCase):

    def setUp(self):
        self.repositorySearch = RepositorySearch()
        self.repository = CountryRepositoryDB()
        self.repository.searchCountries = Mock()

    def test_searchAPossibleCountryInRepositoryWhenTheSearchStrategyIsNoneShouldReturnAName(self):
        searchedInformationDict = {"capital": "Ottawa"}
        expectedNameOfCountry = ["Canada"]
        searchStrategyDictionary = {"capital": ['Contains']}
        self.repository.searchCountries.side_effect = ['Canada']
        self.assertEqual(expectedNameOfCountry, self.repositorySearch.searchPossiblesCountryInRepository(self.repository, searchedInformationDict, searchStrategyDictionary))
