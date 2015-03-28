__author__ = 'alex'
import re


class SearchSubjectInQuestionWithRegex(object):

    def __init__(self):
        self.subjectRegex = [r"((?<=[Mm]y )(.*?)((?=\sinclude)|(?= was )|(?= is )|(?= are)|(?= is the)|(?= contains)))",
                             r"((?<=[Mm]y )(\w+){1}(?= \w*\s?starts))",
                             r"(((?<=has\sa[n\s])\s?(\w+\s?){1,3})((?= of )|(?= between )|(?= greater )|(?= including)|(?= \w+ starts)|(?= and )))",
                             r"((?<=its )|(?<= our ))(\w+)",
                             r"(?<=[Ww]hat country has )(([a-z]{3,}[^d ]\b)|(\w+\s?){1,3})(?= including )",
                             r"(?<=[Ww]hat country has a )(.+)(?= of )",
                             r"((?<=[Ww]hat country considers )((\w+\s*?){2})(?= \w+ing as a ))",
                             r"(?<=is the )(.+)(?= of this country)",
                             r"(?<=The )(\w+\s?){1,3}(?= of this country)"]


    def __removeSmallestElementAlreadyInsideAnOtherItem(self, listOfSubject):
        for x in listOfSubject:
            for y in listOfSubject:
                searchSub = str.find(str(x), str(y))
                if searchSub != -1:
                    if len(x) > len(y):
                        listOfSubject.remove(y)
        return listOfSubject

    def __addElementFromListTempInListSubject(self, indexBegin, listTemp, listOfSubject):

        for key in listTemp:
            if listOfSubject.count(key[indexBegin]) == 0:
                listOfSubject.append(key[indexBegin])
        return listOfSubject

    def searchSubject(self, question,listOfSubject):
        indexBegin = 0
        for reg in self.subjectRegex:
            regex = re.compile(reg)
            wordReturn = regex.search(question)
            if  wordReturn != None:
                if listOfSubject.count(wordReturn) == 0:
                    listTemp = []
                    listTemp = regex.findall(question)
                    if len(listTemp) > 1:
                        listOfSubject = self.__addElementFromListTempInListSubject(indexBegin, listTemp, listOfSubject)
                    else:
                        listOfSubject.append(regex.search(question).group())

        listOfSubject = self.__removeSmallestElementAlreadyInsideAnOtherItem(listOfSubject)

        return listOfSubject