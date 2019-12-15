import requests
import json

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()
filename = 'cars.json'

#writes cars to json file
if filename:
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 4)