from unittest import TestCase
from atlasCountryFlag.flagResource.flagInformationProvider import FlagInformationProvider
__author__ = 'Antoine'


class TestFlagInformationProvider(TestCase):

    def setUp(self):
        path = "C:\Users\Antoine\Documents\design3\\atlasCountryFlag"
        self.flagInformationProvider = FlagInformationProvider(path)

    def test_acquiringFlagPictureFilenameWhenSearchingWithAParsedCountryNameShouldReturnFlagPictureFilename(self):
        nameOfCountry = "France"
        expectedFlagPictureFilename = "Flag_France.gif"
        self.assertEqual(expectedFlagPictureFilename, self.flagInformationProvider.obtainFlagPictureFilename(nameOfCountry))

    def test_acquiringFlagColorListWhenSearchingWithAParsedCountryNameShouldReturnFlagColorList(self):
        nameOfCountry = "France"
        expectedColorList = [None, None, None,
                             "blue", "white", "red",
                             None, None, None]
        self.assertEqual(expectedColorList, self.flagInformationProvider.obtainFlagColorList(nameOfCountry))
