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
        expectedDictionary['capital'] = ['Mos']
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
        expectedDictionary['telephone lines in use'] = ['1.217 million']
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
        expectedDictionary['major urban areas'] = ['Santiago', 'Valparaiso', 'Concepcion']
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
        expectedDictionary['religions'] = ['hindu', 'muslim', 'Christian', 'sikh']
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
        expectedDictionary['electricity production'] = ['600', '650 billion kWh']
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
        expectedDictionary['population growth rate'] = ["1.44%", "1.47%"]
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

    def test_AnalyseQuestion26ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['export partners'] = ["US", "Germany", "UK", "France", "Spain", "Canada", "Italy"]
        question = "My export partners are US, Germany, UK, France, Spain, Canada and Italy."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion27ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['inflation rate'] = ["0.3%", "0.5%"]
        question = "What country has an inflation rate between 0.3% and 0.5%?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion28ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['birth rate'] = ["16 births/1000"]
        expectedDictionary['local short country name'] = ['2 words']
        question = "My birth rate is approximately 16 births/1000 and my local short country name contains 2 words."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion29ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['tropical climate'] = ["tropical"]
        expectedDictionary['capital'] = ['Phn']
        question = "What country has a tropical climate and has a capital that starts with the letters Phn?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion30ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['death rate'] = ["10.37 deaths/1000",'10.40 deaths/1000']
        question = "The death rate of this country is greater than 10.37 deaths/1000 population and less than 10.40 deaths/1000 population."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion31ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['import partners'] = ["Netherlands", "France", "China", "Belgium", "Switzerland", "Austria"]
        question = "My import partners include Netherlands, France, China, Belgium, Switzerland and Austria."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion32ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['industries'] = ["platinum", "gold", "chromium"]
        question = "What country has industries including the world's largest producer of platinum, gold and chromium?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion33ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['major urban areas'] = ["5.068 million", "1.098 million"]
        question = "What country has major urban areas of 5.068 million and 1.098 million?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion34ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['national anthem'] = ["Routhier", "Weir", "Lavallee"]
        question = "The music of my national anthem was composed by Routhier, Weir and Lavallee."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion35ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['internet'] = [".dz"]
        question = "What country has .dz as its internet country code?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion36ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['religions'] = ["51.3% of protestant", "0.7% of buddhist"]
        question = "What country has religions including 51.3% of protestant and 0.7% of buddhist?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion37ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['independence'] = ["1923"]
        question = "In 1923, we proclaimed our independence."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion38ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['birth rate'] = ["46.12 births/ 1000"]
        question = "What country has a birth rate of 46.12 births/ 1000 population?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion39ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['languages'] = ["german", "french", "romansch"]
        question = "My languages include german, french and romansch."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion40ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['illicit drugs activities'] = ["transshipment point for cocaine from South America to North America",
        "illicit cultivation of cannabis"]
        question = "What country has illicit drugs activities including a transshipment point for cocaine from South America to North America and illicit cultivation of cannabis?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion41ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['unemployment rate'] = ["25%"]
        expectedDictionary['industries'] = ['tourism', 'footwear']
        question = "My unemployment rate is greater than 25% and my industries include tourism and footwear."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion42ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['public debt'] = ["7.9% of GDP"]
        question = "My public debt is 7.9% of GDP."
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion43ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['internet users'] = ["13.694 million"]
        question = "What country has 13.694 million internet users?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion44ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['illicit drug'] = ["serious offense", "carry death penalty"]
        question = "What country considers illicit drug trafficking as a serious offense and carry death penalty?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

    def test_AnalyseQuestion46ShouldReturnProperDictionary(self):
        expectedDictionary = {}
        expectedDictionary['population growth rate'] = ["1.46%"]
        question = "What country has a population growth rate of 1.46%?"
        self.processLanguage = QuestionInformationAnalyser()
        self.processLanguage.analyseQuestion(question)
        self.assertDictEqual(self.processLanguage.questionDictionary, expectedDictionary)

