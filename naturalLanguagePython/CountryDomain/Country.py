__author__ = 'Antoine'


class Country(object):

    def __init__(self, nameOfCountry, informationDictionary):
        self.name = nameOfCountry
        self.informationDict = informationDictionary

    def contains(self, key, value):
        isContaining = False
        if self.informationDict.has_key(key):
            if self.informationDict[key] is value:
                isContaining = True
        return isContaining