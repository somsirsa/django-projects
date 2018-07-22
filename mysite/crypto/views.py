from django.shortcuts import render
import requests
import json

def home(request):
	#Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
	price = json.loads(price_request.content)

	#Grab Crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)

	return render(request,'home.html', {'api': api, 'price': price})


def prices(request):
	#Grab Crypto Price Data
	if request.method == 'POST':
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request,'prices.html',{'quote': quote, 'crypto': crypto})
	else:
		notfound = "Enter a crypto currency symbol in the form above..."
		return render(request,'prices.html',{'notfound': notfound})


def prices2(request):
	stream_request = requests.get("https://api.coinmarketcap.com/v2/ticker/?limit=50&sort=rank")
	stream = json.loads(stream_request.content)
	return render(request, 'prices2.html', {'stream': stream})