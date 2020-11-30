import json

from googleapiclient.discovery import build

api_key='AIzaSyBvL8A6Gheekl91Z9ppRPJ06c_YygLNNX8'

youtube = build('youtube', 'v3', developerKey=api_key)


listas = ["machine learning tutorial","Deportes Quindio","Inteligencia de negocios",
"sociedad del cansancio", "byung chul han","Python tutorial"]
archivos1=[]
pagina=None
aux=True

'''while aux==True or pagina!=None:
  pl_request =youtube.search().list(
    q='machine learning tutorial',
     part='snippet', type='video',
      maxResults=50,, pageToken=pagina1)

  pl_requests=youtube
  aux=False
  pl_response = pl_request.execute()
  try:
    pagina=pl_response['nextPageToken']

   
    archivos.extend(pl_response['items'])


  except Exception as e:
    pagina=None
  
  #print(len(archivos))

#print(archivos[0])
'''

for x in listas:
  pl_request1 =youtube.search().list(
      q=x,
      part='snippet', type='video',
        maxResults=3)
  print(x)
  #pl_requests1=youtube
  pl_response1 = pl_request1.execute()
    #try:
    #  pagina1=pl_response1['nextPageToken']

    
  archivos1.extend(pl_response1['items'])
  
for i in archivos1:
  print(i)
  print(".......................................")

