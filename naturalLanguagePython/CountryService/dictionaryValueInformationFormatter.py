__author__ = 'Antoine'
import re


class DictionaryValueInformationFormatter(object):

    def __formatPopulationValue(self, dictionary):
        population = "population"
        if population in dictionary:
            formattedValue = []
            regex = re.compile("\d+(\s\d+){1,}")
            for element in dictionary[population]:
                if regex.match(element):
                    element =element.replace(" ", "")
                formattedValue.append(element)
            dictionary[population] = formattedValue

    def __formatGeographicCoordinate(self, dictionary):
        geographicCoordinate = "geographic coordinates"
        if geographicCoordinate in dictionary:
            formattedValue = []
            for element in dictionary[geographicCoordinate]:
                formattedElement = element.replace(".", " ")
                formattedValue.append(formattedElement)
            dictionary[geographicCoordinate] = formattedValue

    def __formatLanguageKeyword(self, dictionary):
        language = "languages"
        if language in dictionary:
            formattedValue = []
            for element in dictionary[language]:
                formattedValue.append(element.capitalize())
            dictionary[language] = formattedValue

    def __formatSlashValueFormatting(self, dictionary):
        for element in dictionary:
            formattedSlashListElement = []
            for listElement in dictionary[element]:
                formattedSlashListElement.append(listElement.replace("/ ", "/"))
            dictionary[element] = formattedSlashListElement

    def formatValueInformation(self, dictionary):
        self.__formatPopulationValue(dictionary)
        self.__formatSlashValueFormatting(dictionary)
        self.__formatLanguageKeyword(dictionary)
        self.__formatGeographicCoordinate(dictionary)
        return dictionary