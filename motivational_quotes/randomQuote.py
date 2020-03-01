import csv
from random import seed
from random import randint
import os

def randomQuote():
    file_to_reference = "quotes.csv"
    real_path = os.path.join(os.path.dirname(__file__),file_to_reference)
    authors = []
    quotes = []
    transition = []
    with open(real_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') 
        for row in csv_reader:
            authors.append(row[0])
            quotes.append(row[1])

    size = len(authors)
    randomNum = randint(0,size-1)
    ranFull = randint(0,2)
    transition.append(authors[randomNum] + " once said " "\"" +quotes[randomNum] + "\"")
    transition.append(authors[randomNum] + " stated " + "\"" +quotes[randomNum] + "\"")
    transition.append("\"" +quotes[randomNum] + "\"" + ", spoken by " + authors[randomNum])

    print(transition[ranFull])

def activationPhrases():
    act = []

    
    act.append("what's a motivational quote")
    act.append("inspire me")
    act.append("I need something motivational")
    act.append("I need something inspirational")
    act.append("I need  to hear something motivational")
    act.append("What's a good quote")
    act.append("Give me a quote")

    return act
    
