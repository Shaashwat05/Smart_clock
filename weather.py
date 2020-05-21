import requests
import json
from t2s import text_to_speech

api_key = '4221a4f4421fb538b2a650d9c9a3823f'


def set_city(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city 

    response = requests.get(complete_url)

    x = response.json() 

    if x["cod"] != "404": 
        text_to_speech("your city is set")
        valid = True
    else:
        text_to_speech("Invalid city name, give another one.")
        valid = False

    return valid


def weather(city_name):

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

    response = requests.get(complete_url)

    x = response.json() 

    if x["cod"] != "404": 
    
        y = x["main"] 
    
        current_temperature = y["temp"] 
    
        current_pressure = y["pressure"] 
    
        current_humidiy = y["humidity"] 
    
        z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
    
        # print following values 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 

            
    
    else: 
        print(" City Not Found ") 

    return current_temperature, current_humidiy, current_pressure, weather_description