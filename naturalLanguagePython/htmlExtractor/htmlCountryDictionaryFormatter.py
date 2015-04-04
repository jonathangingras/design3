__author__ = 'Antoine'
from naturalLanguagePython.htmlExtractor.htmlInformationFormatter import HtmlInformationFormatter

class HtmlCountryDictionaryFormatter(object):

    def __init__(self):
        self.htmlInformationFormatter = HtmlInformationFormatter()

    def formatMajorUrbanAreaValue(self, dictionary):
        majorUrbanArea = "major urban areas - population"
        if majorUrbanArea in dictionary:
            formattedValueList = []
            for element in dictionary[majorUrbanArea]:
                formattedValue = self.htmlInformationFormatter.formatMajorUrbanAreaValue(element)
                formattedValueList.append(formattedValue)
            dictionary[majorUrbanArea] = formattedValueList

        return dictionary