import requests

try:
    cryptocurrency = input("Enter the cryptocurrency name: ")
    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={cryptocurrency}&vs_currencies=usd")
    data = response.json()
    try:
        print(f"{data[cryptocurrency]['usd']} usd")
    except KeyError:
        print("Invalid cryptocurrency")
except requests.exceptions.ConnectionError:
    print("Connection error")