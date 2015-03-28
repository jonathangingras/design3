from unittest import TestCase
from mock import Mock
from naturalLanguagePython.htmlExtractor.htmlCountryDictionaryFormatter import HtmlCountryDictionaryFormatter
__author__ = 'Antoine'


class TestHtmlCountryDictionaryFormatter(TestCase):

    def setUp(self):
        self.htmlCountryDictionaryFormatter = HtmlCountryDictionaryFormatter()

    def test_formatMajorUrbanAreaValueWhenDictionaryNotContainingMajorUrbanAreaKeywordShouldReturnUnchangedDictionary(self):
        dictionary = {"population": ["a population"]}
        expectedReturnedDictionary = dictionary
        self.assertEqual(expectedReturnedDictionary, self.htmlCountryDictionaryFormatter.formatMajorUrbanAreaValue(dictionary))

    def test_formatMajorUrbanAreaValueWhenDictionaryContainsMajorUrbanAreaKeywordShouldReturnFormattedDictionary(self):
        dictionary = {"major urban areas - population": ["SANTIAGO, Vespacio"]}
        formattedListElement = "Santiago, Vespacio"
        expectedReturnedDictionary = {"major urban areas - population": [formattedListElement]}
        self.htmlCountryDictionaryFormatter.htmlInformationFormatter.formatMajorUrbanAreaValue = Mock(return_value = formattedListElement)
        self.assertEqual(expectedReturnedDictionary, self.htmlCountryDictionaryFormatter.formatMajorUrbanAreaValue(dictionary))