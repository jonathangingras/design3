import os
from unittest import TestCase
from naturalLanguagePython.countryRessource.questionResponder import QuestionResponder
__author__ = 'Antoine'


class TestQuestionResponder(TestCase):

    def setUp(self):
        path = os.getcwd()
        self.questionResponder = QuestionResponder(path)

    def test_askingQuestionWhenSearchingByCountryCapitalShouldReturnTheNameOfCorrespondingCountry(self):
        askedQuestion = "What country has Yaounde as its capital?"
        expectedNameOfCountry = "Cameroon"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsUnemploymentRateShouldReturnTheNameOfCorrespondingCountry(self):
        askedQuestion = "My unemployment rate is 40.6%."
        expectedNameOfCountry = "Haiti"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsInternetCodeShouldReturnTheNameOfCorrespondingCountry(self):
        askedQuestion = "My internet country code is .br."
        expectedNameOfCountry = "Brazil"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsYearAndMonthOfIndependenceShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "My independence was declared in August 1971."
        expectedNameOfCountry = "Bahrain"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByOneOfItsNationalSymbolShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "One national symbol of this country is the edelweiss."
        expectedNameOfCountry = "Austria"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsNumberOfInternetUsersShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "What country has 13.694 million internet users?"
        expectedNameOfCountry = "Argentina"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsNationalSymbolShouldReturnCountryName(self):
        askedQuestion = "My national symbol is the edelweiss."
        expectedNameOfCountry = "Austria"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsBirthRateShouldReturnCountryName(self):
        askedQuestion = "What country has a birth rate of 46.12 births/ 1000 population?"
        expectedNameOfCountry = "Niger"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsTelephoneLinesNumbersShouldReturnNameOfCountry(self):
        askedQuestion = "My telephone lines in use are 1.217 million."
        expectedNameOfCountry = "Cuba"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsNationalAnthemShouldReturnTheNameOfCountry(self):
        askedQuestion = "The title of my national anthem is Advance Australia Fair."
        expectedNameOfCountry = "Australia"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsExportPartnerShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "My export partners are US, Germany, UK, France, Spain, Canada and Italy."
        expectedNameOfCountry = "Bangladesh"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsReligionsPercentageShouldReturnTheNameOfCountry(self):
        askQuestion = "What country has religions including 51.3% of protestant and 0.7% of buddhist?"
        expectedNameOfCountry = "United_States"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askQuestion))

    def test_askingQuestionWhenSearchingByItsTotalAreaShouldReturnTheNameOfCountry(self):
        askQuestion = "What country has a total area of 390757 sq km?"
        expectedNameOfCountry = "Zimbabwe"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askQuestion))

    def test_askingQuestionWhenSearchingByItsReligionsShouldReturnCountryName(self):
        askedQuestion = "What country has religions including hindu, muslim, christian, and sikh?"
        expectedNameOfCountry = "India"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsIndependenceDateInBeginningShouldReturnCountryName(self):
        askedQuestion = "22 September 1960 is the date of independence of this country."
        expectedNameOfCountry = "Mali"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsLatitudeAndLongitudeShouldReturnTheNameOfTheCountry(self):
        askedQuestion = "My latitude is 16 00 S and my longitude is 167 00 E."
        expectedNameOfCountry = "Vanuatu"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByThePopulationGrowthRateShouldReturnTheNameOfTheCountry(self):
       askedQuestion = "My population growth rate is between 1.44% and 1.47%."
       expectedNameOfCountry = "Israel"
       self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheLatitudeShouldReturnCountryName(self):
        askedQuestion = "What country has a latitude of 41.00 S? "
        expectedNameOfCountry = "New_Zealand"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheNationalSymbolAtBeginningShouldReturnCountryName(self):
        askedQuestion = "The lotus blossom is the national symbol of this country."
        expectedNameOfCountry = "Vietnam"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByThePopulationNumberShouldReturnCountryName(self):
        askedQuestion = "My population is 32 742. "
        expectedNameOfCountry = "San_Marino"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheLanguagesShouldReturnTheNameOfCountry(self):
        askedQuestion = "My languages include german, french and romansch."
        expectedNameOfCountry = "Switzerland"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByThePublicDebtShouldReturnCountryName(self):
        askedQuestion = "My public debt is 7.9% of GDP"
        expectedNameOfCountry = "Russia"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheAuthorsOfTheNationalAnthemShouldReturnCountryName(self):
        askedQuestion = "The music of my national anthem was composed by Routhier, Weir and Lavallee."
        expectedNameOfCountry = "Canada"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByThePopulationOfMajorUrbanAreasShouldReturnCountryName(self):
        askedQuestion = "What country has major urban areas of 5.068 million and 1.098 million?"
        expectedNameOfCountry = "Angola"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheImportsPartnersShouldReturnCountryName(self):
        askedQuestion = "My import partners include Netherlands, France, China, Belgium, Switzerland and Austria."
        expectedNameOfCountry = "Germany"
        self.assertEqual(expectedNameOfCountry, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheStartsAndEndsPartOfCapitalNameShouldReturnNameOfCountry(self):
        askedQuestion = "My capital name starts with Ath and ends with ens."
        expectedCountryName = "Greece"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheNameOfMajorUrbanAreaShouldReturnNameOfTheCountry(self):
        askedQuestion = "The major urban areas of this country are Santiago, Valparaiso and Concepcion."
        expectedCountryName = "Chile"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheDateOfIndependenceShouldReturnCountryName(self):
        askedQuestion = "What country has declared its independence on 22 May 1990?"
        expectedCountryName = "Yemen"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheMajorIndustriesShouldReturnCountryName(self):
        askedQuestion = "What country has industries including the world's largest producer of platinum, gold and chromium?"
        expectedCountryName = "South_Africa"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByGreaterPopulationShouldReturnCountryName(self):
        askedQuestion = "What country has a population greater than 1 300 692 576?"
        expectedCountryName = "China"
        dictionary = self.questionResponder.askQuestion(askedQuestion)
        self.assertEqual(expectedCountryName, dictionary)

    def test_askingQuestionWhenSearchingByTheStartsPartOfAQuestionShouldReturnCountryName(self):
        askedQuestion = "My capital name starts with Moga."
        expectedCountryName = "Somalia"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheYearOfTheIndependenceShouldReturnCountryName(self):
        askedQuestion = "In 1923, we proclaimed our independence"
        expectedCountryName = "Turkey"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheCountryInternetCodeShouldReturnCountryName(self):
        askedQuestion = "What country has .dz as its internet country code?"
        expectedCountryName = "Algeria"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheExactPopulationGrowthRatePercentageShouldReturnCountryName(self):
        askedQuestion = "What country has a population growth rate of 1.46%"
        expectedCountryName = "Israel"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheClimateAndTheStartsPortionOfCapitalNameShouldReturnCountryName(self):
        askedQuestion = "What country has a tropical climate and has a capital that starts with the letters Phn?"
        expectedCountryName = "Cambodia"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheIllegalActivitiesShouldReturnCountryName(self):
        askedQuestion = "What country has illicit drugs activities including a transshipment point for cocaine from South America to North America and illicit cultivation of cannabis?"
        expectedCountryName = "Jamaica"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByTheIllicitDrugPenaltyShouldReturnCountryName(self):
        askedQuestion = "What country considers illicit drug trafficking as a serious offense and carry death penalty?"
        expectedCountryName = "Brunei"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByGreaterDeathRateAndStartPortionOfCapitalShouldReturnCountryName(self):
        askedQuestion = "My death rate is greater than 13 deaths/1000 and my capital starts with Mos."
        expectedCountryName = "Russia"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByBetweenTheElectricityProductionShouldReturnCountryName(self):
        askedQuestion = "My electricity production is between 600 and 650 billion kWh."
        expectedCountryName = "India"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsInflationRateBetweenShouldReturnCountryName(self):
        askedQuestion = "What country has an inflation rate between 0.3% and 0.5%?"
        expectedCountryName = "Falkland_Islands_(Islas_Malvinas)"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByItsBetweenDeathRatesShouldReturnCountryName(self):
        askedQuestion = "The death rate of this country is greater than 10.37 deaths/1000 population and less than 10.40 deaths/1000 population."
        expectedCountryName = "Austria"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))

    def test_askingQuestionWhenSearchingByIndustriesAndUnemploymentRateShouldReturnCountryName(self):
        askedQuestion = "My unemployment rate is greater than 24% and my industries include tourism and footwear."
        expectedCountryName = "Greece"
        self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))
    #
    # def test_askingQuestionWhenSearchingByItsLocalShortCapitalNameCompositionAndByTheApproximationOfBirthShouldReturnCountryName(self):
    #     askedQuestion = "My country has an oil production greater than 3.856 million bbl/day."
    #     expectedCountryName = "canada"
    #     self.assertEqual(expectedCountryName, self.questionResponder.askQuestion(askedQuestion))