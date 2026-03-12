# API practice programs
Command-line programs using APIs built in python

## api_test - What it does
- uses https://api.open-meteo.com/v1/forecast?
- retrieves weather data for latitude=13.08, longitude=80.27 in json format
- prints weather and windspeed
- uses requests.exceptions.ConnectionError in except block to prevent program from crashing

## weather_city - What it does
- uses https://geocoding-api.open-meteo.com/v1/search?
- takes user input and uses it in fstring to fetch location data using geocoding-api
- extracts longitude and latitude from location data and uses it in fstring to fetch weather data of that location
- prints weather and windspeed
- also prints brief description of weather
- also handles connection error

## crypto_price.py - What it does
- uses https://api.coingecko.com/api/v3/simple/price?
- takes user input and uses it in fstring to fetch exchange rate of crypto using coingecko-api
- prints exchange rate in usd
- also handles Key error if invalid currency given as input
- also handles connection error

## stock_price.py - What it does
- uses https://query1.finance.yahoo.com/v8/finance/chart/
- uses headers (Mozilla/5.0) to simulate browser as it does not allow "bots" to access it
- also handles connection error