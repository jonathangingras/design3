from unittest import TestCase
from naturalLanguagePython.countryService.dictionaryValueInformationFormatter import DictionaryValueInformationFormatter
__author__ = 'Antoine'


class TestDictionaryValueInformationFormatter(TestCase):

    def setUp(self):
        self.dictionaryValueInformationFormatter = DictionaryValueInformationFormatter()
    def test_formatValueInformationForPopulationKeywordWhenNumberIsSeparatedBySpaceShouldChangeValueInsideDictionaryToNumberWithoutSpace(self):
        dictionary = {"population": ["32 990"]}
        expectedReturnedDictionary = {"population": ["32990"]}
        self.dictionaryValueInformationFormatter.formatPopulationValue(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForPopulationKeywordWhenNumbersNotSeparatedBySpaceShouldNotChangeValueInsideDictionary(self):
        dictionary = {"population": ["32.990"]}
        expectedReturnedDictionary = {"population": ["32.990"]}
        self.dictionaryValueInformationFormatter.formatPopulationValue(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForPopulationKeywordWhenDictionaryNotContainingPopulationKeyShouldNotChangeDictionary(self):
        expectedReturnedDictionary = {"this not population": ["not an number"]}
        dictionary = expectedReturnedDictionary
        self.dictionaryValueInformationFormatter.formatPopulationValue(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForPopulationKeywordWhenHavingTwoValueShouldChangeOnlyTheSecondOne(self):
        expectedReturnedDictionary = {"population": ["population is not real", "32990"]}
        dictionary = {"population": ["population is not real", "32 990"]}
        self.dictionaryValueInformationFormatter.formatPopulationValue(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)
