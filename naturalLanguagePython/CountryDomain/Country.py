__author__ = 'Antoine'


class Country(object):

    def __init__(self, nameOfCountry, informationDictionary):
        if nameOfCountry.islower():
            raise SyntaxError
        self.name = nameOfCountry
        self.informationDict = informationDictionary