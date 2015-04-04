import os
from unittest import TestCase
from naturalLanguagePython.countryService.dictionaryInformationKeywordFormatter import DictionaryInformationFormatter
__author__ = 'Antoine'


class TestDictionaryInformationFormatter(TestCase):

    def setUp(self):
        path = os.getcwd()
        self.dictionaryInformationFormatter = DictionaryInformationFormatter(path)

    def test_changingKeywordOfDictionaryWhenReceivedExportPartnersKeywordShouldReturnDictionaryWithExportUnionMarkPartners(self):
        receivedDictionary = {"export partners": "aPartner"}
        expectedDictionary = {"exports - partners": "aPartner"}
        self.assertEqual(expectedDictionary, self.dictionaryInformationFormatter.formatDictionary(receivedDictionary))

    def test_changingKeywordOfDictionaryWhenReceivedACorrectlyFormattedDictionaryShouldReturnTheReceivedDictionary(self):
        receivedDictionary = {"capital": "aCapital"}
        expectedDictionary = {"capital": "aCapital"}
        self.assertEqual(expectedDictionary, self.dictionaryInformationFormatter.formatDictionary(receivedDictionary))