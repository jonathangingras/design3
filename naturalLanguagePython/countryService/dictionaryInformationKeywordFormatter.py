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

    def __formatToLowerCaseKeyword(self, receivedDictionary):
        dictionary = {}
        for keyword in receivedDictionary:
            dictionary[str.lower(keyword)] = receivedDictionary[keyword]
        return dictionary

    def formatDictionary(self, receivedDictionary):
        convertedDictionary = {}
        receivedDictionary = self.__formatToLowerCaseKeyword(receivedDictionary)
        possibleConversion = self.__obtainPossibleKeywordConversion()
        for keyword in receivedDictionary:
            if keyword in possibleConversion:
                convertedDictionary[possibleConversion[keyword]] = receivedDictionary[keyword]
            else:
                convertedDictionary[keyword] = receivedDictionary[keyword]
        return convertedDictionary
