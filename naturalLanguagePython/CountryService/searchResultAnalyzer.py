__author__ = 'Antoine'

class SearchResultAnalyzer(object):

    def __findCountryNameAppearingInAllResultByKeywordSearch(self, listOfPossibleCountryByCategory):
        nameOfCountry = []
        for nameOfCountryFistCall in listOfPossibleCountryByCategory[0]:
            numberOfAppearanceOfNameOfCountry = self.__findCountryAppearingInListOfPossibleCountry(
                listOfPossibleCountryByCategory,
                nameOfCountryFistCall)
            if numberOfAppearanceOfNameOfCountry >= len(listOfPossibleCountryByCategory):
                nameOfCountry.append(nameOfCountryFistCall)
                break
        return nameOfCountry

    def __findCountryAppearingInListOfPossibleCountry(self, listOfCountry, nameOfCountryFistCall):
        numberOfAppearanceOfNameOfCountry = 0
        for nameOfCountryList in listOfCountry:
            for namePossible in nameOfCountryList:
                if namePossible == nameOfCountryFistCall:
                    numberOfAppearanceOfNameOfCountry += 1
        return numberOfAppearanceOfNameOfCountry

    def findPossibleCountryNameInSearchResultByKeyword(self, listOfPossibleCountryByCategory):
        listOfCountryName = []
        if len(listOfPossibleCountryByCategory) == 1:
            listOfCountryName = listOfPossibleCountryByCategory[0]
        else:
            listOfCountryName = self.__findCountryNameAppearingInAllResultByKeywordSearch(listOfPossibleCountryByCategory)
        return listOfCountryName
