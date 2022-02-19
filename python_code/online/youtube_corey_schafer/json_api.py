import json
from urllib.request import urlopen

with urlopen("https://uk.finance.yahoo.com/currencies") as response:
	source = response.read()	

print(source)

data = json.loads(source)

print(json.dumps(data, indent=2))

print(len(data['list']['resources']))

usd_rates = dict()

for item in data['list']['resources']:
	name = item['resources']['fields']['name']
	price = item['resources']['fields']['price']
	usd_rates[name] = price

print(usd_rates['USD/EUR'])
print(50 * flout(usd_rates['USD/EUR']))
print(50 * flout(usd_rates['USD/INR']))