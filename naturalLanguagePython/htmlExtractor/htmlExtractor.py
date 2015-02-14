__author__ = 'Antoine'
from htmlInformationValidator import HtmlInformationValidator

class HtmlExtractor(object):

    def __init__(self):
        self.htmlInformationValidator = HtmlInformationValidator()


    def extractCountryData(self, key, soup):
        informationKeyTag = soup.find('a', title="Notes and Definitions: " + key)
        parent = ((informationKeyTag.parent).parent).parent
        parentNextElement = (parent.next_sibling).next_element
        extractedInfos = parentNextElement.find_all(['div', 'span'], ['category', 'category_data'])
        extractedInfosList = self.htmlInformationValidator.verifyingStringContent(extractedInfos)
        return extractedInfos

    def extractCountryInformationHtmlTag(self, soup):
        tag = 'div'
        classType  = "category"
        return soup.find_all(tag, classType)

    def getNameOfCountry(self, soup):
        nameOfCountryTag = soup.find('span', 'region')
        return nameOfCountryTag.string

    def informationCategoryFinder(self, informationCategory):
        tagChild = informationCategory.find('a')
        return tagChild