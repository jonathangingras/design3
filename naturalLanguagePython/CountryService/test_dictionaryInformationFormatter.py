from unittest import TestCase
from naturalLanguagePython.countryService.dictionaryInformationFormatter import DictionaryInformationFormatter
__author__ = 'Antoine'


class TestDictionaryInformationFormatter(TestCase):

    def setUp(self):
        path = "C:\Users\Antoine\Documents\\design3\\naturalLanguagePython"
        self.dictionaryInformationFormatter = DictionaryInformationFormatter(path)

    def test_changingKeywordOfDictionaryWhenReceivedExportPartnersKeywordShouldReturnDictionaryWithExportUnionMarkPartners(self):
        receivedDictionary = {"export partners": "aPartner"}
        expectedDictionary = {"exports - partners": "aPartner"}
        self.assertEqual(expectedDictionary, self.dictionaryInformationFormatter.formatDictionary(receivedDictionary))

    def test_changingKeywordOfDictionaryWhenReceivedACorrectlyFormattedDictionaryShouldReturnTheReceivedDictionary(self):
        receivedDictionary = {"capital": "aCapital"}
        expectedDictionary = {"capital": "aCapital"}
        self.assertEqual(expectedDictionary, self.dictionaryInformationFormatter.formatDictionary(receivedDictionary))