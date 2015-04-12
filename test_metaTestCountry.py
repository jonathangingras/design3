__author__ = 'alex'

from naturalLanguagePython.countryRessource.questionResponder import QuestionResponder
from unittest import TestCase
import json
import re
import unittest
import os
from os import path


class MetaTestCountry(TestCase):
    longMessage = True



def createDictionaryForMetaTesting(keyword):
    dictOfValue = {}
    jsonDirectoryPath = "C://Users//Antoine//Documents//design3//naturalLanguagePython//htmlExtractor//extractedCountryJson"
    for countryFile in os.listdir(path.abspath(jsonDirectoryPath)):
        nameOfCountryToAdd = countryFile.split('.')
        extractedCountryJson = jsonDirectoryPath + "//" + countryFile
        countryJson = open((extractedCountryJson), 'r')
        countryInformationDict = json.load(countryJson)
        if countryInformationDict.has_key("country name"):
            countryName = countryInformationDict["country name"][1]
            countryName = countryName.replace(" ", "_")
            value = ""
            if countryInformationDict.has_key(keyword):
                value = countryInformationDict[keyword][0]
            else:
                value = None
            if value != None:
                dictOfValue[countryName] = str(value).strip(" ")

    print dictOfValue

    return dictOfValue


def associateCountryAndValue(pathString, keyToSearch):
    dataFile = open(pathString)
    objJson = json.load(dataFile)

    if(objJson.has_key(keyToSearch)):

        capitalString = objJson[keyToSearch][0]
    else:
        capitalString = "none"
    dataFile.close()
    return capitalString


def make_test_function(description, a, b):
    def test(self):
        self.assertEqual(a, b, description)
    return test

if __name__ == '__main__':

    dictOnCapital = {}
    dictOfBirth = {}
    dictOfExportPartner = {}
    dictOnCapital = createDictionaryForMetaTesting("capital")
    dictOfBirth = createDictionaryForMetaTesting("birth rate")
    dictOfExportPartner = createDictionaryForMetaTesting("export partners")
    testsMapExport = {}
    testsMap = {}
    testsMapStartsWith = {}
    testsMapBirthRate = {}
    currentRealPath = os.getcwd()
    currentRealPath += "\\naturalLanguagePython"


    for country, capital in dictOnCapital.iteritems():
        questionResponder = QuestionResponder(currentRealPath)
        capital = re.split(': |; | \(',capital)[0]
        questionUsedForCompleteCapitalName = "What country has " + capital + " as its capital?"
        questionUsedStartsWithCapitalName = "My capital name starts with " + capital[:4] + "."


        # print questionUsed
        try:

            countryFound = questionResponder.askQuestion(questionUsedForCompleteCapitalName)
            countryFoundStartsWith = questionResponder.askQuestion(questionUsedStartsWithCapitalName)

        except Exception:
            print "\n"
            print "capital injected:"
            print capital
            print "exception with this searching extraction: "
            print questionResponder.countryService.questionAnalyzer.questionDictionary
            countryFoundStartsWith = "Not found"
            countryFound = " Not found"


        testsMap[questionUsedForCompleteCapitalName] = [country,countryFound]
        testsMapStartsWith[questionUsedStartsWithCapitalName] = [country,countryFoundStartsWith]

    for country,birthRate in dictOfBirth.iteritems():
        questionResponder = QuestionResponder(currentRealPath)
        birth = re.split(' \(', birthRate)[0]
        questionUsedWithBirthRate = "My birth rate is " + birth + "."
        try:
            birthFound = questionResponder.askQuestion(questionUsedWithBirthRate)
        except Exception:
            birthFound = "Not found"
            # print "birth rate injected"
            # print birth
            # print "extraction natural language"
            # print questionResponder.countryService.questionAnalyzer.questionDictionary
        testsMapBirthRate[questionUsedWithBirthRate] = [country,birthFound]


    for country,exportPartner in dictOfExportPartner.iteritems():
        questionResponder = QuestionResponder(currentRealPath)
        stringExportPartner = ""
        listItem = []
        for item in exportPartner:
            item.split(" (")[0]
            listItem.append(item)
        stringExportPartner = str(listItem.pop(0))
        for i in listItem:
            stringExportPartner = stringExportPartner + ", " + str(i)

        # exportpart = re.split(' \(', exportPartner)[0]
        questionUsedWithExport = "My export partners are " + stringExportPartner + "."
        try:
            export = questionResponder.askQuestion(questionUsedWithExport)
        except Exception:
            birthFound = "Not found"
            print "birth rate injected"
            print birth
            print "extraction natural language"
            print questionResponder.countryService.questionAnalyzer.questionDictionary
        testsMapBirthRate[questionUsedWithExport] = [country,export]
    for name, params in testsMap.iteritems():
        test_func = make_test_function(name,params[1] , params[0])
        setattr(MetaTestCountry, 'test_{0}'.format(name), test_func)

    for name, params in testsMapStartsWith.iteritems():
        # print params[0]
        test_func = make_test_function(name,params[1] , params[0])
        setattr(MetaTestCountry, 'test_{0}'.format(name), test_func)

    for name, params in testsMapBirthRate.iteritems():
        # print params[0]
        test_func = make_test_function(name,params[1] , params[0])
        setattr(MetaTestCountry, 'test_{0}'.format(name), test_func)

    for name, params in testsMapExport.iteritems():
        # print params[0]
        test_func = make_test_function(name,params[1] , params[0])
        setattr(MetaTestCountry, 'test_{0}'.format(name), test_func)



    suite = unittest.TestLoader().loadTestsFromTestCase(MetaTestCountry)
    suite._tests.sort()
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.TestLoader.discover(unittest.TestLoader(), "C://Users//Antoine//Documents//design3//naturalLanguagePython/")
    unittest.main
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(MetaTestCountry)
    # suite2._tests.sort()
    # unittest.TextTestRunner = suite
    # unittest.TextTestRunner.run(suite)
