import json

from googleapiclient.discovery import build
#api_key = 'AIzaSyCK2qE6uIz7QLqybqW9SX12r5MokRFkF4M'
#api_key='AIzaSyDEyzx3wWj6e1NGuw_bBngQB-2anQ_uda4'
api_key='AIzaSyAZ6mWtOKz6bAo8sNz6sgdAXqKlIJ-y1oU'
youtube = build('youtube', 'v3', developerKey=api_key)

#Endpoint que solicita los detalles de una lista en especifico

listas = ['PL1av4CQniLB0dk5LnfWQhBUcRlzo2jBYB','PL952AEBEF137A5446']

list1="PL1av4CQniLB0dk5LnfWQhBUcRlzo2jBYB"

archivos1=[]
archivos=[]
pagina=None
aux=True

while aux==True or pagina!=None:
	pl_request = youtube.playlistItems().list(
	part='contentDetails',
	playlistId="PL1av4CQniLB0dk5LnfWQhBUcRlzo2jBYB",
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


# Endpoints que realizar una busqueda en Youtube

pagina1=None
aux1=True

while aux1==True or pagina1!=None:
  pl_request1 =youtube.search().list(q='machine learning tutorial', part='snippet', type='video', maxResults=50, pageToken=pagina1)

  pl_requests1=youtube
  aux1=False
  pl_response1 = pl_request1.execute()
  try:
    pagina1=pl_response1['nextPageToken']

   
    archivos1.extend(pl_response1['items'])


  except Exception as e:
    pagina1=None
  
  #print(len(archivos))

print(archivos1[0])



# Endpoints que realizar una busqueda de las estadisticas de un Canal


request_channel= youtube.channels().list(

                part='statistics',
                forUsername='vegeta777'
            )
responde = request_channel.execute()

print(responde)