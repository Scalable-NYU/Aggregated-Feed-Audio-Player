import boto3
import json

dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('USER')
secret_table = dynamodb.Table('SECRET')
twtr_table = dynamodb.Table('TWTR')

json_file = open('./data/user.json','r')
users = json.load(json_file)
'''
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


json_file = open('./data/secrets.json','r')
secrets = json.load(json_file)

user_key1 = 'consumer_key'
user_key2 = 'consumer_secret'
user_key3 = 'access_token_key'
user_key4 = 'access_token_secret'

for userid_key in secrets.keys():
	user_keyset = secrets[userid_key]
	consumer_key = user_keyset[user_key1]
	consumer_secret = user_keyset[user_key2]
	access_key = user_keyset[user_key3]
	access_secret = user_keyset[user_key4]
	print('Adding user:'+userid_key)
	secret_table.put_item(
		Item={
			'User_ID':userid_key,
			user_key1:consumer_key,
			user_key2:consumer_secret,
			user_key3:access_key,
			user_key4:access_secret,
		}
	)
'''

json_file = open('./data/twtr.json','r')
twtr = json.load(json_file)

post_key1 = 'screenName'
post_key2 = 'text'
post_key3 = 'quote_count'
post_key4 = 'reply_count'
post_key5 = 'retweet_count'
post_key6 = 'favorite_count'

for userid_key in twtr.keys():
	for post in twtr[userid_key]:
		k1 = post[post_key1]
		k2 = post[post_key2]
		k3 = post[post_key3]
		k4 = post[post_key4]
		k5 = post[post_key5]
		k6 = post[post_key6]
	print('Adding user:'+userid_key)
	twtr_table.put_item(
		Item={
			'User_ID':userid_key,
			post_key1:k1,
			post_key2:k2,
			post_key3:k3,
			post_key4:k4,
			post_key5:k5,
			post_key6:k6,
		}
	)

	



