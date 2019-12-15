import requests

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

#output to console
print (data)