__author__ = 'Antoine'
from naturalLanguagePython.countryRessource.questionResponder import QuestionResponder
import os
import sys

if __name__ == "__main__":
    currentRealPath = os.getcwd()
    currentRealPath += "\\naturalLanguagePython"
    question = sys.argv[1]
    questionResponder = QuestionResponder(currentRealPath)
    nameOfCountry = questionResponder.askQuestion(question)
    print(nameOfCountry)