import requests
import json

citydata = {}
weather_data = {}
pollution_data = {}
country = input("Enter the country: ")
state = input("Enter the State: ")
city = input("Enter the City: ")

city = 'http://api.airvisual.com/v2/city?city='+city+'&state='+state+'&country='+country+'&key=d569d0d1-520f-4b85-83e5-1903cb622fd8'

response = requests.get(city)

citydata = response.json()

status = citydata['status']
print("Status:      ", status)
city = citydata['data']['city']
print("City:        ",city)
weather_data = citydata['data']['current']['weather']
pollution_data = citydata['data']['current']['pollution']
temperature = weather_data['tp']
pressure = weather_data['pr']
wind_speed = weather_data['ws']
humidity = weather_data['hu']
air_quality = pollution_data['aqius']

print("Temperature: ", temperature ,"\nPressure:    ", pressure, "\nwind_speed:  ", wind_speed, "\nHumidity:    ", humidity ,"\nAir Quality: ", air_quality)
