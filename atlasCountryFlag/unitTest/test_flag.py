from unittest import TestCase
from atlasCountryFlag.flagDomain.flag import Flag
__author__ = 'Antoine'


class TestFlag(TestCase):

    def test_createFlagWithAllParametersShouldCreateTheFlagObject(self):
        flagPath = "aPath"
        nameOfCountry = "ACountry"
        colorList = ["Blue", "Blue"]
        flag = Flag(flagPath, nameOfCountry, colorList)
        self.assertIsInstance(flag, Flag)
