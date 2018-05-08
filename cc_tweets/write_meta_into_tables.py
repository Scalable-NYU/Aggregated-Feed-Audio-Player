import boto3
import json

# dump meta json into dynamodb
dynamodb = boto3.resource('dynamodb')
meta_table = dynamodb.Table('META')

with open('./data/meta.json','r') as json_file:
	meta = json.load(json_file)

for each in meta:
	meta_table.put_item(
		Item = each
	)
	print(each['user_id'] + ' is created!')

# create s3 folders
s3 = boto3.client('s3')
res = meta_table.scan(ProjectionExpression="user_id")
user_list = [dic['user_id'] for dic in res['Items']]

for usr in user_list:
	s3.put_object(Bucket='cc-project-s3', Key=usr + "/")
