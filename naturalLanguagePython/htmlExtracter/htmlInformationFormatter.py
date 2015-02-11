__author__ = 'Antoine'

class HtmlInformationFormatter(object):

    def __init__(self):
        self.countryComparison = 'country comparison to the world'

    def informationKeyFormatting(self, tagToExtractTheKey):
        key = None
        if (tagToExtractTheKey is not None):
            string = tagToExtractTheKey.string
            keyStringFormattedFromHtml = str(string)
            strippedKeyString = keyStringFormattedFromHtml.strip(' :')
            key = strippedKeyString
        if key == self.countryComparison:
            key = None
        return key