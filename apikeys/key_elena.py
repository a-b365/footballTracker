import requests
import os

url = "https://oauth2.elenasport.io/oauth2/token"

Authorization = 'Basic' + ' ' + os.environ['API_KEY']

payload='grant_type=client_credentials'
headers = {
  'Authorization': Authorization,
  'Content-Type': 'application/x-www-form-urlencoded',

}

if __name__!="__main__":

	response = requests.request("POST", url, headers=headers, data=payload)

	tokenData=response.json()

def restrictedFunction():
	return tokenData['token_type']+' '+tokenData['access_token']