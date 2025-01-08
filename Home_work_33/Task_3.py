#The Weather app

#Write a console application which takes as an input a city name and returns current weather in the format of your choice. 
# For the current task, you can choose any weather API or website or use openweathermap.org 

import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()
key = os.getenv('WEATHER_API_KEY')
city = input("Write name of city: ")
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
response = requests.get(geo_url)
geo_data = response.json()
#pprint(geo_data)

if geo_data:
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    pprint(weather_data)
else:
    print("City not found")
