from unittest import TestCase
from naturalLanguagePython.countryService.dictionaryValueInformationFormatter import DictionaryValueInformationFormatter
__author__ = 'Antoine'


class TestDictionaryValueInformationFormatter(TestCase):

    def setUp(self):
        self.dictionaryValueInformationFormatter = DictionaryValueInformationFormatter()
    def test_formatValueInformationForPopulationKeywordWhenNumberIsSeparatedBySpaceShouldChangeValueInsideDictionaryToNumberWithoutSpace(self):
        dictionary = {"population": ["32 990"]}
        expectedReturnedDictionary = {"population": ["32990"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForPopulationKeywordWhenNumbersNotSeparatedBySpaceShouldNotChangeValueInsideDictionary(self):
        dictionary = {"population": ["32.990"]}
        expectedReturnedDictionary = {"population": ["32.990"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForPopulationKeywordWhenDictionaryNotContainingPopulationKeyShouldNotChangeDictionary(self):
        expectedReturnedDictionary = {"this not population": ["not","an", "number"]}
        dictionary = expectedReturnedDictionary
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForPopulationKeywordWhenHavingTwoValueShouldChangeOnlyTheSecondOne(self):
        expectedReturnedDictionary = {"population": ["population is not real", "32990"]}
        dictionary = {"population": ["population is not real", "32 990"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForSlashWhenHavingNoSlashShouldReturnUnchangedValue(self):
        dictionary = {"population": ["a population"]}
        expectedReturnedDictionary = {"population": ["a population"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForSlashWhenHavingASlashSeparatedByASpaceShouldReturnTheStringWithSlashWithoutSpace(self):
        dictionary = {"population": ["10 more/ 1000 population"]}
        expectedReturnedDictionary = {"population": ["10 more/1000 population"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForLanguageKeywordWhenHavingAllLowerCaseWordShouldReturnWordWithUpperCaseFirstLetter(self):
        dictionary = {"languages": ["french", "english"]}
        expectedReturnedDictionary = {"languages": ["French", "English"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForLanguageKeywordWhenHavingFirstLetterUpperCaseShouldReturnWordsUnchanged(self):
        dictionary = {"languages": ["French", "English"]}
        expectedReturnedDictionary = {"languages": ["French", "English"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForGeographicCoordinatesWhenHavingDotBetweenNumbersShouldReturnSpacedNumber(self):
        dictionary = {"geographic coordinates": ["42.00 S"]}
        expectedReturnedDictionary = {"geographic coordinates": ["42 00 S"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForReligionsWhenHavingPercentageOfReligionsShouldReturnDictionaryWithInvertedOrderOfValueInformation(self):
        dictionary = {"religions": ["51.3% of protestant"]}
        expectedReturnedDictionary = {"religions": ["Protestant 51.3%"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForReligionsWhenHavingPercentageOfReligionsWithMuslimReligionShouldReturnTheFormattedDictionary(self):
        dictionary = {"religions": ["1.3% of muslim sia"]}
        expectedReturnedDictionary = {"religions": ["Muslim Sia 1.3%"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForIllicitDrugsWhenHavingOneElementShouldReturnDictionaryWithUnchangedList(self):
        dictionary = {"illicit drugs": ["cocaine"]}
        expectedReturnedDictionary = {"illicit drugs": ["cocaine"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)

    def test_formatValueInformationForIllicitDrugsWhenHavingTwoElementShouldReturnDictionaryWithSplitElement(self):
        dictionary = {"illicit drugs": ["cocaine transhipment"]}
        expectedReturnedDictionary = {"illicit drugs": ["cocaine", "transhipment"]}
        self.dictionaryValueInformationFormatter.formatValueInformation(dictionary)
        self.assertEqual(expectedReturnedDictionary, dictionary)