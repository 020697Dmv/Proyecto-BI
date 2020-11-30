import json
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

from googleapiclient.discovery import build
#api_key='AIzaSyDEyzx3wWj6e1NGuw_bBngQB-2anQ_uda4'
#api_key = 'AIzaSyBvL8A6Gheekl91Z9ppRPJ06c_YygLNNX8'
api_key='AIzaSyDiNy32RaXR7QxZpwCrZXluQ4fOgDuhWeU'
youtube = build('youtube', 'v3', developerKey=api_key)

#Endpoint que solicita los detalles de una lista en especifico


listas1 = ["PLmBFTxNFZbn8X-sFRiOBraJ5p3hf0TVCo","PL952AEBEF137A5446",
"PLK2zhq9oy0K6rjySCH1nARTssbv8m2Kfm","PLJvQXRgtxlumTgSFCMV3aPajZrG-84ezO"]

listas = ["machine learning tutorial","Deportes Quindio","Inteligencia de negocios",
"sociedad del cansancio", "byung chul han","Python tutorial"]

Canales=["HolaSoyGerman","vegetta777","EminemMusic",
"elrubiusOMG","Fernanfloo","TheEllenShow"]
archivos1=[]
archivos=[]
canal=[]
pagina=None
aux=True

def cargar(list,nombre):

	
	for index,i in enumerate(list):
 	 
  		s3.Bucket('youtubes3').put_object(Body=json.dumps(i), Key="/BI/youtube/"+nombre+"/"+str(index)+".json")



while aux==True or pagina!=None:
	print("iiiiiiiiiiiiiiiiiiiittttttt")
	pl_request = youtube.playlistItems().list(
	part='snippet',
	playlistId="PLkLimRXN6NKw24PUEZqHW24CwphBZRDw3",
	maxResults=50,pageToken=pagina


	)

	aux=False
	pl_response = pl_request.execute()
	try:
		pagina=pl_response['nextPageToken']
		
		archivos.extend(pl_response['items'])

		print("-----------------------------------------------------------------------------")
	except Exception as e:
		pagina=None
	
	#print(len(archivos))

print(archivos)
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

	print(y)
	pl_r = request_channel.execute()

	canal.extend(pl_r['items'])

cargar(canal,"channel")

