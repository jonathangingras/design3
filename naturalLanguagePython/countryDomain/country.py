__author__ = 'Antoine'


class Country(object):

    def __init__(self, nameOfCountry, informationDictionary):
        self.name = nameOfCountry
        self.informationDict = informationDictionary

    @staticmethod
    def __isValueListContainingTheWantedValue(currentValuesFromKey, value):
        isContaining = False
        if type(currentValuesFromKey) is list:
            for currentValue in currentValuesFromKey:
                if currentValue == value:
                    isContaining = True
        else:
            if currentValuesFromKey is value:
                isContaining = True
        return isContaining

    def contains(self, key, value, searchStrategy = None):
        isContaining = False
        if self.informationDict.has_key(key):
            if searchStrategy is None:
                currentValue = self.informationDict[key]
                isContaining = self.__isValueListContainingTheWantedValue(currentValue, value)
            else:
                isContaining = searchStrategy.findInformationList(self.informationDict, key, value)
        return isContaining