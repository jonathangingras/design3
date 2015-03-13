from unittest import TestCase
from atlasCountryFlag.flagService.flagInformationSeeker import FlagInformationSeeker
__author__ = 'Antoine'


class TestFlagInformationSeeker(TestCase):

    def setUp(self):
        path = "C:\Users\Antoine\Documents\design3\\atlasCountryFlag"
        self.flagInformationSeeker = FlagInformationSeeker(path)

    def test_searchForAFlagColorListWhenSearchingByTheNameOfANonParsedCountryShouldReturnAnEmptyList(self):
        nameOfCountry = "Country"
        expectedColorList = []
        self.assertEqual(expectedColorList, self.flagInformationSeeker.searchColorFlagByNameOfCountry(nameOfCountry))

    def test_searchForAFlagColorListWhenSearchingByAParsedCountryNameShouldReturnTheCorrespondingColorList(self):
        nameOfCountry = "Netherlands"
        expectedColorList = [None, "red", None,
                             None, "white", None,
                             None, "blue", None]
        self.assertEqual(expectedColorList, self.flagInformationSeeker.searchColorFlagByNameOfCountry(nameOfCountry))

    def test_searchForAFlagPictureFilenameWhenSearchingByTheNameOfUnparsedCountryShouldReturnNone(self):
        nameOfCountry = "Country"
        expectedFlagPictureFilename = None
        self.assertEqual(expectedFlagPictureFilename, self.flagInformationSeeker.searchFlagPictureFilename(nameOfCountry))

    def test_searchForAFlagPictureFilenameWhenSearchingByTheNameOfAParsedCountryShouldReturnCorrespondingFlagPictureFilename(self):
        nameOfCountry = "Netherlands"
        expectedFlagPictureFilename = "Flag_Netherlands.gif"
        self.assertEqual(expectedFlagPictureFilename, self.flagInformationSeeker.searchFlagPictureFilename(nameOfCountry))