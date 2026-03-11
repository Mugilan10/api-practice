import requests
try:
    city_name = input("Enter city name: ")
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1")
    coordinates = response.json()
    if 'results' not in coordinates:
        print("City not found")
    else:
        latitude = coordinates['results'][0]['latitude']
        longitude = coordinates['results'][0]['longitude']
        response2 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
        weather = response2.json()
        temperature = weather['current_weather']['temperature']
        windspeed = weather['current_weather']['windspeed']
        print(f"Temperature: {temperature} {weather['current_weather_units']['temperature']}")
        print(f"Windspeed: {windspeed} {weather['current_weather_units']['windspeed']}")
        if temperature > 35:
            print("Its hot today")
        elif 20 < temperature < 35:
            print("Its pleasant today")
        elif temperature < 20:
            print("Its cold today")
except requests.exceptions.ConnectionError:
    print("Connection error")
    