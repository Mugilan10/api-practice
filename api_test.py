import requests
try:
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true")
    weather_data = response.json()
    print(f'Temperature: {weather_data['current_weather']['temperature']} {weather_data['current_weather_units']['temperature']}')
    print(f'Windspeed: {weather_data['current_weather']['windspeed']} {weather_data['current_weather_units']['windspeed']}')
except requests.exceptions.ConnectionError:
    print('Connection error')