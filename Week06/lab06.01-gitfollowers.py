import requests
import json
#import xlsxwriter
#from xlwt import *

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()
filename = 'gitfollowers.json'

# assign key to json to use for loop
userList = {"user": data}


 #Get the file name for the new file to write
if filename:
    with open(filename, 'w') as f:
     json.dump(data, f, indent = 4)

#w = Workbook()
#ws = w.add_sheet('gitUsers')
#row = 0

# # write headers
#ws.write(row, 0, "login")
#ws.write(row, 1, "id")
#ws.write(row, 2, "node_id")
#ws.write(row, 3, "avatar_url")
#ws.write(row, 4, "gravatar_id")
#ws.write(row, 5, "url")
#ws.write(row, 6, "html_url")
#ws.write(row, 7, "followers_url")
#ws.write(row, 8, "following_url")
#ws.write(row, 9, "gists_url")
#ws.write(row, 10, "starred_url")
#ws.write(row, 11, "subscriptions_url")
#ws.write(row, 12, "organizations_url")
#ws.write(row, 13, "repos_url")
#ws.write(row, 14, "events_url")
#ws.write(row, 15, "received_events_url")
#ws.write(row, 16, "type")
#ws.write(row, 17, "site_admin")

# # move down a row
#row += 1

#for user in userList["user"]:
     #ws.write(row, 0, user["login"])
     #ws.write(row, 1, user["id"])
     #ws.write(row, 2, user["node_id"])
     #ws.write(row, 3, user["avatar_url"])
     #ws.write(row, 4, user["gravatar_id"])
     #ws.write(row, 5, user["url"])
     #ws.write(row, 6, user["html_url"])
     #ws.write(row, 7, user["followers_url"])
     #ws.write(row, 8, user["following_url"])
     #ws.write(row, 9, user["gists_url"])
     #ws.write(row, 10, user["starred_url"])
     #ws.write(row, 11, user["subscriptions_url"])
     #ws.write(row, 12, user["organizations_url"])
     #ws.write(row, 13, user["repos_url"])
     #ws.write(row, 14, user["events_url"])
     #ws.write(row, 15, user["received_events_url"])
     #ws.write(row, 16, user["type"])
     #ws.write(row, 17, user["site_admin"])
     # row+=1

# w.save('githubUsers.xls')