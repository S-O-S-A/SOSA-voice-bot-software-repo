import time

import sys
#sys.path.append('../')
#from motivational_quotes import randomQuote
import motivational_quotes.randomQuote as randomQuote
from quick_commands.jokes import tell_joke
import clock_funcs
import clock_funcs 
import clock_funcs 
import weather 
import numpy as np

def compute_jaccard_similarity_score(x, y):
    """
    Jaccard Similarity J (A,B) = | Intersection (A,B) | /
                                    | Union (A,B) |
    """
    intersection_cardinality = len(set(x).intersection(set(y)))
    union_cardinality = len(set(x).union(set(y)))
    return intersection_cardinality / float(union_cardinality)


command = input("Please enter a command\n")
score_motiv = compute_jaccard_similarity_score(command, "motivational quote")
score_joke = compute_jaccard_similarity_score(command, "say a funny joke")
score_weather = compute_jaccard_similarity_score(command, "what's the weather")

print(score)
if (score > 0.6):
    randomQuote.randomQuote()
elif ("joke" in command):
    tell_joke.tell_joke()
else:
    print("I didn't quite get that")
    




