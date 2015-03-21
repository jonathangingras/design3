__author__ = 'Antoine'
from naturalLanguagePython.searchInformationStrategy.searchStrategyFactory import SearchStrategyFactory
from naturalLanguagePython.countryService.countryServiceException import CountryServiceException
defaultSearchStrategy = "Contains"


class SearchStrategyServiceFactory(object):

    def __init__(self):
        self.searchStrategyFactory = SearchStrategyFactory()

    def wantedSearchStrategyValidator(self, searchedInformationDict, wantedSearchStrategy = None):
        if wantedSearchStrategy is None:
            wantedSearchStrategy = []
        numberOfPossibleSearchStrategy = 0
        print(searchedInformationDict)
        for element in searchedInformationDict:
            print(element)
            numberOfPossibleSearchStrategy += len(searchedInformationDict[element])
        if numberOfPossibleSearchStrategy < len(wantedSearchStrategy):
            raise CountryServiceException(
                "The number of wanted information needs to be higher than the number of wanted search strategy")

        print(numberOfPossibleSearchStrategy)
        while len(wantedSearchStrategy) < numberOfPossibleSearchStrategy:
            wantedSearchStrategy.append(defaultSearchStrategy)
        print(wantedSearchStrategy)
        return wantedSearchStrategy

    def createStrategy(self, searchStrategy = None):
        return self.searchStrategyFactory.createSearchStrategy(searchStrategy)