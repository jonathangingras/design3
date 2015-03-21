__author__ = 'Antoine'
from unittest import TestCase

from naturalLanguagePython.countryParser.countryRepositoryFiller import CountryRepositoryDB, CountryRepositoryFiller
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory

#Acceptance  testing is done with this file
class TestCountryRepositoryFiller(TestCase):

    def setUp(self):
        path = "C:\Users\Antoine\Documents\\design3\\naturalLanguagePython"
        self.countryRepository = CountryRepositoryDB()
        self.countryDBFiller = CountryRepositoryFiller(self.countryRepository)
        self.countryDBFiller.addCountriesToTheRepository(path)
        self.searchStrategyFactory = SearchStrategyFactory()

    def test_searchAParsedCountryByItsCapitalShouldReturnCountryName(self):
        expectedCountryList = [['France']]
        wantedField = {'capital' : ['Paris']}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryByOttawaShouldReturnCanada(self):
        expectedCountryList = [["Canada"]]
        wantedField = {'capital': ['Ottawa']}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryByItsCapitalWhenNoCountryCorrespondingShouldReturnEmptyList(self):
        expectedCountryList = [[]]
        wantedField = {'capital' : ['Capitol City']}
        self.assertEqual(self.countryRepository.searchCountries(wantedField), expectedCountryList)

    def test_searchAParsedCountryByItsCapitalWithStartPortionAndEndPortionShouldReturnCountryName(self):
        expectedCountryList = [['Greece']]
        wantedFieldStartsWith = {'capital' : ['Ath']}
        wantedFieldEndsWith = {'capital' : ['ens']}
        searchStrategyStartsWith = self.searchStrategyFactory.createSearchStrategy("starts with")
        searchStrategyEndsWith = self.searchStrategyFactory.createSearchStrategy("ends with")
        self.assertEqual(self.countryRepository.searchCountries(wantedFieldStartsWith, searchStrategyStartsWith), expectedCountryList)
        self.assertEqual(self.countryRepository.searchCountries(wantedFieldEndsWith, searchStrategyEndsWith), expectedCountryList)

    def test_searchAParsedCountryByItsCapitalWithStartPortionShouldReturnPossibleCountryName(self):
        expectedCountryList = [['Somalia']]
        wantedFieldStartsWith = {'capital' : ['Moga']}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy("starts with")
        self.assertEqual(self.countryRepository.searchCountries(wantedFieldStartsWith, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsPopulationShouldReturnTheCountryName(self):
        expectedCountryList = [['Afghanistan']]
        wantedField = {"population": ["31822848"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsInternetCodeShouldReturnTheCountryName(self):
        expectedCountryList = [['United_Kingdom']]
        wantedField = {"internet country code" : [".uk"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByTheNumberOfTelephoneMainLinesInUseShouldReturnTheCountryName(self):
        expectedCountryList = [['West_Bank', 'Anguilla', 'Burma', 'Paraguay', 'Gaza_Strip']]
        expectedCountryList = [['Anguilla']]
        wantedField = {"telephones - main lines in use": ["6000"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy("Contains")
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByTheBirthRateShouldReturnNameOfPossibleCountry(self):
        expectedCountryList = [['Aruba']]
        wantedField = {"birth rate": ["12.65 births/1000"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsDeathRateShouldReturnNameOfPossibleCountry(self):
        expectedCountryList = [['Australia']]
        wantedField = {"death rate": ["7.07 deaths/1000"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsIndependenceDateShouldReturnNameOfPossibleCountry(self):
        expectedCountryList = [["Bahrain"]]
        wantedField = {"independence" : ["August 1971"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsNationalAnthemShouldReturnTheNameOfTheCountry(self):
        expectedCountryList = [["Egypt"]]
        wantedField = {"national anthem": ["Bilady, Bilady, Bilady"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsUnemploymentRateShouldReturnTheNameOfPossibleCountry(self):
        expectedCountryList = [["Ethiopia"]]
        wantedField = {"unemployment rate": ["17.5%"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsPopulationGrowthRateShouldReturnTheNameOfPossibleCountry(self):
        expectedCountryList = [["Japan", "Armenia"]]
        expectedCountryList[0].reverse()
        wantedField = {"population growth rate": ["-0.13%"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsNationalSymbolShouldReturnTheNameOfTheCountry(self):
        expectedCountryList = [["Saint_Martin", "Saint_Kitts_and_Nevis"]]
        expectedCountryList[0].reverse()
        wantedField = {"national symbol(s)": ["brown pelican"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByReligionShouldReturnTheNameOfPossibleCountry(self):
        expectedCountryList = [["Fiji", "World", "United_Arab_Emirates", "India", "Saudi_Arabia", "Canada"]]
        expectedCountryList = [['Canada', 'Fiji', 'India', 'Saudi_Arabia', 'United_Arab_Emirates']]
        wantedField = {"religions": ["Sikh"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsIndustriesShouldReturnTheNameOfPossibleCountry(self):
        expectedCountryList = [['South_Africa']]
        wantedField = {"industries": ["platinum", "gold", "chromium"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsExportPartnersShouldReturnTheNameOfPossibleCountry(self):
        expectedCountryList = [["Algeria", "Bangladesh"]]
        wantedField = {"exports - partners": ["Italy", "Canada", "France", "Spain"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(self.countryRepository.searchCountries(wantedField, searchStrategy), expectedCountryList)

    def test_searchAParsedCountryWhenSearchingByItsNationalSymbolShouldReturnTheNameOfPossibleCountry(self):
        expectedCountryList = [['Greenland']]
        wantedField = {"national symbol(s)": ["polar bear"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(expectedCountryList, self.countryRepository.searchCountries(wantedField, searchStrategy))

    def test_searchAParsedCountryWhenSearchingByPopulationOfMajorUrbanAreasShouldReturnTheNameOfPossibleCountry(self):
        expectedCountryList = [['Angola']]
        wantedField = {"major urban areas - population": ['5.068 million', '1.098 million']}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy()
        self.assertEqual(expectedCountryList, self.countryRepository.searchCountries(wantedField, searchStrategy))

    def test_searchAParsedCountyWhenSearchingByItsInflationRateBetweenShouldReturnTheNameOfPossibleCountry(self):
        expectedCountryList = [[]]
        wantedField = {"inflation rate (consumer prices)": ["0.4%", "0.6%"]}
        searchStrategy = self.searchStrategyFactory.createSearchStrategy("between")
        self.assertEqual(expectedCountryList, self.countryRepository.searchCountries(wantedField, searchStrategy))