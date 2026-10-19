import requests
import time

url = 'https://api.binance.com/api/v3/ticker/price'

bit_price = []
for i in range(1,15):
    req = requests.get(url, params={'symbol':'BTCUSDT'})
    price = float(req.json()['price'])
    bit_price.append(price)
    time.sleep(1)

print(bit_price)
print(type(bit_price))
print(max(bit_price))
print(min(bit_price))