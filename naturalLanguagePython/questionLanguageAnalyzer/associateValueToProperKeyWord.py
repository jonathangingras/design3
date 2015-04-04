__author__ = 'alex'

import sys

class AssociateValueToSubject(object):

    def __init__(self):
        pass


    def __splitEnumerationStringInToAList(self, item):
        futureList = []
        listTemp = str(item).replace(' and ', ',').split(',')
        for temp in listTemp:
            temp.strip(' ')
            if temp != '':
                temp.rstrip(' ')
                futureList.append(temp.strip(' '))
        return futureList

    def splitEnumerationItemInListString(self,listWithEnumeration):
        futureList = []
        for item in listWithEnumeration:
            for value in self.__splitEnumerationStringInToAList(item):
                futureList.append(value)
        return futureList

    def __associateTwoListOfOneElementEach(self,listOfValue, listOfSubject):
        dictionaryWithRelevantInformationOfTheQuestion = {}
        for subject, key in zip(listOfSubject, listOfValue):
            dictionaryWithRelevantInformationOfTheQuestion[subject] = [key]
        return dictionaryWithRelevantInformationOfTheQuestion

    def removeSubPartOfSameStringOfAList(self,listStringFromRegex):
        flagRemoveElement = True
        while flagRemoveElement is True:
            flagRemoveElement = False
            for x in listStringFromRegex:
                for y in listStringFromRegex:
                    searchSub = str.find(str(x), str(y))
                    if searchSub != -1:
                        if len(x) > len(y):
                            listStringFromRegex.remove(y)
                            flagRemoveElement = True
        return listStringFromRegex

    def __returnPositionInTheListForNearestItemMatching(self, question, x, listOfItem):
        nearestValueDistance = sys.maxint
        nearestValuePosition = 0
        for value in listOfItem:

            valueTemp = abs(question.find(str(x)) -  question.find(str(value)))
            if valueTemp < nearestValueDistance:
                nearestValueDistance = valueTemp
                nearestValuePosition = listOfItem.index(value)

        return nearestValuePosition

    def __returnTheNearestItemOfTheListWithARefferentialObjectInTheStringQuestion(self, question, reffenrentialObject, listOfItem):
        nearestValueDistance = sys.maxint
        nearestValueName = ""
        for value in listOfItem:
            valueTemp = abs(question.find(str(reffenrentialObject)) -  question.find(str(value[len(value) - 1])))
            if valueTemp < nearestValueDistance:
                nearestValueDistance = valueTemp
                nearestValueName = value

        return nearestValueName


    def __associateValueElementIntoDictionary(self, question, listOfValues, dictionaryWithRelevantInformationOfTheQuestion):
        for valueNotPlacedYet in listOfValues:
            nearestValuePosition = self.__returnTheNearestItemOfTheListWithARefferentialObjectInTheStringQuestion(
                question, valueNotPlacedYet, dictionaryWithRelevantInformationOfTheQuestion.values())
            cpt = 0
            for val in dictionaryWithRelevantInformationOfTheQuestion.values():
                if (val == nearestValuePosition):
                    value = dictionaryWithRelevantInformationOfTheQuestion.values()[cpt]
                    value.append(valueNotPlacedYet)
                cpt = cpt + 1
        return dictionaryWithRelevantInformationOfTheQuestion


    def associateWordFromTwoListAndReturnIntoDictionary(self, question,listOfValue, listOfSubject):
        dictionaryWithRelevantInformationOfTheQuestion = {}
        listOfValue = self.splitEnumerationItemInListString(listOfValue)
        if len(listOfSubject) > len(listOfValue):
            listOfSubject = self.removeSubPartOfSameStringOfAList(listOfSubject)

        if len(listOfSubject) == 1 and len(listOfValue) == 1:
            dictionaryWithRelevantInformationOfTheQuestion = self.__associateTwoListOfOneElementEach(listOfValue,
                                                                                                     listOfSubject)
        elif len(listOfSubject) < len(listOfValue) and len(listOfSubject) == 1:
            dictionaryWithRelevantInformationOfTheQuestion[str(listOfSubject[0]).strip(' ')] = listOfValue
        elif len(listOfSubject) >= 2 and len(listOfValue) >= 2:
            for subject in listOfSubject:
                nearestValuePosition = self.__returnPositionInTheListForNearestItemMatching(question, subject, listOfValue)
                dictionaryWithRelevantInformationOfTheQuestion[subject] = [listOfValue.pop(nearestValuePosition)]
            if len(listOfValue) != 0 :
                dictionaryWithRelevantInformationOfTheQuestion = self.__associateValueElementIntoDictionary(question, listOfValue,
                                                           dictionaryWithRelevantInformationOfTheQuestion)
        return dictionaryWithRelevantInformationOfTheQuestion
