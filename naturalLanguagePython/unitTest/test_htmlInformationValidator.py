from unittest import TestCase
from naturalLanguagePython.htmlExtractor.htmlInformationValidator import HtmlInformationValidator
from bs4 import NavigableString, BeautifulSoup
from mock import Mock

__author__ = 'Antoine'


class TestHtmlInformationValidator(TestCase):

    def setUp(self):
        self.htmlInformationValidator = HtmlInformationValidator()
        self.htmlInformationValidator.htmlInformationFormatter = Mock()
        self.stringElement = "string"
        self.htmlInformationValidator.htmlInformationFormatter.informationKeyFormatting = Mock(return_value = self.stringElement)
        self.htmlInformationValidator.htmlInformationFormatter.formatNumberSeparatedByComaFromWorldFactBook = Mock(return_value = self.stringElement)
        self.htmlInformationValidator.htmlInformationFormatter.removeQuoteFromString = Mock(return_value = self.stringElement)

    def test_verifyingStringContentWhenTheExtractedInfoAreAnEmptyListShouldReturnAnEmptyList(self):
        extractedInfoList = []
        expectedInformationList = []
        self.assertEqual(self.htmlInformationValidator.verifyingStringContent(extractedInfoList), expectedInformationList)

    def test_verifyingStringContentWhenTheExtractedInfoStringElementIsNoneShouldReturnAnEmptyList(self):
        element = BeautifulSoup()
        extractedInfoList = [element]
        expectedInformationList = []
        self.assertEqual(self.htmlInformationValidator.verifyingStringContent(extractedInfoList), expectedInformationList)

    def test_verifyingStringContentWhenTheExtractedInfoStringReturnedByTheFormatterIsNoneShouldReturnAnEmptyList(self):
        element = NavigableString(self.stringElement)
        extractedInfoList = [element]
        expectedInformationList = []
        self.htmlInformationValidator.htmlInformationFormatter.informationKeyFormatting = Mock(return_value = None)
        self.assertEqual(self.htmlInformationValidator.verifyingStringContent(extractedInfoList), expectedInformationList)

    def test_verifyingStringContentWhenTheExtractedInfoStringWhenTheInformationIsNotNoneShouldReturnInformationListWithTheString(self):
        element = NavigableString(self.stringElement)
        extractedInfoList = [element]
        expectedInformationList = [self.stringElement]
        self.assertEqual(self.htmlInformationValidator.verifyingStringContent(extractedInfoList), expectedInformationList)

    def test_verifyingStringContentWhenTheExtractedInfoContainsMoreThanOneValidStringShouldReturnInformationListWithMoreThanOneElement(self):
        firstElement = NavigableString(self.stringElement)
        secondElement = NavigableString(self.stringElement)
        extractedInfoList = [firstElement, secondElement]
        expectedInformationList = [self.stringElement, self.stringElement]
        self.assertEqual(self.htmlInformationValidator.verifyingStringContent(extractedInfoList), expectedInformationList)
