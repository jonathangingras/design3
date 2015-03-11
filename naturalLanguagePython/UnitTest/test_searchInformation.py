from unittest import TestCase

__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchContains import SearchContains
from naturalLanguagePython.searchInformationStrategy.searchStartsWith import SearchStartsWith
from naturalLanguagePython.searchInformationStrategy.searchEndsWith import SearchEndsWith

class TestSearchInformation(TestCase):
    def setUp(self):
        self.searchMethodStartsWith = SearchStartsWith()
        self.searchMethodEndsWith = SearchEndsWith()
        self.searchMethodContains = SearchContains()
        self.dictionaryForSearchMethodTestWithoutList = {"capital": ["Paris"]}
        self.dictionaryForSearchMethodTestWithList = {"capital" : ["In the same continent", "Paris"],
                                                      "Population": ["Estimate of 100000"]}

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
        wantedInformation = ["Paris"]
        self.assertTrue(self.searchMethodContains.findInformationList(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInformation))

    def test_notFindingCorrespondingInformationInsideDictionaryWithTheContainsStrategyShouldReturnFalse(self):
        keyword = "capital"
        wantedInformation = "Kiev"
        self.assertFalse(self.searchMethodContains.findInformation(self.dictionaryForSearchMethodTestWithoutList, keyword, wantedInformation))

    def test_findingCorrespondingNumberInsideDictionaryWithTheContainsStrategyShouldReturnTrue(self):
        keyword = "Population"
        wantedInformation = "100000"
        self.assertTrue(self.searchMethodContains.findInformation(self.dictionaryForSearchMethodTestWithList, keyword, wantedInformation))

    def test_notFindingCorrespondingNumberInsideDictionaryWithTheContainsStrategyShouldReturnFalse(self):
        keyword = "Population"
        wantedInformation = "2100000"
        self.assertFalse(self.searchMethodContains.findInformation(self.dictionaryForSearchMethodTestWithList, keyword, wantedInformation))
