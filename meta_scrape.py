import os, sys
from os import walk
import glob


# Open a file
path = os.path.join(os.path.dirname(os.getcwd()), "SOSA-voice-bot-software-repo")
dirs = os.listdir(path)
dirList = glob.glob(path)

# for filename in os.listdir(path):
#     print(filename)
#     print(os.path.isdir(filename))
#     if(os.path.isdir(os.listdir(filename))):
#         print(os.listdir(filename))
#     print("\n\n")

# print((os.listdir(path)))
# print(os.path.isdir((os.listdir(path)[13])))

# This would print all the files and directories
# for file in dirs:
#    print (file)

def findFileInfo(current_path):
    for filename in os.listdir(current_path):
        if filename=="activation_phrases.txt": 
            print(os.path.join(current_path, filename))
        elif(os.path.isdir(current_path)):
            print (os.path.join(current_path, filename))
            findFileInfo(os.path.join(current_path, filename))
 
#findFileInfo(path)