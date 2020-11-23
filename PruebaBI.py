from googleapiclient.discovery import build

api_key = 'AIzaSyCK2qE6uIz7QLqybqW9SX12r5MokRFkF4M'

youtube = build('youtube', 'v3', developerKey=api_key)

pl_request = youtube.playlistItems().list(
	part='contentDetails',
	playlistId="PLw-VjHDlEOgso_-R_g0FkFL1qd5D6vbxD"


	)

pl_response = pl_request.execute()

for item in pl_response['items']:

	vid_id=item['contentDetails']['videoId']
	print(vid_id)
	print()
