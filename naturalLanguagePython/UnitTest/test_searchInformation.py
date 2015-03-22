from unittest import TestCase

__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.searchInformationStrategy.searchStartsWith import SearchStartsWith
from naturalLanguagePython.searchInformationStrategy.searchEndsWith import SearchEndsWith
from naturalLanguagePython.searchInformationStrategy.searchBetween import SearchBetween


class TestSearchInformation(TestCase):
    def setUp(self):
        self.searchMethodStartsWith = SearchStartsWith()
        self.searchMethodEndsWith = SearchEndsWith()
        self.searchMethodContains = SearchContains()
        self.searchMethodBetween = SearchBetween()
        self.dictionaryForSearchMethodTestWithoutList = {"capital": ["Paris"]}
        self.dictionaryForSearchMethodTestWithList = {"capital" : ["In the same continent", "Paris"],
                                                      "Population": ["Estimate of 100000"]}
        self.dictionaryForInteger = {"population": ["12345"]}
        self.dictionaryForFloat = {"population": ["1.50"]}
        self.dictionaryForFloatWithMillion = {"population": ["1.50 million"]}

    #Starting test for the between search strategy
    def test_findingCorrespondingInformationInsideDictionaryWhenUsingTheBetweenSearchStrategyShouldReturnTrue(self):
        keyword = "population"
        wantedInformation = ["12344", "12346"]
        self.assertTrue(self.searchMethodBetween.findInformation(self.dictionaryForInteger, keyword, wantedInformation))

    def test_findingCorrespondingInformationInsideDictionaryWhenUsingBetweenSearchStrategyAndAGapOfMoreThan10ShouldReturnTrue(self):
        keyword = "population"
        wantedInformation = ["12334", "12356"]
        self.assertTrue(self.searchMethodBetween.findInformation(self.dictionaryForInteger, keyword, wantedInformation))

    def test_notFindingCorrespondingInformationWhenUsingBetweenSearchStrategyShouldReturnFalse(self):
        keyword = "population"
        wantedInformation = ["12334", "12344"]
        self.assertFalse(self.searchMethodBetween.findInformation(self.dictionaryForInteger, keyword, wantedInformation))

    def test_findingCorrespondingInformationWhenUsingBetweenSearchStrategyWithFloatNumberShouldReturnTrue(self):
        keyword = "population"
        wantedInformation = ["1.40", "1.60"]
        self.assertTrue(self.searchMethodBetween.findInformation(self.dictionaryForFloat, keyword, wantedInformation))

    # def test_notFindingCorrespondingInformationWhenUsingBetweenSearchStrategyWithFloatNumberShouldReturnFalse(self):
    #     keyword = "population"
    #     wantedInformation = ["1.40", "1.49"]
    #     self.assertFalse(self.searchMethodBetween.findInformation(self.dictionaryForFloat, keyword, wantedInformation))
    # def test_findingCorrespondingInformationWhenUsingBetweenSearchStrategyWithFloatNumberFollowedByMillionShouldReturnTrue(self):
    #     keyword = "population"
    #     wantedInformation = ["1.40 million", "1.60 million"]
    #     self.assertTrue(self.searchMethodBetween.findInformation(self.dictionaryForFloatWithMillion, keyword, wantedInformation))




