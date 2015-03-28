__author__ = 'Antoine'


class FormatValueFromReligionKeyword(object):

    def __removeItemFromInitialReligionItem(self, splitValue):
        i = 0
        while i < len(splitValue):
            if splitValue[i].isalpha():
                splitValue.remove(splitValue[i])
            else:
                i += 1

    def __capitalizeItemFromReligionValue(self, splitValue):
        capitalizeSplitValue = []
        for splitItem in splitValue:
            if splitItem.isalpha():
                capitalizeSplitValue.append(splitItem.capitalize())
        return capitalizeSplitValue

    def __formatSplitValue(self, capitalizeWordValue, splitValue):
        formattedSplitValue = []
        for capitalizeElement in capitalizeWordValue:
            if capitalizeElement != "Of":
                formattedSplitValue.append(capitalizeElement)
        formattedSplitValue.append(splitValue[0])
        return formattedSplitValue

    def formatReligionsKeywordValue(self, dictionary):
        religions = "religions"
        if religions in dictionary:
            formattedValue = []
            for element in dictionary[religions]:
                splitValue = element.split(" ")
                if "of" in splitValue:
                    capitalizeWordValue = self.__capitalizeItemFromReligionValue(splitValue)
                    self.__removeItemFromInitialReligionItem(splitValue)
                    formattedSplitValue = self.__formatSplitValue(capitalizeWordValue, splitValue)
                    formattedValue.append(" ".join(formattedSplitValue))
                else:
                    formattedValue.append(element)
            dictionary[religions] = formattedValue