from unittest import TestCase
from naturalLanguagePython.countryService.searchResultAnalyzer import SearchResultAnalyzer

__author__ = 'Antoine'


class TestSearchResultAnalyzer(TestCase):
    def setUp(self):
        self.searchResultAnalyzer = SearchResultAnalyzer()

    def test_findPossibleCountryNameInResultByKeywordWhenHavingOneListShouldReturnTheFirstElementOfTheList(self):
        listOfPossibleCountryName = [["first element"]]
        expectedReturnCountryNameList = ["first element"]
        self.assertEqual(expectedReturnCountryNameList, self.searchResultAnalyzer.findPossibleCountryNameInSearchResultByKeyword(listOfPossibleCountryName))

    def test_findPossibleCountryNameInSearchResultByKeywordWhenHavingTwoListWithoutAnElementInBothListShouldReturnAnEmptyList(self):
        listOfPossibleCountryName = [["first element"], ["second element"]]
        expectedReturnCountryNameList = []
        self.assertEqual(expectedReturnCountryNameList, self.searchResultAnalyzer.findPossibleCountryNameInSearchResultByKeyword(listOfPossibleCountryName))

    def test_findPossibleCountryNameInSearchResultByKeywordWhenHavingTwoListWithAnElementInBothListShouldReturnListWithTheCountryName(self):
        listOfPossibleCountryName = [["France", "Canada"], ["Canada"]]
        expectedReturnCountryNameList = ["Canada"]
        self.assertEqual(expectedReturnCountryNameList, self.searchResultAnalyzer.findPossibleCountryNameInSearchResultByKeyword(listOfPossibleCountryName))