import socket
import requests
import json
import pytemperature
from requests import get
import pycountry

#Check your IP
#ip = socket.gethostbyname(socket.gethostname())
#print(ip)
#This IP is used since the website can't find the weather according to Israeli IP
ip = '208.67.222.222'
#Get weather coordination
latlong = get('https://ipapi.co/{}/latlong/'.format(ip)).text.split(',')
#Get weather
weather = get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=24b52b13fae832ec6edd1f353d45b150'.format(latlong[0], latlong[1])).json()

#Print weather details to a file
with open('weather_details.txt', 'w') as json_file:
    json.dump(weather, json_file)

#Print 10 cities temperature
cities = { 'London', 'New York', 'France', 'Tel Aviv', 'Tokyo', 'Toronto', 'Berlin', 'Madrid', 'Boston', 'Rome'}
for x in cities:
    city_weather = get('http://api.openweathermap.org/data/2.5/weather?appid=24b52b13fae832ec6edd1f353d45b150&q='+x).json()
    temp_in_celsius = pytemperature.k2c(city_weather['main']['temp'])
    country = city_weather['sys']['country']
#    full_country_name = pycountry-convert.country_alpha3_to_country_name(cn_name_format="default")
    full_country_name = pycountry.countries.get(alpha_2=country)
    print('The weather in  '+ x + ', ' + full_country_name.name + ' is ' + str(round(temp_in_celsius)) + ' degrees')








