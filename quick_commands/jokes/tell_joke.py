import csv
from random import seed
from random import randint
import time
import os


def tell_joke():
    file_to_reference = "jokes.csv"
    real_path = os.path.join(os.path.dirname(__file__),file_to_reference)

    jokes = []
    punchlines = []
    with open(real_path) as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter=',') 
        for row in csv_reader:
            jokes.append(row[0])
            punchlines.append(row[1])

    length = len(jokes)
    randomNum = randint(0,length-1)
    joke = jokes[randomNum]
    punchline = punchlines[randomNum]

    print(joke)
    time.sleep(2)
    print(punchline)

   
    
