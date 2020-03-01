import time

import sys
#sys.path.append('../')
#from motivational_quotes import randomQuote
import motivational_quotes.randomQuote as randomQuote
import quick_commands.jokes.tell_joke as tell_joke
import quick_commands.stories.tell_stories as tell_story
import clock_funcs.dayInfo as dayInfo
import duckduck_search.duckDuckGoSearch as ddgSearch
import weather.get_weather as get_weather

import numpy as np

def compute_jaccard_similarity_score(x, y):
    """
    Jaccard Similarity J (A,B) = | Intersection (A,B) | /
                                    | Union (A,B) |
    """
    intersection_cardinality = len(set(x).intersection(set(y)))
    union_cardinality = len(set(x).union(set(y)))
    return intersection_cardinality / float(union_cardinality)

def maxSim(action_phrases):
    max = 0
    for x in action_phrases:
        score = compute_jaccard_similarity_score(command, x)
        if len(command) >= 10:
            if "search for" in command[0:10]:
                max = -1
                break
        if score > max:
            max = score

    return max



command = input("Please enter a command\n")
score_motiv = maxSim(randomQuote.activationPhrases())
score_joke = maxSim(tell_joke.activationPhrases())
score_story = maxSim(tell_story.activationPhrases())

score_dayInfo = maxSim(dayInfo.activationPhrases())
score_search = maxSim(ddgSearch.activationPhrases())
score_weather = maxSim(get_weather.activationPhrases())


if score_search == -1:
    ddgSearch.ddgSearch(command[10:])
elif (score_weather >= 0.7):
    get_weather.weather()
elif (score_motiv >= 0.7):
    randomQuote.randomQuote()
elif(score_story >= 0.7):
    tell_story.tell_story()
elif (score_joke >= 0.7):
    tell_joke.tell_joke()
elif (score_dayInfo >= 0.8):
    dayInfo.dayInfo()  
else:
    print("I didn't quite get that")
    




