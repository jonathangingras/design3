__author__ = 'alex'
from unittest import TestCase
from naturalLanguagePython.questionLanguageAnalyzer.questionInformationAnalyser import QuestionInformationAnalyser


class testQuestionInformationAnalyser(TestCase):

    def setUp(self):
        self.processLanguage = QuestionInformationAnalyser()


    def test_AnalyseQuestionWithPopulationAsKeySearchingNumberAtTheEndShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population'] = ['1 300 692 576']
        question = "What country has a population greater than 1 300 692 576?"
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithIndependenceAsKeySearchingIncompleteDateAtTheEndShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['independence'] = ['August 1971']
        question = "My independence was declared in August 1971."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithUnemploymentRateAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['unemployment rate'] = ['40.6%']
        question = "My unemployment rate is 40.6%."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithCapitalSearchingIncompleteNameShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['capital'] = ['Moga']
        question = "My capital name starts with Moga."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithDeathRateAndCapitalAsKeysShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['death rate'] = ['15 death/1000']
        expectedDictionary['capital'] = ['Mos']
        question = "My death rate is greater than 15 death/1000 and my capital starts with Mos."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithLongitudeAndLatitudeAsKeysShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['latitude'] = ['16 00 S']
        expectedDictionary['longitude'] = ['167 00 E']
        question = "My latitude is 16 00 S and my longitude is 167 00 E."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithCapitalAsKeySearchingCompleteNameBeforeShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['capital'] = ['Yaounde']
        question = "What country has Yaounde as its capital?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithCapitalAsKeySearchingCompleteNameWithCommaInsideShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['capital'] = ["N'Djamena"]
        question = "What country has N'Djamena as its capital?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithTelephoneLinesInUseAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['telephone lines in use'] = ['1.217 million']
        question = "My telephone lines in use are 1.217 million."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithLatitudeAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['latitude'] = ['41.00 S']
        question = "What country has a latitude of 41.00 S?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithIndependenceAsKeySearchingDateAtTheEndShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['independence'] = ['22 May 1990']
        question = "What country has declared its independence on 22 May 1990?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithNationalSymbolAsKeySearchingValueAtTheEndShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national symbol'] = ['edelweiss']
        question = "One national symbol of this country is the edelweiss."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)



    def test_AnalyseQuestionWithTotalAreaAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['total area'] = ['390757 sq km']
        question = "What country has a total area of 390757 sq km?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithMajorUrbanAreasAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['major urban areas'] = ['Santiago', 'Valparaiso', 'Concepcion']
        question = "The major urban areas of this country are Santiago, Valparaiso and Concepcion. "
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithNationalSymbolAsKeySearchingValueBeforeShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national symbol'] = ['lotus blossom']
        question = "The lotus blossom is the national symbol of this country."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithReligionsAsKeyAndWithLongEnumerationAsValuesShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['religions'] = ['hindu', 'muslim', 'Christian', 'sikh']
        question = "What country has religions including hindu, muslim, Christian, and sikh? "
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)



    def test_AnalyseQuestionWithPopulationAsKeySearchingShortNumberAsValueShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population'] = ['32 742']
        question = "My population is 32 742."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)



    def test_AnalyseQuestionWithNationalSymbolAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national symbol'] = ['elephant']
        question = "My national symbol is the elephant."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithElectricityProductionAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['electricity production'] = ['600', '650 billion kWh']
        question = "My electricity production is between 600 and 650 billion kWh."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithPopulationAsKeySearchingLongNumberShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population'] = ['1 300 692 576']
        question = "What country has a population greater than 1 300 692 576?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithDateOfIndependenceAsKeySearchingCompleteDateShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['date of independence'] = ['22 September 1960']
        question = "22 September 1960 is the date of independence of this country."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithIndependenceAsKeySearchingCompleteDateShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['independence'] = ['22 May 1990']
        question = "What country has declared its independence on 22 May 1990?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithNationalAnthemAsKeySearchingTitleAsValueShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national anthem'] = ['Advance Australia Fair']
        question = "The title of my national anthem is Advance Australia Fair."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithInternetCountryCodeAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['internet country code'] = ['.br']
        question = "My internet country code is .br."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestionWithPopulationGrowthRateAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population growth rate'] = ["1.44%", "1.47%"]
        question = "My population growth rate is between 1.44% and 1.47%."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithCapitalAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['capital'] = ["Ath", "ens"]
        question = "My capital name starts with Ath and ends with ens."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithExportPartnersAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {"export partners" : ["US", "Germany", "UK", "France", "Spain", "Canada", "Italy"]}
        question = "My export partners are US, Germany, UK, France, Spain, Canada and Italy."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithInflationRateAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['inflation rate'] = ["0.3%", "0.5%"]
        question = "What country has an inflation rate between 0.3% and 0.5%?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithBirthRateAndShortCountryNameAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['birth rate'] = ["16 births/1000"]
        expectedDictionary['local short country name'] = ['2 words']
        question = "My birth rate is approximately 16 births/1000 and my local short country name contains 2 words."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithTropicalClimateAndCapitalAsKeysShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['tropical climate'] = ["tropical"]
        expectedDictionary['capital'] = ['Phn']
        question = "What country has a tropical climate and has a capital that starts with the letters Phn?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithDeathRateAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['death rate'] = ["10.37 deaths/1000",'10.40 deaths/1000']
        question = "The death rate of this country is greater than 10.37 deaths/1000 population and less than 10.40 deaths/1000 population."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithImportPartnersAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['import partners'] = ["Netherlands", "France", "China", "Belgium", "Switzerland", "Austria"]
        question = "My import partners include Netherlands, France, China, Belgium, Switzerland and Austria."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithIndustriesAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['industries'] = ["platinum", "gold", "chromium"]
        question = "What country has industries including the world's largest producer of platinum, gold and chromium?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithMaJorUrbanAreasAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['major urban areas'] = ["5.068 million", "1.098 million"]
        question = "What country has major urban areas of 5.068 million and 1.098 million?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithNationalAnthemAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national anthem'] = ["Routhier", "Weir", "Lavallee"]
        question = "The music of my national anthem was composed by Routhier, Weir and Lavallee."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithInternetAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['internet'] = [".dz"]
        question = "What country has .dz as its internet country code?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithReligionsAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['religions'] = ["51.3% of protestant", "0.7% of buddhist"]
        question = "What country has religions including 51.3% of protestant and 0.7% of buddhist?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithIndependenceAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['independence'] = ["1923"]
        question = "In 1923, we proclaimed our independence."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithBirthRateAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['birth rate'] = ["46.12 births/ 1000"]
        question = "What country has a birth rate of 46.12 births/ 1000 population?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithLanguagesAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['languages'] = ["german", "french", "romansch"]
        question = "My languages include german, french and romansch."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithIllicitDrugsActivitiesAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['illicit drugs activities'] = ["transshipment point for cocaine from South America to North America",
        "illicit cultivation of cannabis"]
        question = "What country has illicit drugs activities including a transshipment point for cocaine from South America to North America and illicit cultivation of cannabis?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithUnemploymentRateAndIndustriesAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['unemployment rate'] = ["25%"]
        expectedDictionary['industries'] = ['tourism', 'footwear']
        question = "My unemployment rate is greater than 25% and my industries include tourism and footwear."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithPublicDebtShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['public debt'] = ["7.9% of GDP"]
        question = "My public debt is 7.9% of GDP."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithInternetUsersShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['internet users'] = ["13.694 million"]
        question = "What country has 13.694 million internet users?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithIllicitDrugShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['illicit drug'] = ["serious offense", "carry death penalty"]
        question = "What country considers illicit drug trafficking as a serious offense and carry death penalty?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithPopulationGrowthRateShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population growth rate'] = ["1.46%"]
        question = "What country has a population growth rate of 1.46%?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_addComplexityOnTheNumberUsedForAQuestionWithBetweenAndPercentShoudReturnProperDictionnary(self):
        expectedDictionary = {}
        expectedDictionary['inflation rate'] = ["118.456%", "10.5678%"]
        question = "What country has an inflation rate between 118.456% and 10.5678%?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_useNegativeNumbersForAQuestionWithBetweenAndPercentShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['inflation rate'] = ["-118.456%", "-10.5678%"]
        question = "What country has an inflation rate between -118.456% and -10.5678%?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_useSymbolInTheQuestionSentenceShouldBeCapturedAndReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['electricity production'] = ["600", "650", "billion dollar"]
        question = "My electricity production is between 600$ and 650$ billion dollar."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_useVariateSymbolInQuestionSentenceAtTheEndOfTheStringShouldReturn(self):
        question = "My population is 32 742$#@!^&&*."
        expectedDictionnary = {}
        expectedDictionnary['population'] = ["32 742"]
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionnary)

    def test_useVariateSymbolInQuestionSentenceAtTheBeginningOfTheStringShouldReturn(self):
        question = "$#@!^&&*My population is 32 742."
        expectedDictionnary = {}
        expectedDictionnary['population'] = ["32 742"]
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionnary)

    def test_usepercentageWithoutDecimalSearchingReligionsShouldReturnSomething(self):
        expectedDictionary = {}
        expectedDictionary['religions'] = ["513% of protestant", "076% of buddhist"]
        question = "What country has religions including 513% of protestant and 076% of buddhist?"

        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_usepercentageWithoutDecimalSearchingGDPShouldReturnSomething(self):
        expectedDictionary = {}
        expectedDictionary['public debt'] = ["79% of GDP"]
        question = "My public debt is 79% of GDP."

        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithElectricityProductionUsingReallyBigNumberAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['electricity production'] = ['600 456 345 456', '650 billion kWh']
        question = "My electricity production is between 600 456 345 456 and 650 billion kWh."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithElectricityProductionUsingReallyBigNumberWithDecimalAsKeyShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['electricity production'] = ['600 456 345.456', '650 456 345.456 billion kWh']
        question = "My electricity production is between 600 456 345.456 and 650 456 345.456 billion kWh."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_addBigNumberOnTheNumberUsedForAQuestionWithBetweenAndPercentShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['inflation rate'] = ["23 320.5673%", "34 560.4565%"]
        question = "What country has an inflation rate between 23 320.5673% and 34 560.4565%?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithBirthRateAsKeyUsingBigNumberAsValueShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['birth rate'] = ["46.12 births/ 1000"]
        question = "What country has a birth rate of 46.12 births/ 1000 population?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithDeathRateAsKeyUsingExtremeNumberAndGrammaticalDistortionShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['death rate'] = ["10345 543.37 DEaths/1 000 000.400",'10 3545.40 443 deaths/1000']
        question = "The death rate of this country is greater than 10345 543.37 DEaths/1 000 000.400 population and less than 10 3545.40 443 deaths/1000 population."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithHomeMadeQuestionAndUsingProductionPerDayWithSlashShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['oil production'] = ["3.856 million bbl/day"]
        question = "My country has an oil production greater than 3.856 million bbl/day."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithHomeMadeQuestionAndUsingProductionInCubicMeterPerDayWithSlashShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['gas production'] = ["143.1 billion cubic meter/day"]
        question = "My country has an gas production greater than 143.1 billion cubic meter/day."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithHomeMadeQuestionAndUsingWaterUseInCubicMeterPerYearShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['annual water use'] = ["123 143.1 billion cubic meter"]
        question = "My country has an annual water use greater than 123 143.1 billion cubic meter."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestionWithExportPartnersAsKeyAndCountryNameInTwoWordShouldReturnProperDictionary(self):
        expectedDictionary = {"export partners" : ["US", "Germany", "South Africa", "France", "Spain","United Kingdom", "Canada", "Italy"]}
        question = "My export partners are US, Germany, South Africa, France, Spain, United Kingdom, Canada and Italy."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)









