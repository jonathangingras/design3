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

    def __formatSlashValueFormatting(self, dictionary):
        for element in dictionary:
            formattedSlashListElement = []
            for listElement in dictionary[element]:
                formattedSlashListElement.append(listElement.replace("/ ", "/"))
            dictionary[element] = formattedSlashListElement

    def formatValueInformation(self, dictionary):
        self.__formatPopulationValue(dictionary)
        self.__formatSlashValueFormatting(dictionary)

        return dictionary