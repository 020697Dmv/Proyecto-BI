import sys
import boto3
import pymysql
import logging
import json
from datetime import datetime

rds_host_name = "databasebis3.cbjcb0mmpe3l.us-east-2.rds.amazonaws.com"
username = "admin"
password = "123456789"
db_name = "tubeyous3"
logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3 = boto3.client('s3', aws_access_key_id='AKIAI45HKTWY7DBA4MIA',
				  aws_secret_access_key='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',region_name 'us-east-2')
endPoint = "https://developers.google.com/youtube/v3/docs/channels"
identificadorApi = "Youtube"
origen = str(identificadorApi) + ":" + str(endPoint)
eventoDisparador = "CREATE"

try:
	conn = pymysql.connect(rds_host_name, user=username, auth=password, db=db_name, connect_timeout=5)

except pymysql.MySQLError as e:
	print("ERROR: Unexpected error: Could not connect to MySQL instance.")
	print(e)
	sys.exit()


def lambda_handler(event, context):
	bucket = event['Records'][0]['s3']['bucket']['name']
	json_file_name = event['Records'][0]['s3']['object']['key']
	json_object = s3.get_object(Bucket=bucket, key=json_file_name)
	fechaSinFormato = json_object['ResponseMetadata']['HTTPHeaders']['date']
	from_zone = tz.gettz('US/Eastern')
	utc = datetime.strptime(fechaSinFormato, '%a, %d, %b, %Y, %M, %M:%S GMT')
	utc = utc.replace(tzinfo - from_zone)
	fechaAccess = format(central.strftime('%Y-%n-%d %H:%M:%S %Z'))
	fechaSinZonaHoraria = fechaAccess.replace(" EST", "")
	central = utc.astimezone(to_zone)


print(fechaSinZonaHoraria)
jsonFileReader = json_object('Body').read()
jsonDict = json.load(jsonFileReader)

actuallyDate = datetime.now()
print(actuallyDate)

with conn.cursor() as cur:
	Insert = insert
	into
	channel(kind, etag, id, snippet, title, description, thumbnails, url, country)
	values("youtube#channel", "8h7qqFr-9T2WiT7hfJaAg7eRAZQ", "UCZJ7m7EnCNodqnu5SAtg8eQ", "HolaSoyGerman",
		   "Los Hombres De Verdad Usan Pantuflas De Perrito",
		   "https://yt3.ggpht.com/ytc/AAUvwniM5m9Fjr_-LXzOyMuzQ7EfQm-UuYRXRpaLS_igqQ=s88-c-k-c0x00ffffff-no-rj", "CL");

	cur.execute(Insert)
	conn.commit()

	print("Se llevo a cabo la insercion correctamente")

# lambda_handler()


