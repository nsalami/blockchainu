import requests
import os
import time

## for urllib2 json importing line would be json.loads(), must also import json

resp = requests.get("https://api.bitcoinaverage.com/ticker/USD/")
f = resp.json()
oldprice = f['last']

while True:
	resp = requests.get("https://api.bitcoinaverage.com/ticker/USD/")
	g = resp.json()
	price = g['last']
	if price > oldprice * 1.05:
		## for terminal ping, next line would be print('/a')
		os.system('say "alert bitcoin price up to %d dollars from %d "' % (price, oldprice))
		oldprice = price
	elif price < oldprice * .95:
		os.system('say "alert bitcoin price down to %d dollars from %d "' % (price, oldprice))
		oldprice = price
	else:
		pass
	time.sleep(10)
