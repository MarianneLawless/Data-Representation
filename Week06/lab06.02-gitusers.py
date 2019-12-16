import requests
import json

apiKey = '1acbfa59e6ff224abc4e5b1284bf3059ea2adac0'
url = 'https://api.github.com/user/repos'

filename ="personal.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (repoJSON)

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)