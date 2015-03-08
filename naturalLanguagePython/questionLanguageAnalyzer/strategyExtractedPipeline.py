__author__ = 'Antoine'
import re
class StrategyExtractedPipeline(object):

    def extractStrategies(self, question):
        listOfStrategy = []
        self.__searchStartsWith(question, listOfStrategy)
        self.__searchEndsWith(question, listOfStrategy)
        self.__searchContains(question, listOfStrategy)
        self.__searchGreaterThan(question, listOfStrategy)
        self.__searchLessThan(question, listOfStrategy)
        return listOfStrategy

    def __searchStartsWith(self, question, listOfStrategy):
        regec = re.compile('starts')
        if regec.search(question):
            listOfStrategy.append('Starts with')

    def __searchEndsWith(self, question, listOfStrategy):
        regex = re.compile('ends')
        if regex.search(question):
            listOfStrategy.append('Ends with')

    def __searchContains(self, question , listOfStrategy):
        regex = re.compile('contains')
        if regex.search(question):
            listOfStrategy.append('Contains')

    def __searchGreaterThan(self, question, listOfStrategy):
        regex = re.compile('greater')
        if regex.search(question):
            listOfStrategy.append('Greater than')

    def __searchLessThan(self, question, listOfStrategy):
        regex = re.compile('less')
        if regex.search(question):
            listOfStrategy.append('Less than')