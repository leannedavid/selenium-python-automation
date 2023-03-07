import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '0012993441012'}
response = requests.get(baseUrl, params=parameters)
print(response.url)

content = response.content
info = json.loads(content)
print(type(info))
print(info)

item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']

print(title)
print(brand)
print('=================================================================')

parameters2 = {'upc': '073366118238'}
response = requests.get(baseUrl, params=parameters2)
print(response.url)

content = response.content
info = json.loads(content)
print(type(info))
print(info)

item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']

print(title)
print(brand)