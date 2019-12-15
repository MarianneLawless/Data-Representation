import requests

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

#prints to console one by one
for car in data["cars"]:
    print(car)