__author__ = 'Antoine'

class Flag(object):

    def __init__(self, nameOfCountry, colorList):
        self.nameOfCountry = nameOfCountry
        self.colorList = colorList

    def isFlagForThisCountry(self, nameOfCountry):
        isCorrectFlag = False
        if self.nameOfCountry == nameOfCountry:
            isCorrectFlag = True
        return isCorrectFlag