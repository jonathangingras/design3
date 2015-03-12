from unittest import TestCase
from atlasCountryFlag.flagDomain.flag import Flag
__author__ = 'Antoine'


class TestFlag(TestCase):

    def setUp(self):
        self.nameOfCountry = "ACountry"
        self.colorList = ["Blue", "Blue"]
        self.flag = Flag(self.nameOfCountry, self.colorList)

    def test_createFlagWithAllParametersShouldCreateTheFlagObject(self):
        self.assertIsInstance(self.flag, Flag)

    def test_isFlagCorrespondingToACountryNameWhenTheFlagIsNotTheCorrespondingOneShouldReturnFalse(self):
        nameOfCountry = "NotACountry"
        expectedReturnValue = False
        self.assertEqual(expectedReturnValue, self.flag.isFlagForThisCountry(nameOfCountry))

    def test_isFlagCorrespondingToACountryNameWhenTheFlagIsTheCorrespondingOneShouldReturnTrue(self):
        nameOfCountry = "ACountry"
        expectedReturnValue = True
        self.assertEqual(expectedReturnValue, self.flag.isFlagForThisCountry(nameOfCountry))