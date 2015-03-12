from unittest import TestCase
from atlasCountryFlag.flagDomain.flag import Flag
from atlasCountryFlag.flagPersistance.flagRepositroyDB import FlagRepositoryDB
__author__ = 'Antoine'


class TestFlagRepositoryDB(TestCase):

    def setUp(self):
        self.flagRepositoryDB = FlagRepositoryDB()
        self.firstFlagToAdd = Flag("aPath", "aName", ["blue"])
        self.secondFlagToAdd = Flag("aPath", "aSecondName", ["red"])
        self.flagRepositoryDB

    def test_initiatingTheFlagRepositoryDBShouldCreateAnEmptyList(self):
        expectedCreatedList = []
        self.assertEqual(expectedCreatedList, self.flagRepositoryDB.flagList)


    def test_addAFlagToTheRepositoryWhenHavingAnEmptyListOfFlagShouldAddTheFlagToTheList(self):
        expectedLenOfFlagList = 1
        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        numberOfElementInList = len(self.flagRepositoryDB.flagList)
        self.assertEqual(expectedLenOfFlagList, numberOfElementInList)

    def test_addAFlagToTheRepositoryWhenHavingAListOfFlagOfOneElementShouldAddTheFlagToTheList(self):
        expectedLenOfFlag = 2

        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        self.flagRepositoryDB.addFlag(self.secondFlagToAdd)
        numberOfElementInList = len(self.flagRepositoryDB.flagList)
        self.assertEqual(expectedLenOfFlag, numberOfElementInList)

    def test_searchForAFlagByTheNameOfCountryWhenHavingTheCountryInsideListShouldReturnTheFlagColorList(self):
        expectedColorList = ["blue"]
        nameOfCountry = "aName"
        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        returnedColorList = self.flagRepositoryDB.searchFlag(nameOfCountry)
        self.assertEqual(expectedColorList, returnedColorList)
