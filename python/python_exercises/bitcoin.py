import json
import requests
import sys

if not sys.argv:
    sys.exit("missing command-line argument")
elif len(sys.argv) < 2:
    sys.exit("the argument is not a number")
else:
    change = float(sys.argv[1])

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
    amount = change * price
    print(f'{amount:,.4f}')
except requests.RequestException:
    print("sorry")

