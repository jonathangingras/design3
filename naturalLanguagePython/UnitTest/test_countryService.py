from unittest import TestCase
from mock import Mock
from naturalLanguagePython.CountryService.countryService import CountryService
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.CountryService.searchStrategyServiceFactory import SearchStrategyServiceFactory
from naturalLanguagePython.SearchInformationStrategy.searchEndsWith import SearchEndsWith
from naturalLanguagePython.CountryService.countryServiceException import CountryServiceException
from naturalLanguagePython.questionLanguageAnalyzer.questionAnalyzer import QuestionAnalyzer
__author__ = 'Antoine'


class TestCountryService(TestCase):

    def setUp(self):
        self.countryService = CountryService()
        self.countryService.questionAnalyzer.extractedImportantInformationsFromQuestion = Mock()

    def test_creatingACountryServiceShouldCreateAnInstanceOfCountryRepositoryDB(self):
        expectedInstance = CountryRepositoryDB
        self.assertIsInstance(self.countryService.countryRepository, expectedInstance)

    def test_creatingACountryServiceShouldCreateAnInstanceOfSearchStrategyFactory(self):
        expectedInstance = SearchStrategyServiceFactory
        self.assertIsInstance(self.countryService.searchStrategyServiceFactory, expectedInstance)

    def test_searchingForACountryWhenHavingTheSearchedCountryInsideTheRepositoryShouldReturnTheNameOfTheCountry(self):
        searchedInformation = {
            "Capital": ["aCapital"]
        }
        self.countryService.countryRepository.countryList = ["France"]
        self.countryService.countryRepository.searchCountries = Mock(return_value = ["France"])
        expectedNameOfCountry = "France"
        self.assertEqual(expectedNameOfCountry, self.countryService.searchCountry(searchedInformation))

    def test_searchingForACountryWhenHavingMoreSearchStrategyThanItemInsideTheSearchedInformationDictShouldRaiseAnSearchException(self):
        searchedInformation = {
            "Capital": ["aCapital"]
        }
        self.countryService.countryRepository.countryList = ["France"]
        wantedSearchStrategy = ["starts with", "ends with"]
        self.assertRaises(CountryServiceException, self.countryService.searchCountry, searchedInformation, wantedSearchStrategy)

    def test_analyzingAQuestionWhenTheReceivedStringIsNoneShouldRaiseException(self):
        receivedQuestion = None
        expectedRaisedError = CountryServiceException
        self.assertRaises(expectedRaisedError, self.countryService.analyzeQuestionFromAtlas, receivedQuestion)

    def test_analyzingAQuestionWhenTheReceivedStringIsAnEmptyStringShouldRaisesException(self):
        receivedQuestion = ""
        expectedRaisedError = CountryServiceException
        self.assertRaises(expectedRaisedError, self.countryService.analyzeQuestionFromAtlas, receivedQuestion)
