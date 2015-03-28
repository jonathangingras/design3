__author__ = 'alex'
import re

class SearchValueWithRegex(object):

    def __init__(self):
        self.listRegexValueWord = [r"(?<=starts with )([A-Z][a-z]+){1}",
                                 r"(?<=ends with )(\w+){1}",
                                 r"((?<=including )|(?<=include )|(?<= are ))((\d+\.\d+\%?)(\s\w+)* and (\d+\.\d+\%?)(\s\w+)*|(\w+\,\s)+(\w+\,?\s)?and (\w+)|(\w+ and \w+\s?))",
                                 r"((\d+\.\d+\%?)(\s\w+)* and (\d+\.\d+\%?)(\s\w+)*|(\w+\,\s)+(\w+\,?\s)?and (\w+))",
                                 r"(?<=between )(\S?\d+)+(\.)?(\d+)((\%)|(\w+)+) and ((\S?\d+[%.]?)+)((\s\w+)+)?",
                                 r"((?<=greater than )|(?<=less than ))(((\d+)(\ |\.|\%)?)+(\w+\/\d+)?)+",
                                 r"((\d+\s)?([A-Z][a-z]{2,}\s(\d+)))",
                                 r"((([(\d+\d+)|(\d+)]+\ \d+)|([(\d+\d+)|(\d+)]+\.\d+)) [SENW])",
                                 r"(?<=is the )((\w+\s?){1,2})((?=\.))",
                                 r"(\d+\.?\d*\s\w+\/\s?\d+)",
                                 r"(?<=[Ww]hat country has )(([A-Z][a-z]+\s?)?(\w*['-]?\w*\-?)?(\s?[A-Z][a-z]+)?){1,3}(?= as)",
                                 r"(\.[a-z]+)",
                                 r"((?<=including a )|(?<=(?<!(including ))ing\b as a ))(\w+\s?)+",
                                 r"(\d*\.?\d+\%)",
                                 r"(?<= contains )(\w+\s?\-?\'?){1,2}",
                                 r"((\d+[ /.]?\d+[ %]?)((\w+llion)|(sq km)))",
                                 r"(?<= is )(\d+(\s|\.)\d+\%?)(\s[a-z]{1,2})?(\s[A-Z]{1,})?",
                                 r"((?<=is )([A-Z][a-z]*([\s\,]*))+|(?<= are )([A-Z][a-z]*[\s\,]*([a-z ]+)?)+)",
                                 r"((?<=The )(\w+\s*?){2}(?= is ))",
                                 r"((?<=is )(\d+\s\w*?){1,})",
                                 r"((?<=[Mm]y )(?<=.)*?((?= is)|(?= was)|(?= are)|(?= is the))(\s+\w))"]

    def __addElementsFromListTempIntoListOfKey(self, indexBegin, listTemp,listOfValue):
        for key in listTemp:
            listOfKey = []
            for i in key:
                listOfKey.append(str(i))
            listOfKey = self.__removeSubPartOfSameStringOfAList(listOfKey)
            if listOfValue.count(listOfKey[indexBegin]) == 0:
                listOfValue.append(listOfKey[indexBegin])
        return listOfValue

    def __removeSubPartOfSameStringOfAList(self,listStringFromRegex):
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

    def parseAllRegexValue(self, question):
        listOfValue = []
        indexBegin = 0
        for reg in self.listRegexValueWord:
            regex = re.compile(reg)
            wordReturn = regex.search(question)
            if wordReturn is not None:
                if listOfValue.count(wordReturn) == 0:
                    listTemp = []
                    listTemp = regex.findall(question)

                    if len(listTemp) > 1:
                        listOfValue = self.__addElementsFromListTempIntoListOfKey(indexBegin, listTemp, listOfValue)
                    else:
                        listOfValue.append(regex.search(question).group())

        return listOfValue