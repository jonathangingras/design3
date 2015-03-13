from unittest import TestCase
from atlasCountryFlag.flagPersistance.flagRepositoryFiller import FlagRepositoryFiller
from atlasCountryFlag.flagPersistance.flagRepositroyDB import FlagRepositoryDB
__author__ = 'Antoine'


class TestFlagRepositoryFiller(TestCase):

    def setUp(self):
        self.path = "C:\Users\Antoine\Documents\design3\\atlasCountryFlag"
        self.flagRepositoryDB = FlagRepositoryDB()
        self.flagRepositoryFiller = FlagRepositoryFiller(self.flagRepositoryDB)
        self.flagRepositoryFiller.setupFlagRepository(self.path)

    def test_fillingARepositoryWhenTheNumberOfCountryInsideNewCountryJsonIsNotEmptyNumberOfElementInFlagListOfRepositoryShouldNotBeZero(self):
        numberOfElementInsideTheRepository = len(self.flagRepositoryDB.flagList)
        self.assertNotEqual(0, numberOfElementInsideTheRepository)

    def test_searchingAParsedFlagInsideRepositoryWhenTheNameOfCountryIsInsideOneFlagShouldReturnTheColorListOfTheFlag(self):
        nameOfCountry = "Netherlands"
        expectedColorList = [None, "red", None,
                             None, "white", None,
                             None, "blue", None]
        self.assertEqual(expectedColorList, self.flagRepositoryDB.searchFlagColorList(nameOfCountry))

    def test_searchingAParsedFlagInsideRepositoryWhenTheNameOfCountryIsNotInsideOneFlagShouldReturnAnEmptyList(self):
        nameOfCountry = "aCountry"
        expectedColorList = []
        self.assertEqual(expectedColorList, self.flagRepositoryDB.searchFlagColorList(nameOfCountry))