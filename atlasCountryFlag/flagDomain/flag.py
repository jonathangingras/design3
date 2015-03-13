__author__ = 'Antoine'


class Flag(object):

    def __init__(self, nameOfCountry, colorList):
        self.nameOfCountry = nameOfCountry
        self.colorList = colorList
        self.__setPictureFlagFilename(nameOfCountry)

    def isFlagForThisCountry(self, nameOfCountry):
        isCorrectFlag = False
        if self.nameOfCountry == nameOfCountry:
            isCorrectFlag = True
        return isCorrectFlag

    def __setPictureFlagFilename(self, nameOfCountry):
        filenamePrefix = "Flag_"
        filenameSuffix = ".gif"
        self.flagPictureFilename = filenamePrefix + nameOfCountry + filenameSuffix
