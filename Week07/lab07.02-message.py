# [START gmail_quickstart]

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
   
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
 
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    response = service.users().messages().list(userId='me').execute()
    #print (response)
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId='me', pageToken=page_token).execute()
      messages.extend(response['messages'])

    for message in messages:
       #print(message['id'])
        completeMessage = service.users().messages().get(userId='me', id = message['id']).execute()
        #print(completeMessage['snippet'])
        headers = completeMessage['payload']['headers']
        #print (headers)
        snippet = completeMessage['snippet']
        subject = list(filter(lambda h: h['name']=='Subject',headers))[0]['value']
        massageTo = list(filter(lambda h: h['name']=='To',headers))[0]['value']
        messageFrom = list(filter(lambda h: h['name']=='From',headers))[0]['value']
        #print (messageFrom)
        # you can put this information into an excel spreadsheet here
        

    
    with open('aMessage.json', 'w') as f:
        json.dump(completeMessage, f, indent=4)
    

if __name__ == '__main__':
    main()
# [END gmail_quickstart]