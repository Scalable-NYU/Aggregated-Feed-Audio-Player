import boto3
import json

dynamodb = boto3.resource('dynamodb')

meta_table = dynamodb.Table('META')
twtr_table = dynamodb.Table('TWTR')


with open('./data/meta.json','r') as json_file:
	meta = json.load(json_file)

for each in meta:
	meta_table.put_item(
		Item = each
	)
	print(each['user_id'] + ' is created!')
