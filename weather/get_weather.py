# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules 
import requests, json 
import pytemperature
from weather import meta_data

# Enter your API key here 
api_key = "d3a6d162b370e498c0bbd193a41c7b7b"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def weather():
    # Give city name 
    city_name = meta_data.getCity()
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 

        # store the value corresponding 
        # to the "temp_max" key of y 
        current_high_temperature = y["temp_max"] 

        # store the value corresponding 
        # to the "temp_min" key of y 
        current_low_temperature = y["temp_min"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
    
        # print following values 
        print("description = " + str(weather_description)
        + "\n humidity (in percentage) = " + str(current_humidiy)
        + "\n current temperature (in Fahrenheit unit) = " + str(pytemperature.k2f(current_temperature))
        + "\n high temperature of " + str(pytemperature.k2f(current_high_temperature))
        + "\n low temperature of " + str(pytemperature.k2f(current_low_temperature)))

    else: 
        print("Could not find weather data for the city")

def activationPhrases():
    act = []

    act.append("what's the weather like today")
    act.append("what is the weather like today")
    act.append("How is the weather")
    act.append("Should I wear a coat")
    act.append("Do I need an umbrella")

    return act