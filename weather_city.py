import requests
try:
    city_name = input("Enter city name: ")
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1")
    coordinates = response.json()
    latitude = coordinates['results'][0]['latitude']
    longitude = coordinates['results'][0]['longitude']
    response2 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
    weather = response2.json()
    print(f"Temperature: {weather['current_weather']['temperature']} {weather['current_weather_units']['temperature']}")
    print(f"Windspeed: {weather['current_weather']['windspeed']} {weather['current_weather_units']['windspeed']}")
except requests.exceptions.ConnectionError:
    print("Connection error")
    