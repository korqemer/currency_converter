import requests
import json


currency_from = input().lower()
currency_rate = dict()

# url creating
url = "http://www.floatrates.com/daily/YOUR_CURRENCY_CODE.json"
ex_string = "YOUR_CURRENCY_CODE"
full_url = url.replace(ex_string, currency_from)

# data
request_data = requests.get(full_url)
json_data = request_data.json()

if currency_from == 'usd':
    currency_rate['eur'] = json_data['eur']['rate']

elif currency_from == "eur":
    currency_rate['eur'] = json_data['eur']['rate']

else:
    currency_rate['usd'] = json_data['usd']['rate']
    currency_rate['eur'] = json_data['eur']['rate']



while True:

    currency_to = input().lower()
    if len(currency_to) == 0:
        break

    amount_money = float(input())

    print("Checking the cache...")

    if currency_to in currency_rate.keys():
        print("Oh! It is in the cache!")
        money = amount_money * currency_rate[currency_to]
        money = round(money, 2)
        print("You received {} {}.".format(money, currency_to.upper()))

    else:
        print("Sorry, but it is not in the cache!")
        currency_rate[currency_to] = json_data[currency_to]['rate']
        money = amount_money * currency_rate[currency_to]
        money = round(money, 2)
        currency_rate[currency_to] = json_data[currency_to]['rate']
        print("You received {} {}.".format(money, currency_to.upper()))



