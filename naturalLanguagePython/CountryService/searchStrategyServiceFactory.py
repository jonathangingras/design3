__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
from naturalLanguagePython.countryService.countryServiceException import CountryServiceException
defaultSearchStrategy = "Contains"


class SearchStrategyServiceFactory(object):

    def __init__(self):
        self.searchStrategyFactory = SearchStrategyFactory()

    def wantedSearchStrategyValidator(self, searchedInformationDict, wantedSearchStrategy = None):
        if wantedSearchStrategy is None:
            wantedSearchStrategy = {}
            for keyword in searchedInformationDict:
                wantedSearchStrategy[keyword] = []
        totalNumberOfSearchStrategy = 0
        for searchStrategyByKeyword in wantedSearchStrategy:
            totalNumberOfSearchStrategy += len(wantedSearchStrategy[searchStrategyByKeyword])
        numberOfInformationInDictionary = 0
        for keyword in searchedInformationDict:
            numberOfInformationInDictionary += len(searchedInformationDict[keyword])
        if numberOfInformationInDictionary < totalNumberOfSearchStrategy:
            raise CountryServiceException(
                "The number of wanted information needs to be higher than the number of wanted search strategy")
        for keyword in searchedInformationDict:
            numberOfInformation = len(searchedInformationDict[keyword])
            numberOfSearchStrategy = len(wantedSearchStrategy[keyword])
            while numberOfSearchStrategy < numberOfInformation:
                wantedSearchStrategy[keyword].append("Contains")
                numberOfSearchStrategy += 1
        return wantedSearchStrategy

    def createStrategy(self, searchStrategy = None):
        return self.searchStrategyFactory.createSearchStrategy(searchStrategy)