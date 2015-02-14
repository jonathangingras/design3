__author__ = 'Antoine'
from htmlInformationFormatter import HtmlInformationFormatter

class HtmlInformationValidator(object):

    def __init__(self):
        self.htmlInformationFormatter = HtmlInformationFormatter()

    def verifyingStringContent(self, extractedInfos):
        informationList = []
        for extractedInfo in extractedInfos:
            if extractedInfo.string is not None:
                formattedInformationString = self.htmlInformationFormatter.informationKeyFormatting(extractedInfo.string)
                if formattedInformationString is not None:
                    informationList.append(formattedInformationString.encode('utf-8'))
        return informationList