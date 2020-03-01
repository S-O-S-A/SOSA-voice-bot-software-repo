import json
import os

def getCity():
    file_to_reference = "setup.json"
    real_path = file_to_reference
    json_file = open(real_path, 'r')
    json_as_string = json_file.read()
    json_as_dict = json.loads(json_as_string)
    city = json_as_dict["location"]["city"]
    return city
