__author__ = 'Antoine'
import abc

class questionAnalyzer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def extractedImportantInformationsFromQuestion(self, questionFromAtlas):
        return