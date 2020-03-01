import csv
from random import seed
from random import randint
import time
import os

def tell_story():

    file_to_reference = "stories.csv"
    real_path = os.path.join(os.path.dirname(__file__),file_to_reference)
    titles = []
    stories = []
    with open(real_path) as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter=',') 
        for row in csv_reader:
            titles.append(row[0])
            stories.append(row[1])

    length = len(titles)
    randomNum = randint(0,length-1)
    title = titles[randomNum]
    story = stories[randomNum]

    print("Lets hear a story about " + title)
    time.sleep(1)
    print(story)

   
    
