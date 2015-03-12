__author__ = 'Antoine'

class Flag(object):

    def __init__(self, path, nameOfCountry, colorList):
        self.flagPath = path
        self.nameOfCountry = nameOfCountry
        self.colorList = colorList

    def isFlagForThisCountry(self, nameOfCountry):
        isCorrectFlag = False
        if self.nameOfCountry == nameOfCountry:
            isCorrectFlag = True
        return isCorrectFlag