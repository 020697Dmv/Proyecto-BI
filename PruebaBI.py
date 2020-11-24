from googleapiclient.discovery import build

api_key = 'AIzaSyCK2qE6uIz7QLqybqW9SX12r5MokRFkF4M'

youtube = build('youtube', 'v3', developerKey=api_key)

'''pl_request = youtube.playlistItems().list(
	part='contentDetails',
	playlistId="PL1av4CQniLB0dk5LnfWQhBUcRlzo2jBYB",
	maxResults=50


	)

pl_response = pl_request.execute()



for item in pl_response['items']:

	vid_id=item['contentDetails']['videoId']
	print(vid_id)
	print()
'''
listas = ['PL1av4CQniLB0dk5LnfWQhBUcRlzo2jBYB','PL952AEBEF137A5446']
archivos=[]
pagina=None
aux=True

while aux==True or pagina!=None:
	pl_request = youtube.playlistItems().list(
	part='contentDetails',
	playlistId="PL952AEBEF137A5446",
	maxResults=50,pageToken=pagina


	)

	aux=False
	pl_response = pl_request.execute()
	try:
		pagina=pl_response['nextPageToken']
		archivos.extend(pl_response['items'])
	except Exception as e:
		pagina=None
	
	#print(len(archivos))


print(archivos[0]['statistics'])


