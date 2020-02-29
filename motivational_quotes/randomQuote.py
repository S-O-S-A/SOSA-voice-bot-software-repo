import csv
from random import seed
from random import randint

authors = []
quotes = []
transition = []
with open('quotes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader:
        authors.append(row[0])
        quotes.append(row[1])

len = len(authors)
randomNum = randint(0,len-1)
ranFull = randint(0,2)
transition.append(authors[randomNum] + " once said " "\"" +quotes[randomNum] + "\"")
transition.append(authors[randomNum] + " stated " + "\"" +quotes[randomNum] + "\"")
transition.append("\"" +quotes[randomNum] + "\"" + ", spoken by " + authors[randomNum])






print(transition[ranFull])

   
    
