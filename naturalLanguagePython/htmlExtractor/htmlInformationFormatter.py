__author__ = 'Antoine'
import re


class HtmlInformationFormatter(object):

    def __init__(self):
        self.countryComparison = 'country comparison to the world'

    def informationKeyFormatting(self, tagToExtractTheKey):
        try:
            key = None
            if (tagToExtractTheKey is not None):
                string = tagToExtractTheKey.string
                keyStringFormattedFromHtml = str(string)
                strippedKeyString = keyStringFormattedFromHtml.strip(' :')
                key = strippedKeyString
            if key == self.countryComparison:
                key = None
            return key
        except UnicodeEncodeError:
            pass

    def firstLetterLowering(self, key):
        if key is None:
            return None
        return str.lower(key)

    def formatNumberSeparatedByComaFromWorldFactBook(self, receivedString):
        splittedString = receivedString.split(" ")
        formattedString = ""
        numberFormatRegex = re.compile("\d+(\,\d+){1,}")
        for stringElement in splittedString:
            if numberFormatRegex.search(stringElement):
                stringElement = stringElement.replace(",", "")
            formattedString += stringElement + " "

        return formattedString.strip()

    def removeQuoteFromString(self, receivedString):
        return receivedString.replace("\"", "")

    def formatMajorUrbanAreaValue(self, stringValue):
        formattedString = ""
        for stringPart in stringValue.split(" "):
            formattedStringPart = stringPart
            if stringPart != "million":
                formattedStringPart = stringPart.capitalize()
            formattedString += (formattedStringPart + " ")
        return formattedString.strip()