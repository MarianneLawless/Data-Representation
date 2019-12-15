import requests
import json
from xlwt import *

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

w = Workbook()
ws = w.add_sheet('cars')
row = 0

# write headers
ws.write(row, 0, "reg")
ws.write(row, 1, "make")
ws.write(row, 2, "model")
ws.write(row, 3, "price")

# move down a row
row += 1

for car in data["cars"]:
    ws.write(row, 0, car["reg"])
    ws.write(row, 1, car["make"])
    ws.write(row, 2, car["model"])
    ws.write(row, 3, car["price"])
    row+=1

w.save('cars.xls')