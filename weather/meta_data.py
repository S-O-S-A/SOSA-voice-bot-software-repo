import json


def getCity():
    json_file = open('../setup.json', 'r')
    json_as_string = json_file.read()
    json_as_dict = json.loads(json_as_string)
    city = json_as_dict["location"]["city"]
    return city
