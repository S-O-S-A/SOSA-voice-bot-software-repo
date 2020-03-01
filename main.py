import time

import sys
#sys.path.append('../')
#from motivational_quotes import randomQuote
import motivational_quotes.randomQuote as randomQuote
import quick_commands.jokes as tell_joke
import clock_funcs.dayInfo as dayInfo
import duckduck_search.duckDuckGoSearch as ddgSearch

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
#score_joke = maxSim(tell_joke.tell_joke.activationPhrases())
score_dayInfo = maxSim(dayInfo.activationPhrases())
score_search = -1

if score_search == -1:
    ddgSearch.ddgSearch(command[10:])
elif (score_motiv >= 0.6):
    randomQuote.randomQuote()
elif (score_dayInfo >= 0.6):
    dayInfo.dayInfo()    
else:
    print("I didn't quite get that")
    




