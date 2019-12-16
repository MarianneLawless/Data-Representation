import requests
import json

apiKey = '2c9b7439c13cd1787826a685bc11a31e13164e0c'
url = 'https://api.github.com/repos/MarianneLawless/PrivateRepo'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)