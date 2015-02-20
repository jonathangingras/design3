__author__ = 'Antoine'
import re

class Country(object):

    def __init__(self, nameOfCountry, informationDictionary):
        self.name = nameOfCountry
        self.informationDict = informationDictionary

    def __isValueListContainingTheWantedValue(self, currentValuesFromKey, value, regex):
        isContaining = False
        for currentValue in currentValuesFromKey:
            if regex is None:
                if currentValue == value:
                    isContaining = True
            else:
                expression = re.compile(regex)
                if expression.search(currentValue) is not None:
                    isContaining = True
        return isContaining

    def __isValueCorrespondingToTheWantedValue(self, currentValueFromKey, wantedValue, regex):
        isContaining = False
        if regex is not None:
            expression = re.compile(regex)
            if expression.search(currentValueFromKey) is not None:
                isContaining = True
        else:
            if currentValueFromKey is wantedValue:
                isContaining = True
        return isContaining

    def contains(self, key, value, regex = None):
        isContaining = False
        if self.informationDict.has_key(key):
            if type(self.informationDict[key]) is list:
                currentValue = self.informationDict[key]
                isContaining = self.__isValueListContainingTheWantedValue(currentValue, value, regex)
            else:
                currentValue = self.informationDict[key]
                isContaining = self.__isValueCorrespondingToTheWantedValue(currentValue, value, regex)
        return isContaining