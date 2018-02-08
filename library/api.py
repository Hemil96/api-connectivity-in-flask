# Importe libraries
import requests
import json

url = "https://coinbin.org/coins" #API URl
api = requests.get(url).text #Getting html response to text
dic = json.loads(api) #converting JSON into python dict 
coin_list = ["temp"]
for key, value in dic.iteritems():
    for key in value:
    	coin_list.append(key)

#Direct Key : value
def coin(name):
	name = name.lower()
	if name not in coin_list:
		return full_name(name)
		# return "n/a"
	else:
		coin_data =  dic["coins"][name]
	return coin_data
#Finding name from value 
def full_name(name):
	for key, value in dic.iteritems():
		for key_inner, value_inner in value.iteritems():
			if value_inner["name"].lower() == name:
				print value_inner
				return value_inner
				break
			else:
				pass
		return "n/a"



				

