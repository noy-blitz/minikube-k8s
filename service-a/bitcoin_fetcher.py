import requests
import time
from statistics import mean

prices = []


def fetch_bitcoin_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    return response.json()['bpi']['USD']['rate_float']


while True:
    price = fetch_bitcoin_price()
    print(f"Bitcoin Price: ${price}")
    prices.append(price)

    if len(prices) >= 10:
        avg_price = mean(prices[-10:])
        print(f"Average Bitcoin Price (last 10 minutes): ${avg_price}")

    time.sleep(60)
