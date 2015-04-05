__author__ = 'Antoine'
import json
from os import path


class DictionaryInformationFormatter(object):

    def __init__(self, pathToModule):
        self.pathToModule = pathToModule

    def __setupFormatterData(self):
        pathToFormatterData = path.realpath(self.pathToModule + "/countryService/keywordConversion.json")
        keywordFormatterJsonFile = open(pathToFormatterData, 'r')
        keywordFormatterData = json.load(keywordFormatterJsonFile)
        return keywordFormatterData

    def __obtainPossibleKeywordConversion(self):
        keywordFormatterData = self.__setupFormatterData()
        possibleConversion = keywordFormatterData['conversion']
        possibleConversion = possibleConversion[0]
        return possibleConversion

    def formatDictionary(self, receivedDictionary):
        convertedDictionary = {}
        possibleConversion = self.__obtainPossibleKeywordConversion()
        for keyword in receivedDictionary:
            if keyword in possibleConversion:
                convertedDictionary[possibleConversion[keyword]] = receivedDictionary[keyword]
            else:
                convertedDictionary[keyword] = receivedDictionary[keyword]
        return convertedDictionary
