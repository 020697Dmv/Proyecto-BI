import json

from googleapiclient.discovery import build

api_key = 'AIzaSyDEyzx3wWj6e1NGuw_bBngQB-2anQ_uda4'

youtube = build('youtube', 'v3', developerKey=api_key)


listas = ['PL1av4CQniLB0dk5LnfWQhBUcRlzo2jBYB','PL952AEBEF137A5446']
archivos=[]
pagina=None
aux=True

while aux==True or pagina!=None:
  pl_request =youtube.search().list(q='machine learning tutorial', part='snippet', type='video', maxResults=50, pageToken=pagina)

  pl_requests=youtube
  aux=False
  pl_response = pl_request.execute()
  try:
    pagina=pl_response['nextPageToken']

   
    archivos.extend(pl_response['items'])


  except Exception as e:
    pagina=None
  
  #print(len(archivos))

print(archivos[0])

'''for x in archivos:

  dir = 'C:/Users/userr/Desktop/Poryecto BI/SC3'

  f = open(dir+x['id']['videoId']+".json", "x")

  f.write(json.dumps(x))
  f.close()
