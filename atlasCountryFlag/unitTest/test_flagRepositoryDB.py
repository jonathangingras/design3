from unittest import TestCase
from mock import Mock
from atlasCountryFlag.flagDomain.flag import Flag
from atlasCountryFlag.flagPersistance.flagRepositroyDB import FlagRepositoryDB
__author__ = 'Antoine'


class TestFlagRepositoryDB(TestCase):

    def setUp(self):
        self.flagRepositoryDB = FlagRepositoryDB()
        self.firstFlagToAdd = Flag("countryName", ["blue"])
        self.secondFlagToAdd = Flag("aSecondName", ["red"])
        self.secondFlagToAdd.isFlagForThisCountry = Mock(return_value = False)
        self.firstFlagToAdd.isFlagForThisCountry = Mock(return_value = False)

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

    def test_searchForAFlagColorListByTheNameOfCountryWhenHavingTheCountryInsideListShouldReturnTheFlagColorList(self):
        expectedColorList = ["blue"]
        nameOfCountry = "countryName"
        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        self.firstFlagToAdd.isFlagForThisCountry = Mock(return_value = True)
        self.assertEqual(expectedColorList, self.flagRepositoryDB.searchFlagColorList(nameOfCountry))

    def test_searchForAFlagColorListByTheCountryNameWhenNotHavingTheCountryInsideListShouldReturnAnEmptyList(self):
        expectedColorList = []
        nameOfCountry = "aCountryName"
        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        self.assertEqual(expectedColorList, self.flagRepositoryDB.searchFlagColorList(nameOfCountry))

    def test_searchForFlagColorListByTheCountryNameWhenNotHavingTheCountryInsideListAndHavingMoreThanOneElementInListShouldReturnAnEmptyList(self):
        expectedColorList = []
        nameOfCountry = "aCountryName"
        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        self.flagRepositoryDB.addFlag(self.secondFlagToAdd)
        self.assertEqual(expectedColorList, self.flagRepositoryDB.searchFlagColorList(nameOfCountry))

    def test_searchForAFlagPictureFilenameByCountryNameWhenNotHavingTheCountryInsideListShouldReturnNone(self):
        expectedFlagPictureFilename = None
        nameOFCountry = "aCountryName"
        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        self.assertEqual(expectedFlagPictureFilename, self.flagRepositoryDB.searchFlagPictureFilename(nameOFCountry))

    def test_searchForAFlagPictureFilenameByCountryNameWhenHavingTheCountryInsideListShouldReturnFlagPictureFilename(self):
        expectedFlagPictureFilename = "Flag_countryName.gif"
        nameOfCountry = "countryName"
        self.firstFlagToAdd.isFlagForThisCountry = Mock(return_value = True)
        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        self.assertEqual(expectedFlagPictureFilename, self.flagRepositoryDB.searchFlagPictureFilename(nameOfCountry))

    def test_searchForAFlagPictureFilenameByCountryNameWhenNotHavingCountryInsideListOfTwoElementShouldReturnNone(self):
        expectedFlagPictureFilename = None
        nameOfCountry = "aCountryName"
        self.flagRepositoryDB.addFlag(self.firstFlagToAdd)
        self.flagRepositoryDB.addFlag(self.secondFlagToAdd)
        self.assertEqual(expectedFlagPictureFilename, self.flagRepositoryDB.searchFlagPictureFilename(nameOfCountry))
