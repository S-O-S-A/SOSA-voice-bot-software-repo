import csv
from random import seed
from random import randint
import time

jokes = []
punchlines = []
with open('jokes.csv') as csv_file:   
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

   
    
