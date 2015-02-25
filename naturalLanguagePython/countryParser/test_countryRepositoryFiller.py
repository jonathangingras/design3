__author__ = 'Antoine'
from unittest import TestCase
from naturalLanguagePython.countryParser.countryRepositoryFiller import CountryRepositoryDB, CountryRepositoryFiller
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
#Acceptance  testing is done with this file
class TestCountryRepositoryFiller(TestCase):

    def setUp(self):
        self.countryRepository = CountryRepositoryDB()
        self.countryDBFiller = CountryRepositoryFiller(self.countryRepository)
        self.countryDBFiller.addCountriesToTheRepository()
        self.searchStrategyFactory = SearchStrategyFactory()

    def test_searchAParsedCountryByItsCapitalShouldReturnCountryName(self):
        expectedCountryList = [['France']]
        wantedField = {'Capital' : 'Paris'}
        self.assertEqual(self.countryRepository.searchCountries(wantedField), expectedCountryList)

    def test_searchAParsedCountryByItsCapitalWhenNoCountryCorrespondingShouldReturnEmptyList(self):
        expectedCountryList = [[]]
        wantedField = {'Capital' : 'Capitol City'}
        self.assertEqual(self.countryRepository.searchCountries(wantedField), expectedCountryList)

    def test_searchAParsedCountryByItsCapitalWithStartPortionAndEndPortionShouldReturnCountryName(self):
        expectedCountryList = [['Greece']]
        wantedFieldStartsWith = {'Capital' : 'Ath'}
        wantedFieldEndsWith = {'Capital' : 'ens'}
        searchStrategyStartsWith = self.searchStrategyFactory.createSearchStrategy("starts with")
        searchStrategyEndsWith = self.searchStrategyFactory.createSearchStrategy("ends with")
        self.assertEqual(self.countryRepository.searchCountries(wantedFieldStartsWith, searchStrategyStartsWith), expectedCountryList)
        self.assertEqual(self.countryRepository.searchCountries(wantedFieldEndsWith, searchStrategyEndsWith), expectedCountryList)

    def test_searchAParsedCountryByItsCapitalWithStartPortionShouldReturnPossibleCountryName(self):
        expectedCountryList = [['Somalia']]
        wantedFieldStartsWith = {'Capital' : 'Moga'}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy("starts with")
        self.assertEqual(self.countryRepository.searchCountries(wantedFieldStartsWith, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsPopulationShouldReturnTheCountryName(self):
        expectedCountryList = [['Afghanistan']]
        wantedField = {"Population": "31,822,848"}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsInternetCodeShouldReturnTheCountryName(self):
        expectedCountryList = [['United_Kingdom']]
        wantedField = {"Internet country code" : ".uk"}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByTheNumberOfTelephoneMainLinesInUseShouldReturnTheCountryName(self):
        expectedCountryList = [['Anguilla', 'Burma', 'Gaza_Strip', 'Paraguay', 'West_Bank']]
        wantedField = {"Telephones - main lines in use": "6,000"}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByTheBirthRateShouldReturnNameOfPossibleCountry(self):
        expectedCountryList = [['Aruba']]
        wantedField = {"Birth rate": "12.65 births/1,000"}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsDeathRateShouldReturnNameOfPossibleCountry(self):
        expectedCountryList = [['Australia']]
        wantedField = {"Death rate": "7.07 deaths/1,000"}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)