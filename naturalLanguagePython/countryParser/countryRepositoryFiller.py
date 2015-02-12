__author__ = 'Antoine'
from naturalLanguagePython.CountryDomain.CountryRepository import CountryRepository
from os import path
class CountryRepositoryFiller(object):

    def __init__(self, countryRepository):

        self.countryRepository = countryRepository

    def addCountriesToTheRepository(self):
        self.countryRepository.addCountry()


if __name__ == '__main__':
    pass