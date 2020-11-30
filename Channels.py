import requests  
import json

from googleapiclient.discovery import build

api_key='AIzaSyBvL8A6Gheekl91Z9ppRPJ06c_YygLNNX8'

youtube = build('youtube', 'v3', developerKey=api_key)

request_channel= youtube.channels().list(

				part='snippet',
				forUsername='vegetta777'
			)
responde = request_channel.execute()

print(responde)
	