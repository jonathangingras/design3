from unittest import TestCase

__author__ = 'Antoine'
from naturalLanguagePython.SearchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.SearchInformationStrategy.searchStartsWith import SearchStartsWith
from naturalLanguagePython.SearchInformationStrategy.searchEndsWith import SearchEndsWith

class TestSearchInformation(TestCase):
    def setUp(self):
        self.searchMethodStartsWith = SearchStartsWith()
        self.searchMethodEndsWith = SearchEndsWith()
        self.searchMethodContains = SearchContains()
        self.dictionaryForSearchMethodTestWithoutList = {"capital": ["Paris"]}
        self.dictionaryForSearchMethodTestWithList = {"capital" : ["In the same continent", "Paris"]}

    def test_findingCorrespondingInformationInsideDictionaryWithTheStartsWithRegexShouldReturnTrue(self):
        keyword = "capital"
        wantedInformation = "Pa"
        self.assertTrue(self.searchMethodStartsWith.findInformation(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInformation))

    def test_notFindingCorrespondingInformationInsideDictionaryWhithTheStartsWithRegexShouldReturnFalse(self):
        keyword = "capital"
        wantedInformation = "Ki"
        self.assertFalse(self.searchMethodStartsWith.findInformation(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInformation))

    def test_findingCorrespondingInformationInsideDictionaryWithListWithTheStartsWithRegexShouldReturnTrue(self):
        keyword = "capital"
        wantedInformation = "Pa"
        self.assertTrue(self.searchMethodStartsWith.findInformation(self.dictionaryForSearchMethodTestWithList, keyword, wantedInformation))

    def test_notFindingCorrespondingInformationInsideDictionaryWithListWithTheStartsWithRegexShouldReturnFalse(self):
        keyword = "capital"
        wantedInformation = "Ki"
        self.assertFalse(self.searchMethodStartsWith.findInformation(self.dictionaryForSearchMethodTestWithList, keyword, wantedInformation))

    def test_notHavingKeyInsideDictionaryWhenSearchingWithTheStartsWithSearchShouldReturnFalse(self):
        keyword = "Population"
        wantedInforamtion = "100000"
        self.assertFalse(self.searchMethodStartsWith.findInformation(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInforamtion))

    #Starting test for the ends with search strategy

    def test_findingCorrespondingInformationInsideDictionaryWithTheEndsWithStrategyShouldReturnTrue(self):
        keyword = "capital"
        wantedInformation = "is"
        self.assertTrue(self.searchMethodEndsWith.findInformation(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInformation))

    def test_notFindingCorrespondingInformationInsideDictionaryWithTheEndsWithStrategyShouldReturnFalse(self):
        keyword = "capital"
        wantedInformation = "ev"
        self.assertFalse(self.searchMethodEndsWith.findInformation(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInformation))

    #Starting test for the contains search strategy
    def test_findingCorrespondingInformationInsideDictionaryWithTheContainsStrategyShouldReturnTrue(self):
        keyword = "capital"
        wantedInformation = "Paris"
        self.assertTrue(self.searchMethodContains.findInformation(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInformation))

    def test_notFindingCorrespondingInformationInsideDictionaryWithTheContainsStrategyShouldReturnFalse(self):
        keyword = "capital"
        wantedInformation = "Kiev"
        self.assertFalse(self.searchMethodContains.findInformation(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInformation))