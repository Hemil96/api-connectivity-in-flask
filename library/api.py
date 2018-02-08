# Importe libraries
import requests
import json

url = "https://coinbin.org/coins" #API URl
api = requests.get(url).text #Getting html response to text
dic = json.loads(api) #converting JSON into python dict 

def coin(name):
	coin_data =  dic["coins"][name]
	return coin_data

