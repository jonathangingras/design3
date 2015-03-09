__author__ = 'alex'
from unittest import TestCase
from naturalLanguagePython.questionLanguageAnalyzer.questionInformationAnalyser import QuestionInformationAnalyser


class testQuestionInformationAnalyser(TestCase):

    def setUp(self):
        self.processLanguage = QuestionInformationAnalyser()

    def test_AnalyseQuestion1ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population'] = ['1 300 692 576']
        question = "What country has a population greater than 1 300 692 576?"
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion2ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['independence'] = ['August 1971']
        question = "My independence was declared in August 1971."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion3ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['unemployment rate'] = ['40.6%']
        question = "My unemployment rate is 40.6%."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion4ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['capital'] = ['Moga']
        question = "My capital name starts with Moga."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion5ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['death rate'] = ['15 death/1000']
        expectedDictionary['capital'] = 'Mos'
        question = "My death rate is greater than 15 death/1000 and my capital starts with Mos."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion6ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['latitude'] = ['16 00 S']
        expectedDictionary['longitude'] = ['167 00 E']
        question = "My latitude is 16 00 S and my longitude is 167 00 E."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion7ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['capital'] = ['Yaounde']
        question = "What country has Yaounde as its capital?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion8ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['telephone lines'] = ['1.217 million']
        question = "My telephone lines in use are 1.217 million."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion9ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['latitude'] = ['41.00 S']
        question = "What country has a latitude of 41.00 S?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion10ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['independence'] = ['22 May 1990']
        question = "What country has declared its independence on 22 May 1990?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion11ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national symbol'] = ['edelweiss']
        question = "One national symbol of this country is the edelweiss."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)



    def test_AnalyseQuestion12ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['total area'] = ['390757 sq km']
        question = "What country has a total area of 390757 sq km?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion13ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['major urban'] = ['Santiago, Valparaiso and Concepcion']
        question = "The major urban areas of this country are Santiago, Valparaiso and Concepcion. "
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion14ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national symbol'] = ['lotus blossom']
        question = "The lotus blossom is the national symbol of this country."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion15ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['religions'] = ['hindu, muslim, Christian, and sikh']
        question = "What country has religions including hindu, muslim, Christian, and sikh? "
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)



    def test_AnalyseQuestion16ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population'] = ['32 742']
        question = "My population is 32 742."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)



    def test_AnalyseQuestion17ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national symbol'] = ['elephant']
        question = "My national symbol is the elephant."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion18ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['electricity production'] = ['600 and 650 billion kWh']
        question = "My electricity production is between 600 and 650 billion kWh."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion19ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population'] = ['1 300 692 576']
        question = "What country has a population greater than 1 300 692 576?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion20ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['date of independence'] = ['22 September 1960']
        question = "22 September 1960 is the date of independence of this country."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion21ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['independence'] = ['22 May 1990']
        question = "What country has declared its independence on 22 May 1990?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion22ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national anthem'] = ['Advance Australia Fair']
        question = "The title of my national anthem is Advance Australia Fair."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion23ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['internet country code'] = ['.br']
        question = "My internet country code is .br."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)


    def test_AnalyseQuestion24ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population growth rate'] = ["1.44% and 1.47%"]
        question = "My population growth rate is between 1.44% and 1.47%."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion25ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['capital'] = ["Ath", "ens"]
        question = "My capital name starts with Ath and ends with ens."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)