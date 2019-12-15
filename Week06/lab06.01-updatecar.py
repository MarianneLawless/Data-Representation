import requests
import json

dataString = {'make':'Ford', 'model':'Kuga'}
url = "http://127.0.0.1:5000/cars/08%20C%204567"

response = requests.put(url, json=dataString)

print(response.status_code)
print(response.text)