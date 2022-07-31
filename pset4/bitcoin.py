import requests
import sys
import json


if len(sys.argv) <2:
    sys.exit('Missing command-line argument')

try:
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
    o=response.json()
    # p=json.dumps((o),indent=2) --> to check response skeleton

    live_rate = float((o['bpi']['USD']['rate_float']))
    amount = float(sys.argv[1]) *live_rate
    print(f"${amount:,.4f}")

except ValueError:
    sys.exit('Command-line argument is not number')
except requests.RequestException:
    pass