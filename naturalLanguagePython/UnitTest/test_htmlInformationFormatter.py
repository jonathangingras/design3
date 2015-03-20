from unittest import TestCase
from bs4 import NavigableString
from naturalLanguagePython.htmlExtractor.htmlInformationFormatter import HtmlInformationFormatter
__author__ = 'Antoine'


class TestHtmlInformationFormatter(TestCase):
    def setUp(self):
        self.htmlInformationFormatter = HtmlInformationFormatter()

    def test_formattingTheInformationKeyWhenTheTagToExtractTheKeyIsNoneShouldReturnNone(self):
        tag = None
        self.assertIsNone(self.htmlInformationFormatter.informationKeyFormatting(tag))

    def test_formattingTheInformationKeyWhenTheTagToExtractTheKeyIsEqualToCountryComparisonToTheWorldShouldReturnNone(self):
        tag = NavigableString("country comparison to the world")
        self.assertIsNone(self.htmlInformationFormatter.informationKeyFormatting(tag))

    def test_formattingTheInformationKeyWhenTheTagToExtractContainsDoubleDotsShouldReturnTheTagWithoutTheDoubleDots(self):
        tag = NavigableString("Capital: ")
        expectedTagString = "Capital"
        self.assertEqual(self.htmlInformationFormatter.informationKeyFormatting(tag), expectedTagString)

    def test_formattingTheInformationKeyWhenTheTagHasAnUnicodeEncodeErrorShouldReturnNone(self):
        tag = NavigableString(u"allo\u2026'")
        self.assertIsNone(self.htmlInformationFormatter.informationKeyFormatting(tag))

    def test_formattingNumberValueFromWorldFactBookWhenHavingNumberSeparatedByComaShouldReturnTheStringWithoutTheComa(self):
        stringWithNumber = "34,834,841 (July 2014 est.)"
        expectedReturnedString = "34834841 (July 2014 est.)"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatNumberSeparatedByComaFromWorldFactBook(stringWithNumber))

    def test_formattingNumberValueFromWorldFactBookWhenHavingNumbersSeparatedByDotsShouldReturnTheNumberUnchanged(self):
        stringWithNumberWithComaSeparatedValue = "34.834.841 (July 2014 est.)"
        expectedReturnedString = "34.834.841 (July 2014 est.)"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatNumberSeparatedByComaFromWorldFactBook(stringWithNumberWithComaSeparatedValue))

    def test_formattingNumberValueFromWorldFactBookWhenHavingNumbersSeparatedBySpaceShouldReturnTheNumberUnchanged(self):
        stringWithNumberWithSpaceSeparatedValue = "34 834 841 (July 2014 est.)"
        expectedReturnedString  ="34 834 841 (July 2014 est.)"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatNumberSeparatedByComaFromWorldFactBook(stringWithNumberWithSpaceSeparatedValue))

    def test_formattingNumberValueFromWorldFactBookWhenHavingStringElementSeparatedByComaShouldReturnTheStringUnchanged(self):
        stringWithoutNumber = "Bilady, Bilady, Bilady"
        expectedReturnedString = "Bilady, Bilady, Bilady"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatNumberSeparatedByComaFromWorldFactBook(stringWithoutNumber))

    def test_formattingNameOfMajorUrbanAreaWhenHavingUpperCaseStringShouldReturnCapitalizedString(self):
        upperCaseString = "STRING"
        expectedReturnedString = "String"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatMajorUrbanAreaValue(upperCaseString))

    def test_formattingNameOfMajorUrbanAreaWhenHavingLowerCaseStringShouldReturnCapitalizeString(self):
        lowerCaseString = "string"
        expectedReturnedString = "String"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatMajorUrbanAreaValue(lowerCaseString))

    def test_formattingNameOfMajorUrbanAreaWhenHavingCapitalizeStringShouldReturnUnchangedString(self):
        capitalizeString = "String"
        expectedReturnedString = "String"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatMajorUrbanAreaValue(capitalizeString))

    def test_formattingNameOfMajorUrbanAreaWhenHavingWordsInStringShouldReturnFormattedString(self):
        string = "STRING, string"
        expectedReturnedString = "String, String"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatMajorUrbanAreaValue(string))

    def test_formattingNameOfMajorUrbanAreaWhenHavingNumberInsideStringShouldReturnFormattedStringWithOnlyWordChanged(self):
        stringWithNumber = "string 199999"
        expectedReturnedString = "String 199999"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatMajorUrbanAreaValue(stringWithNumber))

    def test_formatNameOfMajorUrbanAreaWhenHavingMillionInStringShouldNotChangeMillionFormat(self):
        stringWithMillion = "string 19999 million"
        expectedReturnedString = "String 19999 million"
        self.assertEqual(expectedReturnedString, self.htmlInformationFormatter.formatMajorUrbanAreaValue(stringWithMillion))