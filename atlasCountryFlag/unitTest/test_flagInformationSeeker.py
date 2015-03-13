from unittest import TestCase
from mock import Mock
from atlasCountryFlag.flagService.flagInformationSeeker import FlagInformationSeeker
__author__ = 'Antoine'


class TestFlagInformationSeeker(TestCase):

    def setUp(self):
        path = None
        self.flagInformationSeeker = FlagInformationSeeker(path)

    def test_searchingFlagColorWhenNoFlagCountryNameCorrespondToSearchedNameShouldReturnAnEmptyList(self):
        nameOfCountry = "Country"
        expectedColorList = []
        self.flagInformationSeeker.flagRepository.searchFlagColorList = Mock(return_value = expectedColorList)
        self.assertEqual(expectedColorList, self.flagInformationSeeker.searchColorFlagByNameOfCountry(nameOfCountry))

    def test_searchingFlagColorWhenAFlagCountryNameCorrespondToSearchedNameShouldReturnFlagColorList(self):
        nameOfCountry = "Country"
        expectedColorList = ["blue"]
        self.flagInformationSeeker.flagRepository.searchFlagColorList = Mock(return_value = expectedColorList)
        self.assertEqual(expectedColorList, self.flagInformationSeeker.searchColorFlagByNameOfCountry(nameOfCountry))

    def test_searchingFlagPictureFilenameWhenNoFlagCountryNameCorrespondToSearchedNameShouldReturnNone(self):
        nameOfCountry = "Country"
        expectedFlagFilename = None
        self.assertEqual(expectedFlagFilename, self.flagInformationSeeker.searchFlagPictureFilename(nameOfCountry))

    def test_searchingFlagPictureFilenameWhenAFlagCountryNameCorrespondToSearchedNameShouldReturnFlagPictureFilename(self):
        nameOfCountry = "Country"
        expectedFlagFilename = "country.gif"
        self.flagInformationSeeker.flagRepository.searchFlagPictureFilename = Mock(return_value = expectedFlagFilename)
        self.assertEqual(expectedFlagFilename, self.flagInformationSeeker.searchFlagPictureFilename(nameOfCountry))

