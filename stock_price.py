import requests

try:
    stock_name = input("Enter the stock name(abbreviated): ")
    stock_name = stock_name.upper()
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{stock_name}",headers=headers)
    stock_data = response.json()
    print(stock_data['chart']['result'][0]['meta']["regularMarketPrice"])
except requests.exceptions.ConnectionError:
    print("Connection error")