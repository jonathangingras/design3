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