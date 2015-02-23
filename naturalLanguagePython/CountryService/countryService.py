__author__ = 'Antoine'
from naturalLanguagePython.countryPersistence.countryRepositoryDB import CountryRepositoryDB
from naturalLanguagePython.SearchInformationStrategy.searchStrategyFactory import SearchStrategyFactory

class CountryService(object):

    def __init__(self):
        self.countryRepository = CountryRepositoryDB()
        self.searchStrategyFactory = SearchStrategyFactory()