import time

import sys
sys.path.append('../')
from motivational_quotes import randomQuote
from quick_commands.jokes import tell_joke
import clock_funcs
import clock_funcs 
import clock_funcs 
import weather 




command = input("Please enter a command\n")

if ("motivational quote" in command):
    randomQuote.randomQuote()
elif ("joke" in command):
    tell_joke.tell_joke()
else:
    print("I didn't quite get that")
    




