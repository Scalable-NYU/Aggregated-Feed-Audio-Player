import boto3
import json


dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('USER')

json_file = open('./data/user.json','r')
users = json.load(json_file)

for user in users['users']:
	name = user['name']
	userid = user['id']
	print('Adding user:'+name+' '+userid)
	user_table.put_item(
		Item={
			'User':name,
			'Id':userid,
		}
	)






