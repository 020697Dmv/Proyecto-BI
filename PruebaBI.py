import json

from googleapiclient.discovery import build

api_key = 'AIzaSyDEyzx3wWj6e1NGuw_bBngQB-2anQ_uda4'

youtube = build('youtube', 'v3', developerKey=api_key)


listas = ['PL1av4CQniLB0dk5LnfWQhBUcRlzo2jBYB','PL952AEBEF137A5446']
archivos=[]
pagina=None
aux=True

while aux==True or pagina!=None:
	pl_request = youtube.playlistItems().list(
	part='contentDetails',
	playlistId="PLmBFTxNFZbn_ROiUGJwVjvXy7sT6gC-ZQ",
	maxResults=50,pageToken=pagina


	)

	aux=False
	pl_response = pl_request.execute()
	try:
		pagina=pl_response['nextPageToken']
		vid_ids=[]

		for item in pl_response['items']:
			vid_ids.append(item['contentDetails']['videoId'])

		vid_request= youtube.videos().list(

			part="snippet",
			id=','.join(vid_ids)
		)
		vid_response= vid_request.execute()
		archivos.extend(vid_response['items'])


	except Exception as e:
		pagina=None
	
	#print(len(archivos))

print(archivos[0])


#data_json= data.__json
'''for x in archivos:

	f = open("arc"+x['id']+".json", "x")

	f.write(json.dumps(x))
	f.close()
'''