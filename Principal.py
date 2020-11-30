import json
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

from googleapiclient.discovery import build
#api_key='AIzaSyDEyzx3wWj6e1NGuw_bBngQB-2anQ_uda4'
#api_key='AIzaSyAZ6mWtOKz6bAo8sNz6sgdAXqKlIJ-y1oU'
#api_key = 'AIzaSyBvL8A6Gheekl91Z9ppRPJ06c_YygLNNX8'
api_key='AIzaSyDz--xulSkFchn5PWLTPGEt1sYkK2Lxy5w'
youtube = build('youtube', 'v3', developerKey=api_key)

#Endpoint que solicita los detalles de una lista en especifico


listas1 = ["PLmBFTxNFZbn8X-sFRiOBraJ5p3hf0TVCo","PL952AEBEF137A5446",
"PLK2zhq9oy0K6rjySCH1nARTssbv8m2Kfm","PLJvQXRgtxlumTgSFCMV3aPajZrG-84ezO"]

listas = ["machine learning tutorial","Deportes Quindio","Inteligencia de negocios",
"sociedad del cansancio", "byung chul han","Python tutorial"]

Canales=["HolaSoyGerman","vegetta777","EminemMusic",
"Marshmello","elrubiusOMG","Fernanfloo","TheEllenShow"
,"Centripio","Blackpink","pythonizando","hdeleon.net"]
archivos1=[]
archivos=[]
canal=[]
pagina=None
aux=True

def cargar(list,nombre):

	for index,i in enumerate(canal):
 	 
  		s3.Bucket('youtubes3').put_object(Body=json.dumps(i), Key="/BI/youtube/"+nombre+"/"+str(index)+".json")



while aux==True or pagina!=None:
	pl_request = youtube.playlistItems().list(
	part='snippet',
	playlistId="PLK2zhq9oy0K67Rg-k8haJCKMSXbt7Fhtr",
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

cargar(archivos,"lista")



# Endpoints que realizar una busqueda en Youtube


for x in listas:
  pl_request1 =youtube.search().list(
      q=x,
      part='snippet', type='video',
        maxResults=10)

  #pl_requests1=youtube
  pl_response1 = pl_request1.execute()
    #try:
    #  pagina1=pl_response1['nextPageToken']

    
  archivos1.extend(pl_response1['items'])
  

cargar(archivos1,"search")



for y in Canales:
	request_channel= youtube.channels().list(

					part='snippet',
					forUsername=y
				)
	responde = request_channel.execute()

	canal.extend(responde['items'])


cargar(canal,"channel")

