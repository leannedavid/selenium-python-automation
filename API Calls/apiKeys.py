import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '3d84c102edb14f972e652eb839d015ab', 'q': 'Seattle,US'}

response = requests.get(baseUrl, params=parameters)
print(response.content)